---
title: "Is AI Doing My Work or Making Me Work?"
date: 2026-04-29T20:00:38-04:00
tags: ["software", "engineering", "thoughts"]
---

Or Both. But Mostly Latter..

Once upon a time, to build a website, you had to buy a computer. One day, someone had the brilliant idea to buy many computers that nerdy people like myself could pay to use — we called them servers. Almost 20 years ago, AWS had an even more brilliant idea to buy many servers and let less nerdy people pay to use them — we called it cloud compute. Today, everyone can host a website with a few clicks or sentences. Sound familiar?

During World War II, Alan Turing laid the theoretical foundation for computation. The first computers were programmed by rewiring circuits. Then came assembly language, where you could write instructions instead of moving actual wires. Then C abstracted away the hardware. Java abstracted away the operating system. Python and JavaScript are almost like plain English. Each generation of coding language made programming more and more accessible to more people. Today, LLMs made the programming language natural human language itself. Everyone can build an app.

Technology doesn't make hard problems go away — the problems are just as hard. However, technology makes solutions accessible to people without needing to understand the underlying problem. Each layer of abstraction hides the complexity and lets the next wave of people build on top.

## Accessibility is ONLY the Start

When Ford invented the Model T, cars became affordable to everyone. But driving didn't automatically become safe. It took decades of iteration — seat belts, airbags, traffic lights, speed limits, drunk driving laws, licensing requirements — before driving became safe. Making the car accessible was the easy part. Everything around it was the hard part.

Today, building software became easier than ever. AI made it so everyone can build a beautiful app. But software engineering didn't become easy. Testing, security, infrastructure, scalability, governance, cost, maintenance — is still just as hard. 

## Writing Code ≠ Software Engineering

Don't get me wrong. I'm a super power user of many LLM dev tools. The other day I found out my Cursor usage is #3 in my company. But writing more code doesn't mean doing more work. I spend more time verifying if the code is functionally correct, well-tested, implemented in the way that can support how people want to use it.

As an engineer, I want to build systems that are quick to add new features, not easily hackable, upgradable, not too expensive as usage increases, don't break down very often. Sounds reasonable? Not very obvious. Very often, people (engineers included) hand me a (large) pile of LLM-generated code. I ask -- can you explain what does the code do? How do you know it works? Besides the fact that the buttons do work. Quite difficult, isn't it?

## Build System. Not Prompt

Do you ever need a manual for an iphone? No. Good design just works. The answer to "everyone's building software but nobody knows engineering" isn't to tell everyone to stop building. Nor is it teaching everyone how to build. It's to build systems where good engineering practice is already baked in. What if the code your LLM generates automatically comes with CI/CD, a testing framework, cost estimates, security defaults, monitoring — not because you asked for it, but because that's just how software engineering works?

Speaking in technical terms. Kubernetes didn't make deployment easier. In fact, you can argue it's actually much more complicated. However, it segregates responsibility much better. Application developers can focus on application code and infrastructure engineers can focus on scalability and resourcing. While most will say software engineering is much easier than before, I actually think software engineering is now facing the biggest challenge of our time. How do we build tools so that everyone can build software that works?
