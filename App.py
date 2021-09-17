from flask import Flask
import os
from src.TrelloApi import getCards

app = Flask(__name__)

from src import Linebot
app.register_blueprint(Linebot.app)

@app.route("/", methods=['GET'])
def init():
  a = getCards()
  return a

if __name__ == "__main__":
  port = int(os.getenv("PORT", 5000))
  app.run(host="0.0.0.0", port=port)