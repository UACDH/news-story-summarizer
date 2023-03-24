##
# Author: Bahaa Abdulraheem
# Description: This is a module that wraps the NewsAPI API and provides a simple interface to query it,
#           get full article content, or load an article from a URL.
#         The purpose of this module is to allow multiple news sources to be used without changing the
#           core logic of the application.
##
import config
from newsapi import NewsApiClient
from newspaper import Article

newsapi = NewsApiClient(api_key=config.newsapi_key)

class NoArticlesFound(Exception):
    pass

class NewsEngine:
    def __init__(self):
        self.newsapi = newsapi

    def get_top_headline(self, query=None, country='us', language='en', _page_size=1):
        """Get the top headlines for a given query"""
        if query:
            headlines = self.newsapi.get_everything(q=query, language=language, page_size=_page_size)
        else:
            headlines = self.newsapi.get_top_headlines(language=language, country=country, page_size=_page_size)

        if headlines['status'] != 'ok':
            raise Exception(f"Error: {headlines['message']}")
        if len(headlines['articles']) == 0:
            raise NoArticlesFound("Error: No articles found")
        
        article = headlines['articles'][0]

        return NewsArticle(article['url'], article['description'])
    
    def get_article_from_url(self, url):
        """Get an article from a URL"""
        return NewsArticle(url)

class NewsArticle:
    def __init__(self, url, description=""):
        self._article = Article(url)
        self._article.download()
        self._article.parse()
        self._description = description

    def get_title(self):
        return self._article.title

    def get_author(self):
        return self._article.authors

    def get_description(self):
        return self._description

    def get_content(self):
        return self._article.text
    
    def get_url(self):
        return self._article.url
