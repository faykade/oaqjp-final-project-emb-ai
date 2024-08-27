"""
This module is to create the server and listen for incoming requests
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def sent_emotion():
    """
    the main method to analyze emotions with incoming data
    """
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)

    if not resp.get('dominant_emotion'):
        return 'Invalid text! Please try again!'

    return f"""For the given statement, the system response is
        'anger': {resp.get('anger')}, 'disgust': {resp.get('disgust')}, 'fear': {resp.get('fear')}, 
        'joy': {resp.get('joy')} and 'sadness': {resp.get('sadness')}.  
        The dominant emotion is {resp.get('dominant_emotion')}."""

@app.route('/')
def render_home_page():
    """
    The method to render the home page when called
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
