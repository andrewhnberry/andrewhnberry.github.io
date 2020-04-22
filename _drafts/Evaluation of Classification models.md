From there you commit to your github repository, update whatever kaggle notebook you were on, close your computer, pat yourself on the back, and call it a productive day! Well, I wish data science was that straightforward. However, there is a question that you need to ask yourself though. Is this model any good? 

Welcome to my new blog series of “You’ve fit the model, what’s next?” by Andrew Berry. In this post we will be going through a quick overview of some common classification evaluation metrics to help us determine how well our model performed. For simplicity’s sake, let’s imagine we’re dealing with a binary classification problem, such as fraud detection and food recall.

Before we start, repeat after me. "There is no single evaluation metric that is “on the money” for any classification problem, or any other problem.”

Great, now repeat this mantra whenever you’re are evaluating your models.

Okay great, let’s start with the simplist metric available being “accuracy”. It’s popular and very easy to measure. But it’s too simplistic, and it doesn really tell us the full picture. Now repeat my mantra again. “There is no single evaluation metric that is “on the money” for any classification problem, or any other problem."

Let me give you an example, say you have dataset comprising 1000 data points, with 950 being class 0, and 50 being class 1. Assuming class 0 represents correctly printed books, and class 1 represents books that are faulty, let’s assume the faultiness was that they printed it upside down. We create a simple model and behold our accuracy is 95%. 

With little knowledge of the context, we might tell ourselves “damn, this is a great model! Let’s launch this thing into production!” However, because of this highly imbalanced dataset, our model may have just classified everything as class 0, mis-classifying our faulty book, thus our accuracy is 95% having all our class 0 correctly classified. We can quickly check if this is true by calculating the “null accuracy” which refers to the accuracy that is achieved by always predicting the most frequent class.

Now repeat after me. "There is no single evaluation metric that is “on the money” for any classification problem, or any other problem.”

To dig into our accuracy score and break it down further, one tool that many data scientist like to use is the confusion matrix. It’s not an evaluation metric, but it does the job at highlighting the “types” of errors our classifier is making for each class.
Let’s image our predicted values as our model’s actual prediction performance, with the top row having our model predicting that data point as positive, and bottom row having our model predicting that data point as negative. 
Going back to our faulty book example, our model confusion matrix would have looked like this.
With our original model’s accuracy being 95%. We can clearly see that accuracy itself does not paint the full picture and that we should be skeptical of the number. 
From our confusion matrix, we can start calculating further metrics, such as precision and recall. 
Precision measures the accuracy of a predicted positive class.
Recall measures how well the model is able to predict a positive class. Also known as sensitivity in the statistics world. Recall is more or less used more in the machine learning community and by data scientist like me! 
Specificity measures how well the model is able to predict a negative outcome:
It’s tempting to say let’s optimize for precision and recall (good precision and high recall), however there is a tradeoff. Increasing precision decreases recall, and vice versa. I won’t get into why here, but you can look it up here.

However, there is a metric we could use to evaluate our classification while taking into account precision and recall. Which will be discussed below. But first...repeat after me. "There is no single evaluation metric that is “on the money” for any classification problem, or any other problem.” (I promise I will only make you repeat it one more time.)  

For highly imbalanced data like our faulty book example, there is a great metric that I like to use is the F1-Score. Since it takes into account both the precision and recall and combines it into a single score. The perfect F1 score is a score than lands between 0 and 1, with 1 indicating a perfect classifier.
Finally, there is another important evaluation tool that I want to bring up. It being the “Receiver Operating Characteristics” commonly referred to as the ROC curve. The ROC curve plots the recall on the y-axis and the specificity on the x-axis. It does a good job at helping you choose a threshold that balances the sensitivity and specificity. I will discuss how to interpret the ROC curve in a later blog post, as it is a useful plot that requires some further detail to fully grasp the usefulness of it. 

From the ROC curve, we’re able to calculate the area under the curve, commonly known as the AUC. The AUC is a useful metric as it is a single score that essentially tells us how well the classifier performed. An AUC of 1 indicates a perfect classifier, it can correctly predict all the class 1 correctly and does not mis-classify any 0s and 1s. AUC of 0 shows that it is a horrible classifier, and most likely in practice you’ll find a number somewhere between 0 and 1. AUC is very useful when dealing with a dataset with high class imbalance like our faulty book example. 
Now repeat after me. "There is no single evaluation metric that is “on the money” for any classification problem, or any other problem.”