from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)