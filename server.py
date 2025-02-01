"""
Flask Web Server for Emotion Detection Application
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page of the Emotion Detection application.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Processes the input text, runs emotion detection, and returns the response.
    Handles errors when input is missing or invalid.

    Returns:
        JSON response containing the detected emotions or an error message.
    """
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text_to_analyze = data['text']
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    formatted_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return jsonify({"response": formatted_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
