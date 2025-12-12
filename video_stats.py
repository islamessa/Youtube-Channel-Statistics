import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

channel_handel = "MrBeast"
load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("API_KEY")

def get_playlist_id(channel_handel, API_KEY):
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handel}&key={API_KEY}"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
        return playlist_id
    
    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    playlist_id = get_playlist_id(channel_handel, API_KEY)
    print(playlist_id)