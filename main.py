#
# Author: Bahaa Abdulraheem
# Description: This script is a cli tool that allows you to query newsapi
#               for the top news article and use OpenAI's GPT-3 to summarize it.
#

import typer
import openai
import config
from newsapi import NewsApiClient

app = typer.Typer()

newsapi = NewsApiClient(api_key=config.newsapi_key)
openai.api_key = config.openai_key

@app.command("summarize")
def summarize(query: str=None):
    """Summarize the top news article for a given query"""
    # Retrieve the top news article from NewsAPI
    headlines = None
    if query:
        typer.echo(f"Here's some top news about {query}:")
        headlines = newsapi.get_everything(q=query, language='en', sort_by='popularity', page_size=1)
    else:
        typer.echo("Here's some top news for you:")
        headlines = newsapi.get_top_headlines(language='en', country='us', page_size=1)

    if headlines['status'] != 'ok':
        typer.echo(f"Error: {headlines['message']}")
        return
    if len(headlines['articles']) == 0:
        typer.echo("Error: No articles found")
        return
    
    article = headlines['articles'][0]

    # Summarize the article using OpenAI's GPT-3
    prompt = f"{article['title']}\n\n{article['description']}\nSummarize the above in 5 sentences:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=200,
        n=1,
        temperature=1,
    )
    # Error handling
    if response['choices'] == []:
        typer.echo("Error: OpenAI returned an empty response")
        return
    summary = response.choices[0].text.strip()

    # Print the title and summary
    typer.echo(f"Article: {article['title']}\n")
    typer.echo(f"Summary:\n{summary}\n")
    typer.echo(f"Source: {article['url']}")

if __name__ == '__main__':
    app()
