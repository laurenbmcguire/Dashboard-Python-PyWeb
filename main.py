import openai
from pywebio import start_server
from pywebio.output import put_table
from pywebio.input import input
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def openai_response(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.3,
        max_tokens=3000,
        top_p=0.3,
        frequency_penalty=0.6,
        presence_penalty=0.0
    )
    return '{}'.format(response.choices[0].text[6:])

def main():
    while True:
        question = input('Ask something')
        put_table([
            ['Q:', question],
            ['A:', openai_response(question)]
        ])

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)