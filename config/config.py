import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
