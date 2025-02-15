import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

API_URL = "https://api.nasa.gov/planetary/apod"