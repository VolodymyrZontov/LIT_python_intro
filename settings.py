import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

API_URL = "https://api.nasa.gov/planetary/apod"

REGEX_FILENAME = os.getenv("REGEX_FILENAME")
REGEX_PAGE_INFO = os.getenv("REGEX_PAGE_INFO")
REGEX_PAGE_DATA = os.getenv("REGEX_PAGE_DATA")