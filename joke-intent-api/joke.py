"""Use an API to retrieve a joke"""

# imports
import requests
import json 
import logging 

def get_joke(request):
    """Get a joke from the api if triggered, return the plain text"""
    # see the raw request - also available in diagnostics of the Dialogflow simulator
    req = request.get_json(force=True)
    print(str(req))

    # parse the intent
    intent = req.get('queryResult').get('intent').get('displayName')

    # setup the call
    API_URL = "https://icanhazdadjoke.com/"
    HEADERS = {'Accept': 'application/json'}  # tell the api to return json, not html
    resp = requests.get(API_URL, headers=HEADERS)
    if resp.status_code == 200 and intent=='get-joke':
        joke = resp.json().get('joke')
        # https://cloud.google.com/dialogflow/es/docs/fulfillment-webhook
        joke_resp = {"fulfillmentMessages": [{"text": {"text": ["Ok, hold on.  How about this?\n\n", 
                                                                joke]}}]}
        return joke_resp
    else:
        return ("Oops, I am all out of jokes.  Sorry about that.")

