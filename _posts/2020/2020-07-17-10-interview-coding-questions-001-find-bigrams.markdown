---
layout: "post"
title: "10-Interview Coding Questions - #001 Find Bigrams"
date: "2020-07-17 17:01"
tags:
  - Tutorials
  - Python
categories:
  - Interview
---

I've been subscribed to Interview Query's free newsletter, and quite often they would send me some coding questions that have been asked in data science interviews.

This blog series will be on those questions and my attempt to solve them.

#### Question

**Write a function that can take a string and return a list of bigrams.**

**Example:**
```python
sentence = """
Have free hours and love children?
Drive kids to school, soccer practice
and other activities.
"""

output = [('have', 'free'),
 ('free', 'hours'),
 ('hours', 'and'),
 ('and', 'love'),
 ('love', 'children?'),
 ('children?', 'drive'),
 ('drive', 'kids'),
 ('kids', 'to'),
 ('to', 'school,'),
 ('school,', 'soccer'),
 ('soccer', 'practice'),
 ('practice', 'and'),
 ('and', 'other'),
 ('other', 'activities.')]
```

** My Solution:**

```python
import numpy as np

def return_bigrams(sentence):

    bigrams_list = []

    tokens = sentence.split(' ')

    for i in np.arange(1,len(tokens)):
        if i != (len(tokens)-1):
            bigram = (tokens[i], tokens[i+1])
            bigrams_list.append(bigram)

    return bigrams_list
```
