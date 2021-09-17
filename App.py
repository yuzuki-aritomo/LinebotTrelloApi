from flask import Flask, request, abort
from linebot import (
  LineBotApi, WebhookHandler
)
from linebot.exceptions import (
  InvalidSignatureError
)
from linebot.models import (
  MessageEvent, TextMessage, TextSendMessage, messages,
)
import os
from Api import createCard
import json
app = Flask(__name__)


#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/", methods=['GET'])
def init():
  return "hello world"

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  if createCard(event.message.text):
    ReplyText = 'Success Created Card "' + event.message.text + '"'
  else:
    ReplyText = 'Failed Create Card "' + event.message.text + '"'
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=ReplyText))


if __name__ == "__main__":
#    app.run()
  port = int(os.getenv("PORT", 5000))
  app.run(host="0.0.0.0", port=port)