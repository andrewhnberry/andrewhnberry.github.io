---
layout: post
title:  "02-Can LDA modeling techniques and sentiment analysis be used determine media bias?"
excerpt: "I had the bold idea to perform an unsupervised machine learning method to find clusters of different topics in my corpus, to which I would then perform a sentiment analysis and subjectivity analysis to see if that would provide with any interesting insights."
date:   2020-04-14 23:34:00
tags: [nlp, python, projects, Data Science]
categories: [nlp, Data Science]
image:
  feature: #find unsplash picture to put here
---
## The Problem: Media Bias

*Link to Project: https://bit.ly/2KbunTR*

I would say I spend a fair amount of time per week reading up on global affairs. It’s an interest of mine, I think it’s important to stay up to date, and it’s a topic of conversation I have a lot with my folks. I read mainly from US centric news outlets, but I do try to diversify and read outlets based outside of the United States. Personally, I’m a big fan of The Economist and The New York Times. 

I’m well aware that different news outlets have their own agendas and point of views, some news outlets hold a high level of integrity and provide great journalism, however some news outlets may be less so. I can’t say. However, I know that there are news outlets that produce content that I completely disagree with.

An obvious example of different media biases are in political news, there are liberal voices, conservative voices, libertarian, corporate, etc. Thus this project was born, and **I wanted to figure out a way to gain some insights to the possibility of different media biases to different topics.** 

### What did I do?
First of all, let's talk a little bit about the data I used. I didn't use any datasets that were on kaggle or elsewhere. I created my little data set from scratch, from web scraping articles online. To which I wrote a [tutorial](https://andrewhnberry.github.io/articles/2020-04/The-Easy-Way-to-Web-Scrape-Articles-Online) on. Please check it out, it's a shameless plug.

After accumulating data comprising of various articles from various news outlets, I went to work. However, the data I got online was not labeled with the topics it was talking about. Sure it was possible to get the category of the article, but **I wanted the specific detailed topic for each article I scraped. For example, if *article A* discussed about the COVID-19 response in Canada, that would be a category in itself and hopefully the various news outlets had articles that covered the same topic.**

**I had the bold idea to perform an unsupervised machine learning method to find clusters of different topics in my corpus, to which I would then perform a sentiment analysis and subjectivity analysis to see if that would provide with any interesting insights.**

Essentially I needed to do Latent Dirichlet allocation Topic Modeling, which is an unsupervised clustering algorithm specifically used in natural language processing.

**Topic Modeling:** Its job is to identify topics from analyzing a collection of documents, to spot word patterns within them, and automatically cluster these patterns that best describes a set of documents.{: .notice}

### The Outcome



### Project Shortcomings


### Preview:
However, this is a general overview of my project, if you would like to get to know the nitty gritty details of my project. Please do check out my project's GitHub repository [here](https://bit.ly/2KbunTR). It's much more well documented to what I did, and I've taken the courtesy to write up some deeper analysis in the markdown cells of my Jupyter Notebooks.

If you like to check out my online dashboard of the various topics sentiment & subjectivity score. You can find my Google Data Studio Dashboard [here](https://datastudio.google.com/reporting/19ffeced-1ec5-4e9c-a722-4ea55b108ade).

### Extra Resources & References:
[![](http://img.youtube.com/vi/3mHy4OSyRf0/0.jpg)](http://www.youtube.com/watch?v=3mHy4OSyRf0 "LDA Topic Models") Great Video on LDA Topic Modeling by Andrius Knispelis.
