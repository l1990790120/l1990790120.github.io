+++
title = "Hosting Pypicloud on Google Cloud Run for Free"
date = "2019-08-21T23:59:00.000Z"
tags= ["pypi", "gcp", "python", "serverless", "gce", "gcs", "redis"]
+++

I wanted to run free private pypi. There are a couple hosted options such as [https://gemfury.com/](https://gemfury.com/) or [https://pydist.com/](https://pydist.com/) available for as little as $9 per month if you are willing to pay. **BUT** -- if you are not, read on. I will walk through how to host pypicloud on google cloud's free tier: mine is running at [https://pypi.apiobuild.com/](https://pypi.apiobuild.com/).

<!--more-->

## Options, Options, Options

There are a couple options going through my head:

1. Running pypicloud docker container on [google compute engine](https://cloud.google.com/compute/) (VM).  
   This is probably the most straightforward way, however, one needs to figure out ssl cert and configure ngnix on his/her own.
2. Running pypicloud docker container on [gke](https://cloud.google.com/kubernetes-engine/) (kubernetes cluster).  
   This is probably what I'd do at work as I can always assume there's enough applications to share cluster resources and someone to pay for it. Actually, running gke with minimum 3 nodes of n1-stanrdard costs around 70 bucks per month -- nope, I am willing to spend some time to save $840 a year.
3. Running pypicloud docker container serverlessly on [cloud run](https://cloud.google.com/run/)  
   Eventually I landed on this option as ssl cert is already configured and deployment is relatively easy with [cloud build](https://cloud.google.com/cloud-build/). With the number of requests I make -- it's practically free.

I went with the third option since it's the cheapest one. Obviously how much it costs depends on your usage, for a couple python packages (I have 5) and extremely light usages (packages pulled in CI and docker build for a couple repository), it's practically free.

## Option 3

### Prerequisite

Before we go over how to achieve this, there are a couple assumptions made about in this guide:

1. You have google cloud account and you have permissions to use cloud run. Note: I have also offered a more "productionized" way to deploy with cloud build, so if you wish to use cloud build for deployment, make sure you have permissions to push images to gcr and use cloud build itself.
2. You need gcloud client installed if you wish to use cloud build

### Application Components

To host pypicloud, there are a couple components in additional to the application itself.

{{<mermaid>}}
graph TD
    Pypicloud(Cloud Run: Pypicloud Application)
    subgraph "Cloud Build: Build Docker Image and Deploy on GCE"
    Pypicloud --- GCS(GCS Bucket:<br> Package Artifacts)
    Pypicloud --- GCE("GCE (n1-standard):<br> Redis running docker on as caching layer")
    end
{{</mermaid>}}

Most people are probably not running this for critical production CI/CD systems, so I want to offer a more manual but easier way first. However, for those who's looking for more end-to-end IaC (Infrastructure as Code) deployment, I've marked the optional scripts in the stesp.

#### Deploy with Cloud Run Button

It's possible to wrap pypicloud deployment in [cloud run button](https://github.com/GoogleCloudPlatform/cloud-run-button). This assumes secrets, GCS bucket's already created and no caching layer. If you just want to try it out quickly, I recommend you to do it this way.  
*Note: pypicloud does let you run in-memory caching, however, because we are running "serverlessly", it basically means no cache.*

#### Deploy with Cloud Build

Use cloud build to script out deployment of all resources required. This includes creating GCS bucket, secrets, and a redis running on tiny vm for caching.

### Steps

Below I will walk though the basic steps, you should use this foundation and improvise on caching backend and/or extend other pypicloud functionality.

#### 1. Creating Required Resources

Depending how you are deploying pypicloud.

##### 1.1 Deploy with Cloud Run Button

If you are deploying with cloud run button, you will have to manually create

1. GCS Bucket: to store artifacts
2. Service Account: Used as role to [https://cloud.google.com/storage/docs/creating-buckets]
3. Create keyring for encryption/decryption
    [https://cloud.google.com/kms/docs/creating-keys#kms-create-keyring-cli](https://cloud.google.com/kms/docs/creating-keys#kms-create-keyring-cli)

    ```bash
    gcloud kms keyrings create [KEYRING_NAME] --location [LOCATION]
    ```

4. 

##### 1.2 Deploy with Cloud Build



#### 2. Building Custom Pypicloud Image

First and for most, we need a pypicloud image for cloud run to use. Actually, pypicloud already provided a Dockerfile here: [https://github.com/stevearc/pypicloud-docker/blob/master/py3-alpine/Dockerfile](https://github.com/stevearc/pypicloud-docker/blob/master/py3-alpine/Dockerfile).

##### Safety First

Because we are running it serverless, it introduces some interesting complications on secret management. To run pypicloud, we will need two secrets:

* pypicloud configuration as it might contain database url
* [creds.json](https://cloud.google.com/docs/authentication/production) to access gcs

Now, even if these files are tiny, I do not like the idea of fetching secrets from blob store in general, both from a security standpoint, but also we introduce latency in fetching these files, and because it's serverless, we may need to fetch them more often than hosting long running process in a conventional way.

For very light usage (like mine), the performance may be acceptable fetching these files from blob storage on the fly, however, blob storage is not designed for high frequency access, let alone web scale, if hit by high volume, it's likely to timeout.

To accommodate this, **I took pypicloud's example docker image as a base and add installed gcloud cli to decrypt secret where encrypted secret are provided as environment variable on the fly.**

##### Generate pypicloud Configuration

In the same [pypicloud-docker repo](https://github.com/stevearc/pypicloud-docker/), they actually also covered how to generate `config.ini`, so this is purely a copy-and-paste from the repo.

```bash
docker run -it --rm -v $(pwd):/out stevearc/pypicloud make-config -r /out/config.ini
```

It's better to review the config and make sure authentication and db url are updated accordingly. If you wish to enable redis instead of in-memory caching, you'll need to add the following lines to the `config.ini`. Note, for security, I have also set password for the caching layer.

```bash
#!config.ini

pypi.db = redis
db.url = <redis url>
```

There are also other caching backend, refer to [https://pypicloud.readthedocs.io/en/latest/topics/cache.html](https://pypicloud.readthedocs.io/en/latest/topics/cache.html) for full documentation.

##### Generate `creds.json` for GCS

To access google storage, one first needs to create a service account with access to gcs and generate a `creds.json` using the account. One can generate this through command line or in google cloud console. Refer to [https://cloud.google.com/iam/docs/creating-managing-service-accounts] for how to   account with the right permission.

```bash
# create service account
gcloud iam service-accounts create <service account>
# generate creds.json
gcloud iam service-accounts keys create creds.json --iam-account <service account>
```

When invoked in cloud run, we need to give the service account permissions to:

* Access GCS

```bash
gcloud projects add-iam-policy-binding <project> \
    --member serviceAccount:<service account>@<project>.iam.gserviceaccount.com \
    --role roles/storage.admin
```

* Decrypt Secret with Key
  
```bash
gcloud kms keys add-iam-policy-binding <project> \
    --location global \
    --keyring <> \
    --member serviceAccount:<service account>@<project>.iam.gserviceaccount.com \
    --role roles/cloudkms.cryptoKeyDecrypter
```

* Deploy to Cloud Run  
    (Optional: This is only required if you are planning to use cloud build for automated build and deploy steps)*

```bash
gcloud projects add-iam-policy-binding <project> \
    --member serviceAccount:<service account>@<project>.iam.gserviceaccount.com \
    --role roles/run.admin
```

##### Encrypt and Decrypt the Secrets

Now that we have all the pieces we need to run pypicloud, we need to find a way to pass it to pypicloud on cloud run. Google cloud also have kms service available for encryption and decryption. First we need to create key ring and key itself. Refer to [https://cloud.google.com/kms/docs/creating-keys](https://cloud.google.com/kms/docs/creating-keys) for details. Once the key is created, we can then use it for encryption/decryption.

For encryption, we first encrypt the file with the key we just created, and then base64 encode and output save locally for the time being.

```bash
# encrypt the file
FILE=<creds.json|config.ini>

gcloud kms encrypt \
    --plaintext-file=$FILE \
    --ciphertext-file=$FILE.enc \
    --location=global \
    --keyring=<> \
    --key=<>

# base64 encode the encrypted file
base64 <<< $FILE.enc > $FILE.enc.base64
```

The file generated can be then can be passed into pypicloud container as environment variables and decrypted on the spot. For decryption, we simply invoke another gcloud cli command.

```bash
FILE=<creds.json|config.ini>

gcloud kms decrypt \
    --ciphertext-file=$FILE.enc.base64 \
    --plaintext-file=$FILE \
    --location=global \
    --keyring=<> \
    --key=<>
```

##### Summary

Finally, everything we need to run the Dockerfile is ready. You can find the Dockerfile to decrypt these secrets on the fly here: [https://github.com/l1990790120/gcloud-run-pypicloud/blob/master/Dockerfile](https://github.com/l1990790120/gcloud-run-pypicloud/blob/master/Dockerfile).

The image simply installs pypicloud and gcloud cli. In `start.sh`, it'll take encrypted, base64 coded string from environment variable, decrypt and echo it into local files. You can find full implementation here: [https://github.com/l1990790120/gcloud-run-pypicloud/blob/master/start.sh](https://github.com/l1990790120/gcloud-run-pypicloud/blob/master/start.sh)
