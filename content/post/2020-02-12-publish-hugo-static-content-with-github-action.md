+++
title = "Publish Hugo Static Content With Github Action"
date = "2020-02-12T22:12:59-05:00"
tags = ["blog", "cicd"]
+++

About two days ago, one of my coworkers was so fed up by Jenkins and decided to try Github Action. I've been thinking about automating publishing [this github site](http://l1990790120.github.io/) since ... the day I set it up. At work, if I have to setup a CD pipeline, I'd usually put it on Jenkins. But at home, I just want to sit back and relax, I don't want to spend my Netflix time fixing Jenkins (which unfortunately it breaks all the time at work). So, I decided to find a way to setup automated static content publishing process (or the fancy term -- CD) in Github Action for this site (repo: [https://github.com/l1990790120/l1990790120.github.io](https://github.com/l1990790120/l1990790120.github.io)).

## Auto Publish Custom Hugo Docker Image

First tricky thing, because I need to embed ipython notebook and it's usually way bigger than normal static content page size, I have to re-compile hugo to workaround some annoying file length limit. I forked the official hugo repo and added some of my own changes on develop here: [https://github.com/l1990790120/hugo](https://github.com/l1990790120/hugo). If you compare tags with `-p` versus the official release tag, you can easily find the changes I've made on my own: [https://github.com/gohugoio/hugo/compare/v0.64.1...l1990790120:v0.64.1-p](https://github.com/gohugoio/hugo/compare/v0.64.1...l1990790120:v0.64.1-p).

Now, for the CD process, I need to following things to happen:

1. Once a while, pull the latest release from upstream official hugo repo, apply my own change and publish a new patched tag (official release tag with a `-p`).
2. If I push updates to my forking repo, update the latest release patched tag with new changes.
3. For any tag pushed, build and publish custom docker image to docker hub here: [https://hub.docker.com/repository/docker/l1990790120/hugo](https://hub.docker.com/repository/docker/l1990790120/hugo)

For the first two items, I've created a [push-forked-tag.yaml](https://github.com/l1990790120/hugo/blob/develop/.github/workflows/push-forked-tag.yaml) that does the following:  
Every time there's a new push to develop, get the latest tag in upstream (official hugo repo), checkout and cherry-pick all commits from my forking repo, and then publish a patched tag accordingly.  
For the third one, I've created another [publish-docker-tag.yaml](https://github.com/l1990790120/hugo/blob/develop/.github/workflows/publish-docker-tag.yaml) that simply grab the any push to tags, build and publish image to docker hub accordingly.

### Weird Limitation Workaround

Along the way I've also discovered some interesting limitations in Github Action. These two workflows, when running independently, there's no issues at all. The expected flow is that the first workflow triggers the second one by pushing a tag. However, Github Action has a weird limitation such that one workflow cannot trigger another workflow with the same github token (more details discussed here: [https://github.community/t5/GitHub-Actions/Triggering-a-new-workflow-from-another-workflow/td-p/31676](https://github.community/t5/GitHub-Actions/Triggering-a-new-workflow-from-another-workflow/td-p/31676)). I have to create a separate token and feed it into the job. Obviously this introduced several drawbacks as discussed in the above thread also.

Note, I only have to add this extra step because the way I am embedding jupyter notebook. If you don't need to push hugo to its limit, just simply build the tag you need from [https://github.com/gohugoio/hugo/blob/master/Dockerfile](https://github.com/gohugoio/hugo/blob/master/Dockerfile) and use it.

## Set Up Publish

On [hugo docs](https://gohugo.io/hosting-and-deployment/hosting-on-github/#put-it-into-a-script), there's detailed instruction on how to publish to github page. The [publish.yml](https://github.com/l1990790120/l1990790120.github.io/blob/develop/.github/workflows/publish.yml) in my github site's repo literally just copy the doc, but instead of calling hugo binary directly, I put a docker run command with the image I just built from the prior step:

```bash
docker run --rm -v $(pwd):/site -v $(pwd)/public:/site/public l1990790120/hugo:0.64.1-p ""
```

That's all. Now I never to look at these commands again. Anything I merge into `develop` will get published automatically.

## Summary

This adventure took me maybe less than two days. For a pipeline I have been procrastinated to setup for more than 3 years, I really appreciate this feature, and it's almost guaranteed to be free for light usage like this. Obviously the same thing can be done in Jenkins, TravisCI, CircleCI, Cloud Build, there's no doubt about that.

For more containerized CI/CD, for example, one of the CI/CD I had setup needed to use Docker Buildkit to build image. I really need to do some complicated stuff (running docker in docker and build the image against docker in docker daemon etc.) with my CI/CD pipeline (details in my [Stack Overflow answer](https://stackoverflow.com/questions/57175062/using-docker-buildkit-on-google-cloud-build/58440922#58440922)). I can see developing complex pipeline in Github Action can be painful -- solely because there's no easy way for me to test this locally (or maybe it's just that I am not aware of in the matter of two days, but I am happy to learn).

The syntax is also not as "container-native" as some of the other tools out there - CircleCI, Cloud Build. However, I feel this is a conscious decision from github to make the interface simpler. Overall, for light weight pipelines such as the one above or things like closing PR, Issues, generate release notes etc. I highly recommend to try Github Action first if you are setting up new ones.

Happy CI/CD!
