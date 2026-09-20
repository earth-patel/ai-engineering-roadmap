import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY")

print(api_key)  # This will print the value of OPENAI_API_KEY from the .env file