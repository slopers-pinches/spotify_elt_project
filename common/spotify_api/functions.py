import requests
import json
import os
import base64


def get_token():

    """ 

    The get_token() function generates a bearer token when calling Spotify API Endpoint.
    No arguements are required to the get_token() function.
    In the .env file, enter or update 'client_id' and 'client_secret'.

    """

    # Calling and declaring Spotify Client ID and Secret from .env file.
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded",
    }

    grant_dict = {
        "grant_type" : "client_credentials"
    }

    result = requests.post(url, headers=headers, data=grant_dict)
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token