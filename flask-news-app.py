from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def home():
    news_api = NewsApiClient(api_key="b9979723e9bf41259ad5aa5750a59e8e")
    top_headlines = news_api.get_top_headlines(sources="al-jazeera-english")

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []

    for article in range(len(articles)):
        my_article = articles[article]

        news.append(my_article['title'])
        desc.append(my_article['description'])
        img.append(my_article['urlToImage'])

    my_list = zip(news, desc, img)

    return render_template('base.html', context=my_list)


@app.route('/bbc')
def bbc():
    news_api = NewsApiClient(api_key="b9979723e9bf41259ad5aa5750a59e8e")
    top_headlines = news_api.get_top_headlines(sources="bbc-news")

    articles = top_headlines['articles']

    desc = []
    news = []
    img = []

    for article in range(len(articles)):
        my_article = articles[article]

        news.append(my_article['title'])
        desc.append(my_article['description'])
        img.append(my_article['urlToImage'])

    my_list = zip(news, desc, img)

    return render_template('bbc.html', context=my_list)


if __name__ == "__main__":
    app.run(debug=True)
