---
layout: post
title:  "03-You've fit the model, what's next?"
excerpt: "Before we start, repeat after me. 'There is no single evaluation metric that is 'on the money' for any classification problem, or any other problem.'"
date:   2020-04-21 22:55:00
tags: [classification, model evaluation, Data Science]
categories: [Statistics]
image:
  feature:
---
From there you commit to your github repository, update whatever kaggle notebook you were on, close your computer, pat yourself on the back, and call it a productive day! .....Well, I wish data science was that straightforward. However, **there is a question that you need to ask yourself though. Is this model any good?**

Welcome to my new blog series of “You’ve fit the model, what’s next?” by Andrew Berry. In this post we will be going through a quick overview of some common classification evaluation metrics to help us determine how well our model performed. For simplicity’s sake, let’s imagine we’re dealing with a binary classification problem, such as fraud detection and food recall.

Before we start, repeat after me. **"There is no single evaluation metric that is "on the money" for any classification problem, or any other problem."**

Great, now repeat this mantra whenever you’re are evaluating your models.

Okay great, let's start with the simplest metric available being "**accuracy**". It’s popular and very easy to measure. But it’s too simplistic, and it doesn't really tell us the full picture. Now repeat my mantra again. **“There is no single evaluation metric that is “on the money” for any classification problem, or any other problem."**

Let me give you an example, say you have dataset comprising 1000 data points, with 950 being class 0, and 50 being class 1. Assuming class 0 represents correctly printed books, and class 1 represents books that are faulty, let’s assume the faultiness was that they printed it upside down. We create a simple model and behold our accuracy is 95%.

With little knowledge of the context, we might tell ourselves “damn, this is a great model! Let’s launch this thing into production!” However, because of this highly imbalanced dataset, our model may have just classified everything as class 0, mis-classifying our faulty book, thus our accuracy is 95% having all our class 0 correctly classified. We can quickly check if this is true by calculating the “**null accuracy**” which refers to the accuracy that is achieved by always predicting the most frequent class.

Now repeat after me. **"There is no single evaluation metric that is "on the money" for any classification problem, or any other problem."**

To dig into our accuracy score and break it down further, one tool that many data scientist like to use is the **confusion matrix.** It’s not an evaluation metric, but it does the job at highlighting the “types” of errors our classifier is making for each class.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#93a1a1;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#93a1a1;color:#002b36;background-color:#fdf6e3;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#93a1a1;color:#fdf6e3;background-color:#657b83;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky" colspan="3">Actual Values</th>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="3">Predicted Values</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">Positve</td>
    <td class="tg-0lax">Negative</td>
  </tr>
  <tr>
    <td class="tg-0pky">Positive</td>
    <td class="tg-1wig">TP</td>
    <td class="tg-1wig">FP</td>
  </tr>
  <tr>
    <td class="tg-0lax">Negative</td>
    <td class="tg-1wig">FN</td>
    <td class="tg-1wig">TN</td>
  </tr>
</table>

Let’s image our predicted values as our model’s actual prediction performance, with the top row having our model predicting that data point as positive, and bottom row having our model predicting that data point as negative.

- **True Positive (TP)** refers to predicting a positive class as positive. Meaning it correctly classified it.
- **False Positive( FP)** refers to predicting a negative class as positive. Meaning it failed to classify it properly.
- **False negative (FN)** refers to predicting a positive class as negative. Meaning it failed to classify it properly.
- **True Negative (TN)** refers to predicting the negative class as negative. Meaning it correctly classified it.

Going back to our faulty book example, our model confusion matrix would have looked like this.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#93a1a1;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#93a1a1;color:#002b36;background-color:#fdf6e3;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#93a1a1;color:#fdf6e3;background-color:#657b83;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky" colspan="3">Actual Values</th>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="3">Predicted Values</td>
    <td class="tg-0pky"></td>
    <td class="tg-0lax">Positve</td>
    <td class="tg-0lax">Negative</td>
  </tr>
  <tr>
    <td class="tg-0pky">Positive</td>
    <td class="tg-1wig">0-TP</td>
    <td class="tg-1wig">0-FP</td>
  </tr>
  <tr>
    <td class="tg-0lax">Negative</td>
    <td class="tg-1wig">50-FN</td>
    <td class="tg-1wig">950-TN</td>
  </tr>
</table>

With our original model's accuracy being 95%. We can clearly see that accuracy itself does not paint the full picture and that we should be skeptical of the number.

From our confusion matrix, we can start calculating further metrics, such as **precision and recall.**

**Precision** measures the accuracy of a predicted positive class.

![precision](/img/equations/precision.png)

**Recall** measures how well the model is able to predict a positive class. Also known as **sensitivity** in the statistics world. Recall is more or less used more in the machine learning community and by data scientist like me!

![recall](/img/equations/recall.png)

**Specificity** measures how well the model is able to predict a negative outcome:

![specificity](/img/equations/specificity.png)

It’s tempting to say let’s optimize for precision and recall (good precision and high recall), however there is a tradeoff. Increasing precision decreases recall, and vice versa. I won’t get into why here, but you can look it up [here](https://www.wikiwand.com/en/Precision_and_recall).

However, there is a metric we could use to evaluate our classification while taking into account precision and recall. Which will be discussed below. But first...repeat after me. **"There is no single evaluation metric that is "on the money" for any classification problem, or any other problem."** (I promise I will only make you repeat it one more time.)  

For highly imbalanced data like our faulty book example, there is a great metric that I like to use is the **F1-Score**. Since it takes into account both the precision and recall and combines it into a single score. The perfect F1 score is a score than lands between 0 and 1, with 1 indicating a perfect classifier.

![f1score](/img/equations/f1score.png)

Finally, there is another important evaluation tool that I want to bring up. It being the "**Receiver Operating Characteristics**" commonly referred to as the **ROC curve**. The ROC curve plots the recall on the y-axis and the specificity on the x-axis. It does a good job at helping you choose a threshold that balances the sensitivity and specificity. I will discuss how to interpret the ROC curve in a later blog post, as it is a useful plot that requires some further detail to fully grasp the usefulness of it.

From the ROC curve, we’re able to calculate the **area under the curve**, commonly known as the **AUC**. The AUC is a useful metric as it is a single score that essentially tells us how well the classifier performed. An AUC of 1 indicates a perfect classifier, it can correctly predict all the class 1 correctly and does not mis-classify any 0s and 1s. AUC of 0 shows that it is a horrible classifier, and most likely in practice you’ll find a number somewhere between 0 and 1. AUC is very useful when dealing with a dataset with high class imbalance like our faulty book example.

Now repeat after me. **"There is no single evaluation metric that is “on the money” for any classification problem, or any other problem.”**
