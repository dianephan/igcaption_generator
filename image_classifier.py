import os
from dotenv import load_dotenv
from clarifai.rest import ClarifaiApp

load_dotenv()
CLARIFAI_API_KEY = os.environ.get('CLARIFAI_API_KEY')
app = ClarifaiApp(api_key=CLARIFAI_API_KEY)

def get_picture_tags(image_url):
    response_data = app.tag_urls([image_url])
    relevant_tags = {}   #dictionary data structure for faster lookup time 
    for concept in response_data['outputs'][0]['data']['concepts']:
        relevant_tags[concept['name']] = 1
    return relevant_tags.keys()
