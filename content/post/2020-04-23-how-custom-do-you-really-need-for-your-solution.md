+++
title = "How Custom Do You Really Need for Your Solution?"
date = 2020-04-23T14:53:45-04:00
tags = ["blog", "career", "work", "software-engineering", "product", "tech"]
+++

Companies who could afford in-house engineering teams often have tendencies to build custom in-house solutions no matter how prevalent that solution already is. To highlight the absurdity, let me give an example: [Jupyter Notebook](https://jupyter.org/). Despite the space being extremely competitive, [Google has Colab](https://colab.research.google.com/notebooks/welcome.ipynb), [Amazon has Sagemaker](https://aws.amazon.com/sagemaker/), [Azure](https://notebooks.azure.com/), [Databricks](https://docs.databricks.com/notebooks/index.html), [Domino](https://www.dominodatalab.com/), [Binder](https://mybinder.org/) all offer similar services and the list goes on, Product or Technology still cannot resist the urge to build one (if not multiple) in-house. Not to mention some notable companies spent $$$$ on building fully integrated notebooks on their platforms.

## Shoulders of Giants

Everyone who works with me knows my strong stance on building something new - if there are existing solutions to a similar problem, one should not attempt to build without fully exploiting the existing ones first.

Engineering's tendency to build something new is sometimes understandable:

- existing ones may not be well-maintained, it takes more time to use it than build a new one from scratch.
- even though existing ones can meet the needs, but not without workarounds and hacks.

I challenge with everyone who wants to build something new to answer these:

- If a team of capable people already attempted at solving a similar problem you are solving, why would you do it better? You are either narcissistic or disrespectful of other people's ability to execute. Otherwise, it's not a people problem.
- Would faster and better technologies always solve the a similar problem better? Do you feel conversations with your mom are better with a smartphone than a landline phone? Smartphones did create ranges of new problems, but not for the ones where there were existing solutions, one couldn't possibly argue texts in bubbles read better than boxes.

**Do not misunderstand this as opposing changes and new technology.** As a matter of fact, I am often the one that brings new technologies into an organization and encourage people to try it out (almost to an annoying level). Let me elaborate more.

## Fix Problem not Solution

One should not "re-fix" a problem, instead, one should constantly try to identify better problems to solve and "re-fit" solutions (existing or new) through the lenses of problems.

The questions are often not asked: what is it that your problem so special from others? Sure, when things are not working, people are frustrated, instead of framing the right problems to solve, perhaps it's easier to solve them first.

Let's take the notebook example (90% based on mixes of true stories):

1. It usually started with no more than setting up credentials, networking to access data and api and some pre-installed private packages.
2. Afterwards, the team wants it to be hosted so they can use it to run recurring reports or other long running jobs.
3. If the project is still alive. Quite likely it has accumulated some users. Now, they need to run certain notebook on GPU, some on micro instance and some others on a spark cluster.

Let's see how engineering will build when stories are rolled out as above without product's help to frame the issues into better problem.

1. A Jupyter notebook docker image with AWS, API credentials configured and some pre-installed packages.
2. Deploy that image on ec2 instances. Configure custom networking, permissioning and monitoring.
3. Add a cli tool to so one can automatically deploy to custom ec2 instances.

Very logical progression, other than not asking the right question in the first place, engineering can hardly be blamed for wasting their time solving problems that's been solved over and over by the internet. Some of them might eventually raise questions after they found out just how many people have approached product's **unique problem** on google. I highly recommend to keep in touch with those engineers who dare to ask these questions, they will at some point prevent teams from wasting $$$$ on useless projects down the road.

## Notorious Custom Solutions

Custom solutions can rarely compete with existing vendor offerings. From the ones built by consultants to the home grown enterprise tools, people rarely have good things to say about them.

Home grown solutions rarely respond to broader market needs but are sourced from problems shared across teams within the company. They rarely have the luxury to step beyond **requirements** and respond to **visions** or **market trends**.

If IPhone was developed by listing out a complete list of problems they want to solve instead of visioning how the future of communication on handheld devices, we will never have IPhone.

If a truly great product can never come from custom solutions, why is it so prevalent?

### No Existing Solutions

When existing solutions don't exist or don't meet the needs, it's easier to opt for building a custom one. When I was looking for ML frameworks, only a handful of them were relatively mature, and we still need to add a number of features for it really be useful. That being said, it's too often product "misunderstands" what they need doesn't exist or what exists doesn't meet their needs. Politics often pushes them to build something anyways instead of calling for surveying on existing solutions.

### Outdated Systems or Cost Constraint

Perhaps a more justified cause is that outdated systems make it difficult to integrate existing solutions. There's only enough budget to build custom features to meet the needs but not enough to rebuild the whole system so that engineering can easily extend upgraded systems with existing solutions. Due to both cost and resource constraints, it's quite common to update only one part of the system while keep the remaining functioning as is so one could keep the customers happy and the cost reasonable. In this case, engineering will often build custom solutions until it's possible to integrate with more permanent solutions.

### Unforeseen Expenses

Real issues that could come with custom solution in a relative near term:

1. It's less likely to stay relevant to the problem its solving. Obviously, once IPhone's out, not long after no one uses Nokia or Motorola.
2. Either the on-going budget for maintenance is no longer there (hint: re-org) or the people and resources to keep it up and running is growing much quicker than the company expected. Afterwards, it's either deprecated forcibly or no one knows how to use it anymore.
3. If it's in an unfortunate state that a custom solution is no longer maintained, migrating off from a solution often comes with a deadline which is never executed with high standards but desperation.

## Summary

On one hand, every company is complaining there's not enough tech talent; on the other, most people or company I talked to want to build similar but slightly different solutions - it got me thinking, what could be the reasons that most companies wants to build something that's already there?

I reflected on different organizations and teams I worked for, and I realized, there's indeed biases towards custom solutions without evaluating whether it's really worth it?

If anything I've learned from this wasteful approach to building custom solutions:

1. If you really have to build one, make it open source, invite others to contribute to it. If the community sees it useful enough, there will be people or resources to keep it going.
2. Otherwise, carefully research your problem space. Do not come to the conclusion that "we can do it" without careful evaluation. The first check may seem trivial, but the on-going maintenance and communication can cost a lot more.

Anyways, happy coding. Focus on what the company does the best, not building one off custom solutions no one likes.
