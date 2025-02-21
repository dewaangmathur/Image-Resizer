import tweepy
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

def authenticate_twitter():
    """Authenticate with X API."""
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

def post_images(api, images):
    """Post resized images to the user's X timeline."""
    media_ids = []
    for size, image in images.items():
        image_path = f"temp_{size}.png"
        image.save(image_path)
        media = api.media_upload(image_path)
        media_ids.append(media.media_id)
    
    # Post tweet with images
    api.update_status(status="Here are my resized images! 📷", media_ids=media_ids)
    return "Images posted successfully!"
