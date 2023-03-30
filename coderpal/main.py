"""
This script reads from STDIN, sends related data to the OpenAI API, and prints the output.
"""

import os
import sys
import openai
from dotenv import load_dotenv


def main(args):
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = openai_api_key

    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt="Say this is a test",
        temperature=0,
        max_tokens=7,
    )
    print(completion.choices[0])

if __name__ == "__main__":
    main(sys.argv[1:])
