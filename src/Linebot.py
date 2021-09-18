from flask import request, abort, Blueprint
from linebot import (
  LineBotApi, WebhookHandler
)
from linebot.exceptions import (
  InvalidSignatureError
)
from linebot.models import (
  MessageEvent, TextMessage, TextSendMessage,
)
import os
from src.TrelloApi import createCard, getCards

app = Blueprint("LinebotApp", __name__, url_prefix="/linebot")

from config import LinebotConfig
YOUR_CHANNEL_ACCESS_TOKEN = LinebotConfig.YOUR_CHANNEL_ACCESS_TOKEN
YOUR_CHANNEL_SECRET = LinebotConfig.YOUR_CHANNEL_SECRET
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
  # get X-Line-Signature header value
  signature = request.headers['X-Line-Signature']
  # get request body as text
  body = request.get_data(as_text=True)
  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)
  return 'OK'

#trello cardを作成し、結果をリプライ
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  if createCard(event.message.text):
    ReplyText = '"' + event.message.text + '" Card Created'
  else:
    ReplyText = 'Failed Create Card "' + event.message.text + '"'
  # ReplyText += '\n' + getCards()
  # line_bot_api.reply_message(
  #   event.reply_token,
  #   TextSendMessage(text=ReplyText))
  Cardlist = getCards()
  line_bot_api.reply_message(
    event.reply_token,
    [TextSendMessage(text=ReplyText),TextSendMessage(text=Cardlist)]
  )

@app.route("/test", methods=["GET"])
def test():
  return "health"