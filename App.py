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

YOUR_CHANNEL_ACCESS_TOKEN = 'BgL5Q+YnHFN+VtkGDYKrTSYyoDpkUVcPmUlG6bWCYmnESi4lgNYnHjTd2qzeOqrpsjJOKi8QZaSQa/LQcf4Cxd8wcQua8LOEr6fojr8ceIm3Y6naGj3331BnbpFmQwGsooT7xiHfNWVovEVJEkDRBgdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = '5521bb2a895206ab596a0334730d12a6'

#環境変数取得
# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

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

  # ReqContent = request.get_json()
  # ReqText = ReqContent['events'][0]['message']['text']
  # handle webhook body
  try:
    print("api呼び出し")
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)
  return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  if createCard(event.message.text):
    ReplyText = "カードを作成しました。"
  else:
    ReplyText = "カード作成に失敗しました。"
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=ReplyText))


if __name__ == "__main__":
#    app.run()
  port = int(os.getenv("PORT", 5000))
  app.run(host="0.0.0.0", port=port)