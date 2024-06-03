import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()

def main():
    configure()
    print(os.getenv('username'))

main()