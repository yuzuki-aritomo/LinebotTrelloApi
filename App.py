from flask import Flask
import os

app = Flask(__name__)

from src import Linebot
app.register_blueprint(Linebot.app)

@app.route("/", methods=['GET'])
def init():
  return "hello world"

if __name__ == "__main__":
  port = int(os.getenv("PORT", 5000))
  app.run(host="0.0.0.0", port=port)