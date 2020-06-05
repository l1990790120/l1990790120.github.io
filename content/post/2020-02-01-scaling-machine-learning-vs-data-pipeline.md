+++
title = "The Differences in Scaling Machine Learning and ETL Pipelines"
date = "2020-02-01T15:20:10.000Z"
tags = ["data-science", "machine-learning", "data-engineering", "infrastructure"]
+++

Data engineers rarely have a say in what's coming in the systems we've built. This presents great challenges where data systems often need to be tolerant about unseen events and at the same time have extra monitoring or QA processes to allow human to determine if the exception actually signals a broader system failure. Machine learning systems have brought this challenge to a new level - in data pipelines, system failures are mostly deterministic or at least reproducible when certain conditions are met. Machine learning applications outputs are stochastic, when exceptions are raised, there are way more probable causes from data to application where stochastic behavior does not make investigation any easier.

Over the past year, I've transitioned from building the more traditional **ETL** or **Data Transformation** into **Machine Learning** pipeline. Throughout the years, I've worked with various distributed technologies (Cassandra, Kafka, Hadoop, Spark, Kubernetes etc.) and built a few custom distributed data systems myself. The data volume can only grow, computation requirements either for a single instance or ability to scale a cluster compute increases. On the journey to help data science teams to do experiments faster, easier and safer, I've learned that scaling machine learning infrastructure is quite different from scaling data pipeline - although they often fall into the same category of **Data Engineering**.

## Scaling both High Performance and Distributed Computing

Think about it, one can scale workers two ways:
1. Train a worker to do work more efficiently
2. Add more workers

Scaling computation is not much different, the former falls into the category of HPC (High Performance Computing) and the latter is called **Distributed Computing**. [I am a long time advocate for Distributed Computing over HPC, at least, for data pipelines.](/post/2018-04-21-good-data-pipelines/#the-granular-the-better) My view has been drastically shifted as I work with more and more machine learning algorithms.

A very distinct difference between **Machine Learning** and **Data Processing** algorithms is that, machine learning algorithms, by nature, is very complicated. Now, there are great initiatives to train deep learning models on multi GPUs and have shown significant performance improvement. Outside of deep learning world where the data accumulated though the training phases is not as ridiculously large, training on classification or regression algorithms such as xgboost is often more efficient on one node as opposed to distributed fashion.

Two main differences between machine learning and ETL pipeline infrastructure:

1. Infrastructure to support machine learning experimentation needs to scale both dimensions, on one hand we need powerful instances to train models even with large data sets; on the other, hyperparameter tuning often means running hundreds or thousands of experiments at the same time where we need to scale also horizontally.
2. Machine learning algorithms are sometimes compiled to be hardware specific, much more strict than data processing algorithms. There are some database technology built upon GPU for performance boosts, especially for graphs or fast analytics. For streaming unstructured event processing, there's no distinction of different hardwares allocating for resources. For machine learning algorithms, however, resource planning software needs to be able to resolve requests with wider range of hardwares requirements.

## Building for Data Scientists

It's important to think about who the platform is supporting and how they are going to use it. When building data pipelines, developers usually have good understanding about the business logic and expected output. Now, not to say that developers won't be able to understand machine learning algorithms, it's just a lot more knowledge transfer is involved than business logics.

The fact that building models requires a lot more expertise that's outside of the engineering domain, it's more efficient to have data scientists to focus on developing models. On the other hand, serving predictions in real time and retrain models with new data is a challenging yet common engineering problems. It's quite common for engineering to work with different disciplines, a collaborative dynamic between the engineering and data science can be key to actually using models in production (beyond research projects).

### Dev to Ops as Data Engineering to Data Science

The relationship between developers and IT/Ops team is not so different from engineering and data science. Developers know their applications the best, it makes most sense to deploy applications their way. However, if everyone wants to do things their way, it'll be very difficult for IT/ops team to keep up with the demand and at the same time maintain the performance and stability of applications running across the infrastructure.

Fast forward to now, cloud is the mainstream for most small tech teams and enterprises are also catching up. All major cloud as well as successful devops team are building or enhancing platforms and toolings (such as Kubernetes) to enable developers to manage their own application deployment while abstracting out best practices in networking, security, monitoring etc.

### It's about Enablement

It's clear, engineering needs to build for enablement not creating limitations on data scientists. Machine learning ecosystem is expanding and changing at a extremely fast pace. ETL has been around for decades, even though custom workload can still be introduced, tools such as SQL or Pandas are quite established - it's easier to find a common ground between business analysts than data scientists and data engineers. Platform supporting data science experimentation needs to provide

1. Greater autonomy on compute resources. Perhaps even dynamic than most data systems. Data science experimentation often has very complicated hardware requirement combined with software configuration for optimized performance.
2. Flexibility on deployment and ad-hoc experimentation. It's a lot more common for data science to run experimentation without committing one line of code. In many ETL systems, we often rely on source control to track the software that process the data. Data science platform needs to capture a lot more metadata about experimentation for reproducibility when the run is triggered ad-hoc.

## Open Source Tools to Scale Data Science

Presented with these challenges, [our team in Hux at Deloitte Digital](https://www.deloittedigital.com/us/en/offerings/customer-led-marketing/advertising--marketing-and-commerce/hux.html) had great success with [Kubeflow](https://www.kubeflow.org/). Things that helped us:

1. Docker to create a standardized layer across different ML algorithms or packages. This allow us to:
   1. Scale ML algorithms on different hardware easily.
   2. Create automated and unified CI/CD process for additional customization implemented on top of vanilla ML algorithms.
   3. It's also a nice way to modularized repeated functionality across multiple machine learning pipelines such as splitting data sets, visualize model performance.
2. Kubernetes for resource planning. We are able to tag both instances and container compute requirements easily with Kubeflow pipeline dsl (backed by [Argo](https://argoproj.github.io/argo/)). Data scientists can easily specify hardware type, core/memory specs. Thanks to Kubernetes, VM permissioning and auto-scaling and creds management are abstracted away from them.

Now, this is not to say Kubeflow and Kubernetes are antidote to all problems. As it's been running for several months, we are now facing new engineering challenges:

1. Retries, monitoring and alerting is not as robust as more mature pipeline orchestration packages such as [Airflow](https://airflow.apache.org/). Not that it's hard to implement, but it's a very distinct difference from other orchestration tools.
2. If the team is not familiar with packaging with docker and running containers on kubernetes, this can be quite a learning curve.
3. Integration testing is difficult when there's ad-hoc workflows. Extra layers of protections needs to be built for **productionized** workflows.
4. No open-source "repository" to share or fork re-usable resources. On google cloud, one can access [AI Hub](https://cloud.google.com/ai-hub/). For rest of the world, other than writing custom module to share component over github, I have found no easier way to copy versioned re-usable components.

One last note. Those who are on the market to look at machine learning platforms or frameworks, there are many more options. The space is still under rapid development and is far from convergence. Other tools to look out for:

* [cortex](https://github.com/cortexlabs/cortex)
* [mlflow](https://mlflow.org/) -- tried, not easy to extend and reproduce.
* [comet](https://www.comet.ml/)
* [Pachyderm](https://www.pachyderm.com/)
* [Polyaxon](https://polyaxon.com/)
* All major cloud have their own **Managed ML** product. Sagemaker in AWS and Azure ML in Azure.

Here's a even more extended list of tools on reddit -- [link](https://www.reddit.com/r/MachineLearning/comments/bx0apm/d_how_do_you_manage_your_machine_learning/).

Happy data engineering!