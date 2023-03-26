"""
This script reads from STDIN, sends related data to the OpenAI API, and prints the output.
"""

import os
import sys
from dotenv import load_dotenv


def main(args):
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    main(sys.argv[1:])
