import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from image_classifier import get_picture_tags
from caption_generator import generate_caption

app = Flask(__name__)
client = Client()

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/webhook', methods=['POST'])
def reply():
    sender = request.form.get('From')
    media_msg = request.form.get('NumMedia')  
    message = request.form.get('Body').lower()
    if media_msg == '1':
        pic_url = request.form.get('MediaUrl0')  
        relevant_tags = get_picture_tags(pic_url)
        print("The tags for your picture are : ", relevant_tags)
        # call openai gpt3
        caption = generate_caption(relevant_tags)
        print(caption)
        return respond(caption)
    else:
        return respond(f'Please send in a picture.')