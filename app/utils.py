import requests 
from dotenv import load_dotenv
load_dotenv(override=True)
import pyshorteners

class urlShortener(): 
    def __init__(self): 
        self.url_mapping = {} 

    def convert_long_to_short_url(self, long_url):
        s = pyshorteners.Shortener()
        s.timeout = 10
        try:
            short_url = s.tinyurl.short(long_url)
            return short_url
        except requests.exceptions.ReadTimeout:
            return "Error: The request timed out. Please try again later."
        except Exception as e:
            return "An error occurred. Please check your original URLs and try again later."
        
    def get_original_url(self, short_url):
        return self.url_mapping.get(short_url)