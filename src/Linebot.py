from flask import Flask, request, abort, blueprints
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
from src.TrelloApi import createCard

from flask import Blueprint
app = Blueprint("LinebotApp", __name__, url_prefix="/linebot")

YOUR_CHANNEL_ACCESS_TOKEN = 'BgL5Q+YnHFN+VtkGDYKrTSYyoDpkUVcPmUlG6bWCYmnESi4lgNYnHjTd2qzeOqrpsjJOKi8QZaSQa/LQcf4Cxd8wcQua8LOEr6fojr8ceIm3Y6naGj3331BnbpFmQwGsooT7xiHfNWVovEVJEkDRBgdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = '5521bb2a895206ab596a0334730d12a6'

#環境変数取得
# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
  # get X-Line-Signature header value
  signature = request.headers['X-Line-Signature']
  # get request body as text
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)
  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)
  return 'OK'

#trello cardを作成し、結果をリプライ
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  if createCard(event.message.text):
    ReplyText = 'Success Created Card "' + event.message.text + '"'
  else:
    ReplyText = 'Failed Create Card "' + event.message.text + '"'
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=ReplyText))
