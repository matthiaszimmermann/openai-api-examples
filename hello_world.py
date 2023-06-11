import openai  # for calling the OpenAI API
import sys

FILE_NAME = './data/wikipedia_curling.txt'
QUIT_WORD = 'quit'

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
    file_name = FILE_NAME

    # check command line
    if len(sys.argv) > 2:
        print("usage: {} [article-file]".format(sys.argv[0]))
        sys.exit(1)
    elif len(sys.argv) == 2:
        file_name = sys.argv[1]

    # load text of article
    article = read_file(file_name)

    # answer user questions
    while True:
        user_question = input('Ask a question about article {} (or "{}" to exit): '.format(file_name, QUIT_WORD))
        if user_question.lower() == QUIT_WORD:
            break

        answer = get_answer(article, user_question)

        print(answer)


if __name__ == '__main__':
    main()