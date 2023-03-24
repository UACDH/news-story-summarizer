import config
import openai
from news_engine import NewsArticle

openai.api_key = config.openai_key

class SummarizeEngine():
    def __init__(self):
        self.openai = openai

    def summarize(self, article: NewsArticle):
        """Summarize the top news article for a given query"""  
        if (not article or not article.get_content()):
            raise Exception("Error: Article is empty.")
    
        # Summarize the article using OpenAI's GPT-3
        prompt = f"{article.get_title()}\n{article.get_description()}\n{article.get_content()}\nSummarize the above in at most 5 sentences:"

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=200,
            n=1,
            temperature=1,
        )

        if response['choices'] == []:
            raise Exception("OpenAI returned an empty response!")

        summary = response['choices'][0].text.strip()
        tokens_used = response['usage']['total_tokens']

        return summary, tokens_used
        