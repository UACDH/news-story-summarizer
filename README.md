# NewsAPI and OpenAI's GPT-3 Summarizer

This script is a command-line tool that allows you to query NewsAPI for the top news article and use OpenAI's GPT-3 to summarize it.

## Installation

1. Clone the repository
2. If you don't have pipenv installed, install pipenv using `pip install pipenv`
3. Create a new virtual environment using `pipenv install`
4. Activate the virtual environment using `pipenv shell`
5. Install the dependencies using `pipenv install -r requirements.txt`
6. Set up your NewsAPI key by following the instructions in the [NewsAPI documentation](https://newsapi.org/docs/get-started)
7. Set up your OpenAI API key by following the instructions in the [OpenAI API documentation](https://beta.openai.com/docs/api-reference/introduction)
8. Finally, add your API keys to `config.py`. It should look like this:
```py
openai_key = "YOUR_OPENAI_KEY"
newsapi_key = "YOUR_NEWSAPI_KEY"
```

## Usage

To summarize the top news article for a given query, run:

```
python main.py --query <query>
```

To summarize an article from a specific URL, run:
```
python main.py --url <url>
```

You can also use the `--verbose` flag to get more detailed output.

## License

This project is licensed under the GNU AGPLv3 License - see the LICENSE.md file for details.
