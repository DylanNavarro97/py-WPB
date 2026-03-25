from flask import Flask, request
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return {"mensaje": "Servidor Flask funcionando 🚀"}

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    env_verify_token = os.getenv("WP_KEY")

    if token ==  env_verify_token:
        return challenge, 200
    else:
        return "error", 403

    

if __name__ == "__main__":
    app.run(debug=True)

