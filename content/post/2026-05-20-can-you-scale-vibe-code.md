---
title: "Can You Scale Vibe Code ?"
date: 2026-05-20T23:55:38-04:00
tags: ["software", "engineering", "thoughts"]
---

<img src="/img/localhost-meme.webp" alt="localhost meme" width="520" style="max-width: 100%; height: auto; margin-bottom: 20px;" />

We've all seen the meme — "check out my app at localhost:1234" Me and many of my fellow engineer friends find it funny. Every other week someone sends me a huge pile of generated code and tells me they made an app. It's like the WebMD moment — when your friends asks you to fix their printers because you're "in tech."

<!--more-->

<iframe src="https://giphy.com/embed/kWp8QC99Z6xFn8bF0v" width="300" height="306" style="display:block;max-width:100%;margin-top:20px;margin-bottom:12px;" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/way-morning-dresser-kWp8QC99Z6xFn8bF0v">via GIPHY</a></p>

If it's not clear already — code is a liability, not an asset. Every engineer knows this joke: if you delete all the code, there will be no bugs. A pile of generated code is not an app. Vibe coding clearly has its limits. I don't build software through chat. Instead, I write about design, tradeoffs, requirements, failure modes, scalability — it's a whole process before even a line gets written.

The fact that anyone can go from "I'd like to build..." to a working prototype in an afternoon — it's incredible. The gap isn't vibe coding itself. It's that it skips the most important questions: what exactly are you building, and how should it be built?

## Things You and the Vibe Coding Chat Don't Talk About

When I build, I think about what happens when it breaks? What if someone tries to hack it? What if I need to add a feature six months from now? How do I update it without taking the whole thing down? How much will it cost to run when more people start using it? I'm not talking about Google scale here. Simply: what if my app has an admin and a regular user and they need different permissions? What if I onboard 10 users and need to reset someone's password? What if my database runs out of space? What if I want to add a payment flow next quarter?

These are the questions engineers think about every day. Writing code is the easy part. Writing code that aligns with business goals — that's engineering.

## Is there a Better IDE than Chat?

You can probably tell where I'm going with this. Writing code used to be hard. Now it's as simple as a one-sentence, zero-context prompt. But vibing with chat isn't going to help you define the problem. For decades, software engineers have worked with requirements docs, architecture diagrams, dashboards, project management tools. Not because we love documentation — but because these tools help us organize the information better. It's how we break down problems, track decisions, and make sure nothing falls through the cracks. In my opinion, chat-based development actually makes development harder — you lose track of what's been decided, what's changed, and what still needs to happen.

<video autoplay muted loop playsinline preload="metadata" width="420" style="display:block;max-width:100%;margin-top:16px;margin-bottom:16px;">
	<source src="/img/bad-ui-battle.mp4" type="video/mp4" />
	Your browser does not support the video tag.
</video>

I know, I know — everything is a chat now because ChatGPT literally has "chat" in the name. But chat interface is working AGAINST you when it comes to complex problem solving. Imagine ordering groceries through a chat...

"I need eggs," 

"Oh wait, also milk,"

"Actually make the eggs a dozen," 

"Wait, did I add butter?" 

Or, you could browse a list, see everything, adjust quantities, and check out. Which way do you think you're more likely to get what you need?

## Build Software like a Normal Person

I'm not saying you shouldn't use LLMs to generate code. You absolutely should. I even don't like writing code myself. But chat is about the worst interface I could think of to write code with.

Instead of chat, use the LLM for what it's good at — generating structured artifacts. Requirements docs. Architecture diagrams. API designs. Database schemas. Use the artifacts as the abstraction between your problem and the code.


## The 80% Problem

For years, business owners are stuck with two bad options. Pay for SaaS that does 80% of what they need and never gets the last 20%. Or pay an agency tens of thousands of dollars for a custom app they can never update.

Vibe coding changes the equation entirely. The gym owner who needs a booking system that matches their weird scheduling rules. The property manager who needs a tenant portal that works with their actual workflow. The clinic that needs an intake form wired to their specific stack. For the first time, these people can actually get the app they need — not the app some SaaS company decided to build for everyone.

## More to Come ...

But exactly what artifacts to generate? How to organize the information to help you define the problem and solutions when it comes to building an app? Great questions. I got you.

I'm building a system where structured artifacts — not chat — are the interface to code generation. You define your problem through requirements, designs, and specs. The system generates and organizes them with you. Then the code gets written from those artifacts, not from a loose conversation. The artifacts are the abstraction layer between what you need and what gets built.

Stay tuned.
