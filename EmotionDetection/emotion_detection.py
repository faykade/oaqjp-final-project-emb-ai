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
    response = requests.post(url = url, json = body, headers = headers, timeout = 5000)
    
    # tracked attributes
    keys = ('anger', 'disgust', 'fear', 'joy', 'sadness')
    # store current maximum key/val
    max_val = (None, 0)
    # dict to store emotion values
    emotions = {}

    # only parse if everything is successful
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_predictions = formatted_response.get('emotionPredictions')
        if emotion_predictions and len(emotion_predictions):
            res_emotions = emotion_predictions[0].get('emotion')
            # for every tracked attribute, set a new max if necessary, and store the emotion value
            for key in keys:
                res_emotion_val = res_emotions.get(key)
                emotions[key] = res_emotion_val
                if res_emotion_val > max_val[1]:
                    max_val = (key, res_emotion_val)
    
    res = {}
    for key in keys:
        res[key] = emotions.get(key)
    res['dominant_emotion'] = max_val[0]

    return res
