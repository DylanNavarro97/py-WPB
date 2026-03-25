from flask import Flask, request
from dotenv import load_dotenv
import os
import hmac
import hashlib

app = Flask(__name__)

env_verify_token = os.getenv("WP_HUB_TOKEN")
WP_KEY = os.getenv("WP_KEY")

@app.route("/", methods=["GET"])
def home():
    return {"mensaje": "Servidor Flask funcionando 🚀"}

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    

    if token == env_verify_token:
        return challenge, 200
    else:
        return "error", 403


@app.route("/webhook", methods=["POST"])
def load_webhook():
    signature = request.headers.get("X-Hub-Signature-256")

    body = request.data

    # expected_signature = "sha256=" + hmac.new(
    #     WP_KEY.encode(),
    #     body,
    #     hashlib.sha256
    # ).hexdigest()

    # if signature != expected_signature:
    #     return "firma inválida", 403
    
    data = request.json()
    print(data)

    
        

if __name__ == "__main__":
    app.run(debug=True)

