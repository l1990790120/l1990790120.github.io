+++
title = "What's Shared in Good Data Pipelines?"
date = "2018-04-21T15:20:10.000Z"
tags = ["data-engineering", "infrastructure"]
+++

Planning resources for data systems usually involves more than a load balancer, in many data processing pipelines, it’s common to see some of the steps are more resource demanding while others are simple and quick, some needs to be happened in a specific setup (say a spark cluster as opposed to a linux box with python installed) while others don’t.

Here are some things to think about when you are building or trying to improve existing data processing pipelines.

## Poor Planning of Resources

90% of the time, bottlenecks are due to poor resource planning — either it’s difficult to scale when the demand spike (have too many data processing jobs but not enough core/memory to allocate), or wasting money on under-utilized resources.

### Flexibility to Scale

Clusters are scalable but not necessarily flexible (rarely they aim for flexibility but rather having the ability to scale for high demands). For example, databases or data stores are often easier to scale up than down. Scaling down often incurs interruptions for running jobs (ECS and EMR clusters for example). This introduces difficulties for organizations with smaller budget and lower fixed demand where jobs are often customized and unscheduled to maintain their infrastructure cost effectively.

### Sharing a Weird Pool of Resources or Inflexibility in Resource Specifications

Even if we have the flexibility to scale the infrastructure quickly and easily with minimal interruptions, being able to customize resource requirements and guarantee the demands are met could further enable us to fully utilize the resources cost effectively. In different stages we might want bigger or smaller executors, depends on how the backend of the executor is setup, sometimes it’s difficult to guarantee resource available for a job.

For example, say we have a 3 nodes cluster running our database, resources available will be different when there’s one query as opposed to ten queries as opposed to a hundred queries. This introduces uncertainties in estimating tasks’ SLA and eventually becomes the bottleneck when things get busy.

Another classic example is not being able to customize resource specifications for different steps. In a typical spark application, we often mixed map and reduce together as a monolithe application. This is a problem, because most of the time we need small but many executors in map step and less but bigger executors in reduce step. We either give it more memory and wasting resources in the map step or blowing up reduce step in order to fully utilize resources.

## What's in Good Data Pipelines?

Ok, those are all valid and obvious explanations, the real question is — how do we solve them? Instead of being very specific about how we solve those problems, I wanted to first share some of my personal philosophies about data engineering.

### The Granular the Better

Traditionally, we think of ETL as batch processing. We bring up big boxes and process a bunch of them at a time. But time is changing, so is the pricing model of computing resources. Instead of on-prem boxes, we can get as granular as on demand function runs (AWS Lambda or Azure Function). The more atomic the processing unit is, the easier it is on the infrastructure setup, the lighter the resources requirement is, the more efficient resource allocation could be.

Humans are risk averse, so should our systems be. [The classic psychology theory: even though taking the gamble might win one some money, if the stake is too high, one rather not take the chance.](http://web.missouri.edu/~segerti/capstone/choicesvalues.pdf) Even though running one huge job might save us some overhead and complexity to track job status, but it could also mean we waited a 3 hours for nothing, slow feedback loops is one of the major complaints from data engineers (or to put it differently — [watching paint dry](https://medium.com/@maximebeauchemin/the-downfall-of-the-data-engineer-5bfb701e5d6b)). The quicker a job can fail, the easier we can troubleshoot and the happier the engineers will be.


### E is for Event and Queue is the New Resource Manager

[Ok, I stole the headline.](https://blog.iron.io/e-is-for-event-a-fresh-take-on-etl/) The post is rather irrelevant but I thought it’s a good headline to borrow. [Traditionally we regulate our resource demand by scheduling as we have more fixed supply of computation resources.](https://www.cloverdx.com/blog/event-driven-design-vs-timetable-scheduling) As the cloud services evolve, with serverless offerings and per second ec2 billing, for a little premium, we can actually request as much resources as we need. This is a very great thing for data engineers.

Just think about it, why is software way more scalable than manufacturing? How do you scale manufacturing? By building more plants. How long does it take to build a plant? Depending on the size of the plant, but way longer than requesting a new ec2 box that’s for sure. On demand function calls or serverless container runs (such as AWS Fargate) means we can expand the supply without building a plant but rather renting a manufacturing line for a few mil seconds in another plant. Making it unnecessary to have boxes up and running at all times.

With all these cool tools, how do we scale as fast and flexible as we can with minimal interruptions? Instead of managing resources with timetables or setting up weird pools of resources and load balancer. There’s this great invention of queues. If you go to stores, people get in queues to checkout, no matter how many customers are in line, the cashiers are business as usual. The customer won’t get less of a cashier’s attention if there are more demands (no weird pool of resources), the manager doesn’t have to recognize how many things a customer’s buying and assign to those who buys more to the less busy cashiers (no load balancing). Instead, if the queue gets very long, without any interruptions, the manager simply has to add clerks to cashiers. Same wisdom applies to resource planning in the modern data engineering world. The processor should never worry about demand but just focus on its job — processing. Adding or removing processors shouldn’t interrupt the current processors at all, but instead, when the demand spikes, add the job requests to the queue, the orchestrator can monitor the demand (like the store manager) and add processors as needed.

## In Practices

One thing I really enjoy about microservice architecture — I can swap the entire infrastructure that a system is running on without anybody even noticing. The interesting thing about swapping infrastructure is that (at least for me), really, no one cares about where is it running on, as long as it’s running. Environment are not as important as you thought as long as it does what it promises and it does not break.

### Repackaging Monolithe as Microservice

If you are like us (at PeerIQ) still running some legacy monolithe service and you’d like to try this new data engineering practice with minimal interruptions to your day-to-day business — One thing I’ve done with our monolithe application is to add different entry point to access different modules. Running them as a set of microservices (docker containers) but only calling those different entry point in different service. That way, you segment out steps as a service and orchestrate them on different infrastructure independently so they no longer fight for resources on a single box.

### Introducing the Concept of Queue in Process

While you are breaking up monolithe into microservices, try not to use http requests/triggers to link them but queues in between. There’s two great things about queue, not only it can give you flexibility in scaling with no interruptions, some also offers to let you playback as many times as you want and shard (partition in Kafka’s terminology) it for you. The further you follow this strategy, the less and less batch job you need.

### Microservice becomes Lambda Function, Queue is still Queue — Infinite Scalability!

What I’ve found myself doing ultimately — If something’s already microservice, [I’ll package it as lambda functions and use SQS as message queue with the same architecture.](https://medium.com/@PaulDJohnston/how-to-do-queues-in-aws-lambda-f66028cc7f13) Even though there’s 1000 concurrent invocation limit, it already feels infinite as it’s already beyond the size of kubernetes cluster we can possibly afford.

For me at least, my biggest joy is to get as much flexibility and scalability as possible by swapping infrastructure with minimal code changes and without people noticing. In the following weeks I’ll share some of my own observations in terms of cost, speed, maintenance and issues on my experience moving monolithe ETL running on expensive box to microservice-based mostly serverless ETL infrastructure.