+++
date = "2016-04-04T11:53:30.000Z"
tags = []
title = "Lulu Cheng"
disableComments = true
hideMeta = true
Hide = true
+++

<!--more-->

New York, NY, 10013  
[lulu.cheng90@gmail.com](mailto:lulu.cheng90@gmail.com)  
[l1990790120.github.io/about](http://l1990790120.github.io/about)

### Technology

- Development: Scala, Python, R, Java, Go
- Data: Redshift, Cassandra, Kafka, MQ, Airflow, Superset, Spark, Hive, Presto, Couchbase, MongoDB, Oracle
- Infrastructure: Kubernetes, Helm, Argo, Docker, Cloud Run, GKE, AWS, GCP, Jenkins, Cloud Build, EMR, Lambda, Batch, Hadoop, Bash
- Visualization/Web App: Python (django, flask), html, css, javascript (d3.js, dc.js, crossfilter.js)
- Machine Learning: MLFlow, Kubeflow, XGBoost, LightGBM
- BI: Tableau, Alteryx

### Work Experience

**Software Engineer**, Block, New York, NY
2021-11 to Present

**Master Data Engineer/Manager, Data Engineering**, Capital One, New York, NY  
2020-03 to 2021-11

- Machine Learning Platform
  - Contributing to platform's model building and training module. Create abstraction layer for hyperparameter tuning packages ([Optuna](https://optuna.org/), [SparkML](https://spark.apache.org/docs/latest/ml-guide.html)) to allow easy integration on a variety workflow and experimentation tools ([Airflow](https://airflow.apache.org/), [MLFlow](https://mlflow.org/), [Dask](https://dask.org/), [Argo](https://argoproj.github.io/)).
  - Productionize document vulnerability scan model pipeline. Experiment with [Hugging Face](https://huggingface.co/), [Tensorflow](https://www.tensorflow.org/), [Spark XGBoost](https://databricks.com/blog/2020/11/16/how-to-train-xgboost-with-spark.html) against the full dataset (entire Capital One Retail Bank's S3 documents) to reduce training time.
  - Mentor in internal and external Data and AI/ML projects. Working with team(s) of interns and software engineers to research and prototype new AI/ML packages on enterprise platform.

- Identity and Fraud
  - Leading cross team efforts with product, data science and business operations to "modernize" Capital One's Identity and Fraud tech and data stack in Retail Banking. Re-architect backend APIs and pipeline to enable realtime analytics, experimentations, dashboard monitoring and machine learning model development.

**Senior Data Engineer**, Deloitte Digital, New York, NY  
2019-05 to 2020-03

- Leading adoptions and migration process across group-wide data science and analytics teams to self-service, open-source AI/ML stack. Improve overall stability, quality and performance of AI/ML applications across organization. Streamline and shorten data science experimentation to production cycle time.
- Research, evaluate, contribute and deploy AI/ML stack. Integrate and internalize popular modern AI/ML frameworks ([Kubeflow](https://www.kubeflow.org/), [MLFlow](https://mlflow.org/), [H2O](https://www.h2o.ai/), [XGBoost](https://xgboost.readthedocs.io/), [Bert](https://github.com/google-research/bert), [Spark](https://spark.apache.org/)) into:
  1. YAML configurable pipelines for both ad-hoc experiments and production workflows.
  2. Reusable components with unified CI/CD processes to validate, build, share across experiments easily.
  3. Optimize kubernetes to scale hyperparameter search. Automate scoring services deployment.
  4. Integration with external enterprise data science platforms.

**Senior Software Engineer (Tech Lead)**, PeerIQ, New York, NY  
2018-01 to 2019-04

- Leading the efforts to transform existing data systems to highly distributable, scalable while maintaining flexibility. [Transitioning legacy monolithe ETL application to microservice-architecture leveraging serverless container-based infrastructure, microservice, messaging bus and on-demand function calls (Lambda) with minimum business interruptions and code changes.](https://medium.com/@l1990790120/the-battles-of-etl-bottlenecks-and-how-to-fight-them-bd242dfc6733)
- [Designing and building distributed, serverless ETL system that process with drastically heterogeneous data volumne (GB ~ <5TB)](https://medium.com/@l1990790120/why-spark-is-not-the-distributed-framework-of-the-future-ab974ea75308)
  1. Reduce run time from days+ and dozens of datasets that weren't able to finish to < 30 mins
  2. Without touching a line of business logic code base (10000+ lines)
  3. Up to 50% cost savings on the infrastructure (Ability to scale 1 to 1000 instances only when needed in < 5 mins)
  4. Increase developer productivity. The serverless setup, allow users to run any version at the same time at any scale for quick validation. Users are able to debug one specific record in and step through with minimal local environment setup.
- Designing and building ML models to recommend system parameters based on system logs to offer true zero configuration (other than what needs to be processed) on complex distributed system.
- Leading and coaching a team of data engineers. Managing dynamic competing client requests, internal projects to improve data system's scalability and reliability, supporting engineering of our data products with limited resources.

**Software Engineer**, PeerIQ, New York, NY  
2017-02 to 2018-01

- Design and develop big data infrastructure and spark ETL jobs process 20 yrs+ consumer credit records on AWS EMR with Spark (scala) maintain and support a wide range of query engine such as hive and presto, scheduling (airflow) and notebook tools (jupyter, zeppelin) to support analytics query needs. [Serverless big data warehouse architecture design with S3 as data store and AWS athena (presto) as query engine](https://medium.com/@l1990790120/how-we-do-serverless-big-data-etl-olap-queries-15979a71574).
- Design highly scalable production grade machine learning environment to support internal data science needs.
- Develop highly scalable, 15~20x faster valuation/projection microservices with python, go through kafak managed with kubernetes.
- Design and develop internal/external data API for ETL automation to provide continuous automated data quality monitoring tool for ETL pipeline.

**Data Analyst**, McGraw Hill Education, New York, NY  
2015-05 to 2017-02  
Work with management and leadership to develop analytics and dashboards around company strategy and operation

- Implement classification algorithms (SVM, Logistic Regression, Decision Tree, Random Forest, KNN and other ensemble methods) to predict fraud orders from 400+ million transaction data
- Text mining on customer service inquiries to tag and identify high-demand issues
- Develop forecast approach using unsupervised algorithms (EM and K-means) to group similar time-series trends and ARIMA model to forecast on group-aggregate trends
  - [Forecast 7000 US colleges enrollment in the next three years](https://l1990790120.github.io/post/2015-12-14-college-enrollment-forecast-inst-level/)
  - Cluster sales patterns on 1.5+ million titles and use classification algorithms to predict the sales patterns of new titles using only non-transactional features
- Apply unsupervised algorithm on 16+ million student records to create segmentation and analyze usage behavior
- Work with technical teams and business teams to develop ETL in python that parse text data from legacy system into csv feed for Oracle Supply and Demand Planning system
- Develop dashboards and tracking applications for customer service and inventory

**Statistical Analyst**, Radius Global Market Research, New York, NY  
2014-04 to 2015-05  
Work with major brands in eCommerce, retail and technology:

- Manage and execute analytics requirements of market research projects
- Design and develop experiments on front-end to collect user data (html, css, javascript, jquery)
- Run algorithms on customer segmentation, price elasticity, shelf display optimization
- Develop dashboards in Excel VBA based GUI tools and web applications

**Data Analyst**, Baldwin Richardson Foods, Rochester, NY  
2013-10 to 2014-03

- Integrate legacy system into SAP application
- Design statistical metrics for real-time reporting in R and Excel to monitor production line

### Education

**Master of Science, Computer Science**, Georgia Institute of Technology  
2015-01 to 2017-04

- Specialization: Machine Learning
- Teaching Assistant for Educational Technology

**Master of Art, Economics**, Syracuse University, Syracuse, NY  
2012-07 to 2013-05

**Bachelor of Art, Political Science**, National Chengchi University, Taipei, Taiwan  
2008-09 to 2012-07

### Volunteer

**Data Expert**, [Datakind](http://www.datakind.org/), New York, NY  
2019-04 to 2019-05

- Work with [Plentiful](https://www.plentifulapp.com/) to analyze their pantry and survey data

**Data Expert**, [Datakind](http://www.datakind.org/), New York, NY  
2018-06 to 2018-12

- Work with [Commit](https://commitpartnership.org/) (education) to setup their big data infrastructure to support data science efforts on Azure

**Data Expert**, [Datakind](http://www.datakind.org/), New York, NY  
2016-04 to 2016-10

- Work with [Threshold](http://www.thresholds.org/) (health care) to setup their analytical data warehouse in MongoDB and develop dashboard in flask + d3

**Volunteer**, [Humanitarian Data Exchange](https://data.hdx.rwlabs.org/)  
2014-05 to 2014-11

**Volunteer**, Statistics Without Borders  
2013-11 to 2017-8

### Professional Development

[coursera.org](https://www.coursera.org/)

- Deep Learning Specialization by deeplearning.ai
  - Sequence Models
  - Convolutional Neural Networks
  - Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization
  - Neural Networks and Deep Learning
  - Structuring Machine Learning Projects
- An Introduction to Interactive Programming in Python, Rice University
- Practical Machine Learning, John Hopkins University
- Machine Learning, Stanford University

[udacity](https://www.udacity.com/)

- Grow with Google Challenge Scholarship
- Tensorflow free course
