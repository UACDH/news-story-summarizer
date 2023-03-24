##
# Author: Bahaa Abdulraheem
# Description: This script is a cli tool that allows you to query newsapi
#               for the top news article and use OpenAI's GPT-3 to summarize it.
##

import typer
import openai
from rich.console import Console
from news_engine import NewsEngine, NewsArticle
from summarize_engine import SummarizeEngine

app = typer.Typer()
console = Console(width=80)

news = NewsEngine()
summarize_engine = SummarizeEngine()

@app.command("summarize")
def summarize(query: str=None, show_usage: bool=False, url=None, verbose: bool=False):
    """Summarize the top news article for a given query"""
    article = None
    if query:
        article = news.get_top_headline(query=query)
    elif url:
        article = news.get_article_from_url(url)
    else:
        article = news.get_top_headline()

    if not article:
        raise Exception("Error: Got empty article from news engine!")

    console.print(f"Author(s): {article.get_author()}", highlight=False)
    console.print(f"Article: {article.get_title()}\n", highlight=False)
    
    # Summarize the article using OpenAI's GPT-3
    prompt = f"{article.get_title()}\n{article.get_description()}\n{article.get_content()}\nSummarize the above in at most 5 sentences:"

    summary, tokens_used = None, None
    with console.status("Summarizing...", spinner="bouncingBar"):
        summary, tokens_used = summarize_engine.summarize(article)
        
    usage_string = (f"(used {tokens_used} tokens)" if show_usage else "")

    console.print(f"Summary: {usage_string}\n")
    console.print(f"{summary}\n", highlight=False)
    console.print(f"Source: {article.get_url()}")

if __name__ == '__main__':
    app()
