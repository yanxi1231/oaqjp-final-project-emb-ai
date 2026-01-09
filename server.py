"""
server.py

Flask application for emotion detection using Watson NLP.
Provides endpoints for home page and emotion analysis.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    """
    Render the home page of the application.

    Returns:
        str: Rendered HTML from index.html template
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Analyze the text provided by the user for emotions.

    Retrieves user input from the query parameter 'textToAnalyze',
    calls the emotion_detector function, and returns a formatted
    response including emotion scores and dominant emotion.

    Returns:
        str: Formatted response with emotion scores.
             If input is blank, returns error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function
    result = emotion_detector(text_to_analyze)

    # Error handling for blank input
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Extract values
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    # Format the response exactly as required
    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response

if __name__ == "__main__":
    """Run the Flask application on localhost:5000"""
    app.run(host="0.0.0.0", port=5001)
