"""
This module has the functions needed to interact with the AI
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    The function that detects emotion using the AI
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    body = { 
        "raw_document": { 
            "text": text_to_analyze 
        }
    }
    res = requests.post(url = url, json = body, headers = headers, timeout = 5000)
    
    keys = ('anger', 'disgust', 'fear', 'joy', 'sadness')

    for key in keys:
        



    return res.text
