+++
title = "Jekyll to Hugo"
date = "2017-09-18T10:55:00.000Z"
tags = ["blog"]
notebook=false
+++

I use this little github site to host my jupyter notebook for machine learning projects I've done and some toy examples of doing cool visualization with d3 with notebook and python. I've been using jekyll for years but I finally got to a point where - I rarely maintain this site and because jekyll is such a flexible and extendable library, everytime I try to update something it's becoming difficult to navigate, I pulled the trigger to move to hugo recently.

Hugo turned out to be quite simple to update and flexible just enough with the functionality I am looking for. While I am mostly backend and data, I know how html/css/javascript works, at the very least, I know how to poke around, change the values and get the effect I want - it wasn't so easy for me to figure out jekyll but hugo to me is very straightforward. The migration turned out to be easy. Other than the headers on each post, I just copy and paste the notebook html files and it works - took me less than couple mins!

# Embedding jupyter notebook in post

The difficult part is the integration and css formatting. This post here [https://sharmamohit.com/post/jupyter-notebooks-in-blog/](https://sharmamohit.com/post/jupyter-notebooks-in-blog/) has been a great help. Since I am a data person, I am not a fan of duplication of fragment of code without automated pipeline - if a data is generated from source code, we should track the source code not the generated file.

As an alternative, here's what I did and what I didn't do -

## Not working

* If you google how to embed notebook in hugo, first thing you might see is to use blackfriday, my frustration being - the formatting are just not cooperating, even though it's probably the closest option to jekyll's embeding tag.

## Sort of working

I've created a custom shortcode to embed jupyter notebook html -

```
{{ $file := .Get 0 | readFile }}
{{ htmlUnescape $file | safeHTML}}
```

Easy enough, in the post markdown, just put <code>\{\{% jupyter_notebook "static/\<some notebook>.html" %}}</code>. However, there's some limit to the length of file. I happen to use go from time to time so I upped that limit and recompiled hugo to make this work.

# Publishing to github

This is pretty much the same as jekyll. I just wanted to share the easiest way I've found. The best reference I could've found is this [https://discourse.gohugo.io/t/simple-deployment-to-gh-pages/5003](https://discourse.gohugo.io/t/simple-deployment-to-gh-pages/5003). Couple tweaks I needed to make, for personal github page you need to push to `master` not `gh-page`. What worked for me is to default the branch to `develop` and then make subtree branch of public folder to `master`.

Go to the root dir and do -

```
rm -rf public
git worktree prune
git branch -D master
mkdir public
git worktree add -B master public origin/master
~/go/bin/hugo
cd public && git add --all && git commit -m "Publishing to master" && git push && cd ..
```

Check your page you should be good to go.
