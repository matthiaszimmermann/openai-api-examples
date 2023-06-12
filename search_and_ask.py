import openai  # for calling the OpenAI API
import pandas as pd
import sys

FILE1_NAME = './data/wikipedia_curling.txt'
FILE2_NAME = './data/wikipedia_cop27.shortened.txt'
QUIT_WORD = 'quit'

EMBEDDING_MODEL = "text-embedding-ada-002"

GPT_35 = "gpt-3.5-turbo"
# apply here for access to gpt-4 https://openai.com/waitlist/gpt-4-api
GPT_40 = "gpt-4"
GPT_MODEL = GPT_35

QUERY_PREFIX = """
Use the below article to answer the subsequent question marked "Question:". 
If the answer cannot be found, write "I don't know."

Article:
"""

def read_file(filename:str) -> str:
    with open(filename, 'r') as file:
        lines = file.readlines()

    return '\n'.join(lines)


def get_embeddings(articles: list[str]) -> list[dict]:
    embeddings = []

    # call embedding api
    response = openai.Embedding.create(model=EMBEDDING_MODEL, input=articles)    

    # build result list including both articles and corresponding embeddings
    for i, item in enumerate(response["data"]):
        assert i == item['index'] # double check embeddings are in same order as input
        embeddings.append({
            'article': articles[i],
            'embedding': item['embedding']
        })

    return embeddings


def create_query(article:str, user_question:str) -> str:
    return QUERY_PREFIX + article + "\nQuestion: " + user_question


def get_answer(article:str, user_question:str) -> str:
    user_query = create_query(article, user_question)

    response = openai.ChatCompletion.create(
        messages = [
            {'role': 'system', 'content': 'You answer questions about the provided article.'},
            {'role': 'user', 'content': user_query },
        ],
        model = GPT_MODEL,
        temperature = 0,
    )

    return response['choices'][0]['message']['content']


def main():
    # check command line
    if len(sys.argv) > 1:
        print("usage: {}".format(sys.argv[0]))
        sys.exit(1)

    # load articles
    articles = []
    articles.append(read_file(FILE1_NAME))
    articles.append(read_file(FILE2_NAME))

    # get embeddings for articles
    embeddings = get_embeddings(articles)


if __name__ == '__main__':
    main()