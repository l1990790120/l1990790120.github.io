---
title: "Thoughts on AI Biases"
date: 2020-08-02T23:37:25-04:00
tags: ["machine-learning", "data-science", "AI", "algorithm", "biases", "software", "engineering", "justice", "politics"]
---

Almost in every AI or Machine Learning conferences I've been to lately, there's a track dedicating to biases or "injustices" in algorithmic decisions. Books have been published ([Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor](https://amzn.to/3k1U4Vs), [Algorithms of Oppression: How Search Engines Reinforce Racism](https://amzn.to/2XjUeh8) etc.) and fear has been spread ([Elon Musk says AI development should be better regulated, even at Tesla
](https://www.theverge.com/2020/2/18/21142489/elon-musk-ai-regulation-tweets-open-ai-tesla-spacex-twitter)).

The fear of unknown is, perhaps, more persuasive than [a realistic survey of the state of AGI (Artificial General Intelligence) development](https://www.nature.com/articles/s41599-020-0494-4). Admittedly, from the very beginning of my career, I despised those who lacks the imagination of how data and algorithms can improve the quality of human decisions - I have always believed that human intelligence could be drastically improved when augmented with the right information at the right time.

## Machine Learning is only good with specialized problems (in 2020)

However, a master degree in machine learning and working in the field has made me realized its limitations. Machine learning algorithm is good at solving a specialized problem - a problem that could be theorized and hypothesize with clear constraints and optimization. It could be as complicated as [go game](https://deepmind.com/research/case-studies/alphago-the-story-so-far), or recognizing [cat in the video](https://www.wired.com/2012/06/google-x-neural-network/).

If we look at the more difficult decisions we have to make in our lives, what are some common traits they share? It's relative easy to decide whether to bring an umbrella with you or not but it's much more difficult to choose a major in college. Why is the latter so much more complicated than the former? Mathematically speaking, when there are too many parameters and no rules fed into an optimization problem, the problem becomes infinitely difficult to solve.

Different from how human brain solves a problem, programs are very good at solving repetitive and tedious steps. Therefore, though we were required to practice arithmetic in middle school, no one practically calculates anything without a calculator in real life. Alphago algorithm, as advanced as it is to search the potential outcomes on the game board and make moves that averages the highest likelihood for it to win the game in relative short time, it's not able to predict 2020 US presidential election for us. There's simply too many variables and too little constraints.

Another great example I was once given in grad school: what was the mechanism in human brain that triggered Wright brothers to figure out how airplane could work by observing how birds fly? How human "learns" is still very much a mystery that engineers can yet replicate on machines.

## Algorithms are byproducts of data

Humans and machines are not so different in this aspect, we both need data to make decisions. [Human brains have the superpower to "jump to conclusions" (Thinking Fast and Slow).](https://amzn.to/3k4Dp3B) Since machines don't have this super power, machines are always much more greedy on data to make inferences in order to make human quality decisions.

One can also think about this as machines will make the most honest decisions based on data it's given. At the same time, because algorithms are so greedy about data, we often have to feed algorithms with the volume of data that's beyond our ability to grasp. The fact that human can neither understand the underlying data nor the [complicated non-linear decision inferences](https://en.wikipedia.org/wiki/Deep_learning) exhaustively is where **the misunderstanding of how machine learning algorithms or AI are BIASED begin to develop.**

## Data is biased

If algorithm is only giving an honest view based on the data provided and we think algorithm is biased, it's likely that the data is biased. [This relationship is clearly established in the field where fairness is a concern.](https://www.brookings.edu/research/understanding-risk-assessment-instruments-in-criminal-justice/)

One of the more popular question often mentioned in AI ethics is [the trolley dilemma](https://en.wikipedia.org/wiki/Trolley_problem). While it's certainly worth governing the behavior of algorithms in tricky situations, this is a dilemma more for humans not machines. If the user rewards the algorithm to save it's own life (with data), the algorithm will save the driver's life and vice versa. There's very little room for ethical discussion algorithm-wise, if anything, the discussion should focus on what if most of the users (which generates the data) rewards self-interest behavior but it's in fact considered less moral?

This leads to the next area of interest, what if users are generating data that's considered less moral and biased but it's getting feed into the algorithms?

## Data is byproduct of human and human is biased

Most AI/ML biases discussions are trying to fix the algorithms or developing evaluation mechanisms comparing predictions by gender, races, ages and other demographic based attribute. A concrete example: [microsoft published an open-source package to score the fairness of a model as by evaluating the parity of various demographic attributes](https://fairlearn.github.io/user_guide/fairness_in_machine_learning.html#parity-constraints).

While controls and governance are always beneficial to help researchers and practitioners understand and mitigate risks, I argue we are not dealing with the actual problem. If the source of a biased model is data and human generates data, a more critical question would be - are platforms publishing decisioning algorithms responsible for fixing their users and further fix the data?

## Regulating human biases

[Facebook responds to their problematic usage of data and algorithms with an oversight board.](https://about.fb.com/news/2020/05/welcoming-the-oversight-board/) [Twitter suspends "fake accounts"](https://techcrunch.com/2020/02/03/twitter-suspends-large-network-of-fake-accounts-used-to-match-phone-numbers-to-users/) It's not hard to see an interesting tension between the "fairness" of decisioning and business growth. Limiting access to different groups of users in order to improve data and algorithms could potentially lead to revenue loss.

Algorithmic decisioning, perhaps newer to social media platforms and more difficult to regulate, is not new to the businesses. In heavily regulated industry such as banks, fairness is required by law. Correctness of credit reporting is bounded by [FCRA (Fair Credit Reporting Act)](https://www.ftc.gov/enforcement/statutes/fair-credit-reporting-act), unbiased decision to credit is guaranteed by [ECOA (Equal Credit Opportunity Act)](https://www.justice.gov/crt/equal-credit-opportunity-act-3). Even written in law, one could still argue it's unfair to those who do not have credit history with established institutions. Whether the intention is self-interest or altruistic, bureau monopolizing credit data (transunion, equifax, fico) has motivated the industry to improve on serving the underserved. A new line of financial products such as [Chime](https://www.chime.com/) or [Petal](https://www.petalcard.com/) requires no credit score claims to provide banking services and credit access the "untapped" population by traditional banking.

## A political and philosophical debate since human history

As I've laid out, AI biases could not be seen solely as a technological but a political problem (or at least, involves human to be part of the solution). As a technologist myself, it saddens me to learn that a solution will not present itself as technology progresses (as opposed to a cure for COVID-19). It's encouraging at the same time that equal right and fairness is an old subject since human history([Equal Employment Opportunity Act](https://en.wikipedia.org/wiki/Equal_Educational_Opportunities_Act_of_1974), [the struggling Affordable Care Act](https://www.healthcare.gov/where-can-i-read-the-affordable-care-act/)) - in fact, [equal right is in our constitution](https://en.wikipedia.org/wiki/Equal_Protection_Clause). A democratic society and government would always strive for these values, it's just a matter of understanding "how"?

## Summary

The post is meant to explain the seemingly abstract relationships between algorithms, data, human and society in the most realistic way possible. By reframing the emerging technology challenges into existing ones, I hope it helps to ground the fluffy AI biases conversations into something more directional and productive ones. From the books I have read or discussions I've participated, very rarely such an obvious yet deep connections was ever established or explored. We often get lost in the possibilities of technology just because it's unseen. Complicated as it may be, technology or science is always bounded to "truth", how it's used will always be a human decision. Nuclear could alleviate energy shortage in France and strengthen its independence among its neighbors or used in World War 2. The differences between AI and nuclear technology, thanks to sci-fi books and movies - anyone could suddenly stretch the possibilities beyond reality without justifying their imagination. To the technologists and policy makers who really wants to build a better future with technology, we should always focus on the fundamental biases present in human society and instrument measures to prevent algorithms magnifying the biases or better yet, reduce the biases.

Happy machine learning!
