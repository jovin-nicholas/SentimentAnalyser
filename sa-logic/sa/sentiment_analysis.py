from textblob import TextBlob
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/testHealth", methods=['GET'])
def hello():
    return "Hello from python sentiment analysis flask app!"

@app.route("/testCommsLocal", methods=['GET'])
def test_comms_local():
    response = requests.get("http://localhost:8080/testHealth")
    return response.text

@app.route("/testComms", methods=['GET'])
def test_comms():
    try:
        response = requests.get("http://localhost:8080/testHealth")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Failed to reach Java app"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/analyse/sentiment", methods=['POST'])
def analyse_sentiment():
    sentence = request.get_json()['sentence']
    polarity = TextBlob(sentence).sentences[0].polarity
    return jsonify(
        sentence=sentence,
        polarity=polarity
    )

# use + for spaces, i.e. http://localhost:5000/analyse?sentence=i+am+so+happy!
@app.route("/analyse", methods=['GET'])
def analyse_sentiment_get():
    #data = request.get_json()
    #sentence = data['sentence']
    sentence = request.args.get('sentence')
    polarity = TextBlob(sentence).sentences[0].polarity
    return str(polarity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)