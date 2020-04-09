---
layout: post
title:  "01-The Easy Way to Web Scrape Articles Online"
excerpt: "I will show you how to web scrape articles online and put it into a DataFrame in under 10 minutes! We'll be using the newspaper3k plugin to and some python to achieve this."
date:   2020-04-07 21:06:00
tags: [web scraping, python, tutorials]
categories: [web scraping]
image:
  feature: /img/code/01_code.png
---
# The simplest way to web scrape news articles online!

About a year ago, my final capstone project required me to **web scrape a bunch of news articles online**. Knowing my lazy self, I wanted to figure out the easiest way to achieve this task. There are tonnes of python web scraping plugins out there that could have helped me do the job, a popular one being [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). It's a great plugin, however I did not want to get into the nitty gritty of understanding the unique html structures of each online news sites.

![Web Scraping](/img/code/01_code.png)

Through much googling (which is an important skill to know if you're a developer), I did find a **simple solution to my problems**.  I found [Newspaper3k](https://newspaper.readthedocs.io/en/latest/)!

Oh, did it save me so much time when parsing through an online news site to scrape that article. I'll show you!
## How to use Newspaper3k to Scrape Online Articles

First, we need to install the python plugin on your terminal. *Disclaimer: I'm using OSX*

*Pro tip: Do create another environment, it's considered best practice.*

    $ pip install newspaper3k

### The Basics
{% highlight python %}
    import newspaper
    from newspaper import Article

    #The Basics of downloading the article to memory
    article = Article("link to your article")
    article.download()
    article.parse()
    article.nlp()

    #To print out the full text
    print(article.text)
    >>> #the text of the article should be printed out

    #To print out the list of authors
    article.authors
    >>> ['author_1','author_2']

    #To print out the list of keywords (thanks to the built in NLP functionalities)
    >>> ['keywords_1','keywords_2',.....etc

    #To print out a summary of the text
    print(article.summary)
    >>> #Summary of the text

    #Other functions to gather the other bits of useful data in an article
    article.title #Gives the title
    article.top_image #Gives the link to the banner image, main image with the article
    article.images #Provides a set of image links that could be saved and downloaded
{% endhighlight %}
### Advanced: Downloading multiple articles from one news site.

When I was scraping these articles, I wanted to scrape a bunch of articles from one news site and put everything in a pandas DataFrame so that I could export data out to a csv file. Sounds like a simple task right? You betcha!
{% highlight python %}
    import newspaper
    from newspaper import Article
    from newspaper import Source
    import pandas as pd

    #Lets say we wanted to download articles from GameSpot
    gamespot = newspaper.build('https://www.gamespot.com/news/', memoize_articles = False)
    # I set memoize_articles to False, because I don't want it to cache and save
    # articles run after run. Fresh run, every time essentially

    final_df = pd.DataFrame()

    for each_article in gamespot.articles:

    		each_article.download()
    		each_article.parse()
    		each_article.nlp()

    		temp_df = pd.DataFrame(columns = ['Title', 'Authors',
                                          'Text','Summary',
                                          'published_date','Source'])

        temp_df['Authors'] = each_article.authors
        temp_df['Title'] = each_article.title
        temp_df['Text'] = each_article.text
        temp_df['Summary'] = each_article.summary
        temp_df['published_date'] = each_article.publish_date
        temp_df['Source'] = each_article.source_url

        final_df = final_df.append(temp_df, ignore_index = True)

    #From here you can export this
    final_df.to_csv(my_scraped_articles.csv)
{% endhighlight %}
....and there you go! That's is how you scrape a bunch of articles easily. With the code above, you could implement a for loop to loop over a bunch of newspaper sources. Creating a massive final data-frame, that you could export and then play around with.

### Enthusiast: Multithreading Web Scraping

However, my proposed solution above could be a bit slow for some, as it downloads each article one after another. If you have many news sources, this could be a bit time consuming however, lets figure out a way to speed this all up. We can do this with a little help from [multithreading](https://realpython.com/intro-to-python-threading/) technologies.
{% highlight python %}
    import newspaper
    from newspaper import Article
    from newspaper import Source
    from newspaper import news_pool
    import pandas as pd

    gamespot = newspaper.build('https://www.gamespot.com/news/', memoize_articles=False)
    bbc = newspaper.build("https://www.bbc.com/news", memoize_articles=False)
    papers = [gamespot, bbc]
    news_pool.set(papers, threads_per_source=4)
    news_pool.join()

    #Create our final dataframe
    final_df = pd.DataFrame()

    #Create a download limit per sources
    limit = 100

    for source in papers:
        #tempoary lists to store each element we want to extract
        list_title = []
        list_text = []
        list_source =[]

        count = 0

        for article_extract in source.articles:
            article_extract.parse()

            if count > limit: #Lets have a limit, so it doesnt take too long when you're
                break         #running the code.

            #appending the elements we want to extract
            list_title.append(article_extract.title)
            list_text.append(article_extract.text)
            list_source.append(article_extract.source_url)

            #Update count
            count +=1


        temp_df = pd.DataFrame({'Title': list_title, 'Text': list_text, 'Source': list_source})
        #Append to the final DataFrame
        final_df = final_df.append(temp_df, ignore_index = True)
{% endhighlight %}

I'm a person who **learns by doing**, so I suggest anyone reading this to **play with the code above.** From here, you now be able to web scape articles using the newspaper3k plugin. **Happy Web Scaping!**
