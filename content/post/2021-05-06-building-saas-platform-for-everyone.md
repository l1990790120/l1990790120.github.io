---
title: "Building SaaS Platform for Everyone"
date: 2021-05-06T20:00:38-04:00
tags: ["tech", "startup", "software", "engineering", "SaaS", "apiobuild"]
---

As some of you may know, with the help of many very talented and kind people, I alone with others have been building out a teeny tiny SaaS platform [apiobuild.com](https://apiobuild.com/) in the past several months - A low code platform enabling everyone to create automation software at ease. We started the project as pandemic hit, people were getting creative with their career (out of necessity or exploration), we saw a healthy demand where people really needs some form of very niche software yet have no clue how to get started.

As someone who works for large company building software at scale. It's a torture to see individual business owners have to lose sleep over verifying a domain, consolidating spreadsheets, generating and sending invoices. I can't help but think, even when there's a SaaS for almost anything one could possibly need to run businesses, why are people still suffering?

## Monstrous SaaS

To help small businesses who's struggling on the technical front, I try to first setup solutions for them myself on various SaaS platforms such as [square](https://squareup.com/us/en), [wix](https://www.wix.com/), [mailchimp](https://mailchimp.com/), [omnisend](https://www.omnisend.com/) and many many more. I started to realize, just because there is a SaaS for every need, doesn't mean you could really onboard yourself to ten different platforms and actually solve your problem.

In order to achieve economies of scale, SaaS platforms have to generalize and expand upon their original business domain to attract customers with broader use cases. That's in general a very good thing for the consumers. Before, it's only possible to build e-commerce websites with Wordpress or Shopify. Nowadays, every website builder platform has an e-commerce component ([wix](https://www.wix.com/), [squarespace](https://www.squarespace.com/), [godaddy](https://www.godaddy.com/)), even payments ([square](https://squareup.com/us/en)) and email automation ([mailchimp](https://mailchimp.com/)) platforms have built out their own e-commerce functionality. Ultimately, the more choices there are, the more likely customers would be able to find a product that suits their needs.

The bigger a SaaS platform is, the more complicated it is to onboard or offboard. Common SaaS growth model is building out more functionality to suit more use cases in order to gain user base. Monstrous SaaS platform inevitably sacrifices usability and simplicity for users with simple needs. Worse, in order to create platform lock-in, that is, making leaving a platform as difficult as possible so users are stuck with the platform even if they outgrow or are no longer satisfied with the product, platforms often make data and processes migration very difficult.

While it's justifiable most SaaS platforms opting for more functionality to sustain growth, users stand no chance to keep their nice and simple solution nice and simple.

This makes me think, is there an alternative for SaaS to grow? An alternative that doesn't lock customers in or add functionalities that most people don't need. The alternative is usually call 'Custom Software'. The type of software that companies pay good amount of money for developers to build. Software that serves very specific purpose and the company has the full freedom to take it whichever direction suits the business needs.

It's even difficult for developers to build great custom software, let alone average people. There are  reason for this:

1. Engineering is complicated. Building technology often requires substantial expertise and resources.
2. Building software is not the hardest part, maintaining is even more expensive.
3. It's hard to predict long term business use case. Pivoting could be detrimental to a business if the technology isn't built for it.

I've heard countless horror stories where businesses hire consultants or agencies to build something custom and left with useless code either

1. the businesses have already spent way over budget and have no choice but to live with a suboptimal solution
2. the businesses have no choice but to build from scratch even though if done carefully, it's completely avoidable.

## Scalable Custom Software

Is it possible to build a SaaS platform which users can ...

- onboard and pay only what they need
- have the complete freedom to integrate or extend based on their needs, whether th ey are technical or not
- have a community of users to continue to support and maintain the software they are using

And the platform could still grow and maintain profitability.

I think it's possible. Developers have long enjoyed the benefits of open source software with the exact same benefits. Companies like [elastic search](https://www.elastic.co/), [redis labs](https://redislabs.com/), [databricks (spark)](https://databricks.com/), [preset (airflow/superset)](https://preset.io/) have all started from open source. Earlier in the days, it's common for developers, instead of building our own, fork these open source code, tailor towards our needs and contribute back.

Note the word: **Developer**. To take advantage of these great open source software (which I argue most of the close source software is built upon the open source ones), users have to be technical. They have to know enough to host and implement customization.

## Closing the Gap for Everyone

What is it that's stopping non-technical, or rather, **most** people from taking advantage of open source software directly? Meanwhile, companies like AWS makes great profits from the community contributed software.

In my opinion, software on its own is worth nothing. They are only worth the value if they could solve substantial real world problems. To **most** (that is, non-technical) people, it's hard to see the direct benefits of technology. Tech companies spends a great amount of resources to develop product use cases, in other words, to map tech solution back to the actual problem or study and survey the actual problem to create the tech solution.

For example, a computer vision algorithm that could track your face isn't really that exciting to most. However, put the algorithm in snapchat and give everyone furry ears in the camera is a 50b business.

If we could help people identify product use cases for various open source software that's currently only accessible on proprietary SaaS platform, I am confident creative and innovative entrepreneurs like myself will be more than happy to DIY out their own tech solution.

Not just for non-technical users. We solve for developers too. Hosting and maintaining software is hard. Even developers are willing to pay AWS just to use the **hosted** free software. Security, stability, scalability is at the heart of every devops engineer.

By having a common and robust layer of CI/CD processes, platform can take care of the laborious devops work, developers can contribute directly to the code base and release features at any moment. We could potentially create a true **D2C** software platform.

## Yet Another SaaS

Going back to the platform we've created: [apiobuild.com](https://apiobuild.com/). Although it's still a teeny tiny platform with much more catch up to actually deliver what's promised, we were able to meet a good number (way beyond our expectation) of builders and entrepreneurs who's willing to build with us.

Working with our users, not only we've become friends, we've also learned a great deal on how they run their business. Through solving problems together, we've come to the realization that great software product should not only be offering a solution, the more powerful thing is to also teach users about the problem space. By building together, we were able to show our customers how design, marketing, payments, supply chain etc. is done at scale, and how they could adapt conventional approaches to their own needs.

In the long run, we hope to create a platform where technology is no longer a barrier but an enabler for anyone who's creating a business. Ambitious innovators could solve problems **for the community** with technology **by the community**.
