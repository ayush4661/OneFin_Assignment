import os
import requests
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

def authenticate_with_movie_api():
    response = requests.get(
        os.environ.get("MOVIE_API_URL"),
        auth=(os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET"))
    )
    return response.json().get("data", [])
