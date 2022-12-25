# import flask related
from flask import Flask, request, abort, url_for
# from urllib.parse import parse_qsl, parse_qs
import random
from linebot.models import events
from lineBot_api import *

from functionalities import *


# create flask server
app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print('receive msg')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'



@handler.add(FollowEvent)
def handle(event):
    '''
        處理加好友事件
    '''
    userName = line_bot_api.get_profile(event.source.user_id).display_name
    message = f"{userName}，嗨 !\n本服務是用來辨識明星的。\n請傳送明星的圖片給我 !!!"
    line_bot_api.reply_message(event.reply_token, TextMessage(text=message))


@handler.add(MessageEvent)
def handle_message(event):
    '''
        處理訊息事件
    '''
    print(celebName)
    if event.message.type == 'image':
        with open('.\\static\\image.png', 'wb') as f:
            f.write(line_bot_api.get_message_content(event.message.id).content)
        face_result(event)
    if event.message.type == 'text':
        command = event.message.text
        if command == basicStr:
            basic(event)
        elif command == filmStr:
            film(event)
        elif command == socialStr:
            social(event)
        elif command == newsStr:
            news(event)
        else:
            sorry(event)


# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
