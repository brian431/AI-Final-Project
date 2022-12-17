from lineBot_api import *
from flask import url_for
import json

#共用變數
celebName = '林柏廷'
basicStr = '告訴我他的基本資料ㄅ'
filmStr = '真想知道他演了什麼...'
socialStr = '哀居拿來!'
newsStr = '八卦一下好了'

#快速回覆選單
quickReplyMessage = TextSendMessage(
        text='你還想要知道什麼關於他的什麼嗎??',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label='基本資料', text=basicStr)
                ),
                QuickReplyButton(
                    action=MessageAction(label='出演作品', text=filmStr)
                ),
                QuickReplyButton(
                    action=MessageAction(label='社群軟體', text=socialStr)
                ),
                QuickReplyButton(
                    action=MessageAction(label='最近新聞', text=newsStr)
                )
            ]
        )
    )

def face_result(event):
    '''
        傳送辨識完成後的訊息
    '''
    print(url_for('static', filename='image.png', _scheme='https', _external=True))
    print('\n\n\n\n')
    celebName = "林柏廷"
    imageURL = "https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2022/11/25/0/19529482.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=750"
    buttonsMessage = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='image.png', _scheme='https', _external=True),
            thumbnail_image_url=imageURL,
            title=f'我看出他是{celebName}了，哈!!',
            text='你想知道關於他的什麼事?\n或是要重新傳圖片也行的!',
            actions=[
                MessageAction(
                    label='基本資料',
                    text=basicStr
                ),
                MessageAction(
                    label='出演作品',
                    text=filmStr
                ),
                MessageAction(
                    label='社群軟體',
                    text=socialStr
                ),
                MessageAction(
                    label='最近新聞',
                    text=newsStr
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttonsMessage)


def basic(event):
    '''
        傳送基本資料訊息
    '''
    height, weight, born, nationality, spouse = "180", "61", "2003/06/07", "台灣", "無" 
    image = "https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2022/11/25/0/19529482.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=750"
    messages = []

    with open('static/basicJson.txt', 'r', encoding='UTF-8') as f:
        s=f.read()
    message = json.loads(s)

    message['hero']['url'] = image
    message['body']['contents'][0]['text'] = celebName

    flexMessage = FlexSendMessage(
        alt_text='hi',
        contents=message
    )
    messages.extend([flexMessage, quickReplyMessage])
    line_bot_api.reply_message(event.reply_token, messages)


def film(event):
    '''
        傳送出演作品訊息
    '''
    message = ''
    flexMessage = FlexSendMessage(
        alt_text='hi',
        contents=message
    )
    messages.extend([flexMessage, quickReplyMessage])
    line_bot_api.reply_message(event.reply_token, messages)


def social(event):
    '''
        傳送社交軟體訊息
    '''
    message = ''
    flexMessage = FlexSendMessage(
        alt_text='hi',
        contents=message
    )
    messages.extend([flexMessage, quickReplyMessage])
    line_bot_api.reply_message(event.reply_token, messages)


def news(event):
    '''
        傳送最近新聞訊息
    '''
    message = ''
    flexMessage = FlexSendMessage(
        alt_text='hi',
        contents=message
    )
    messages.extend([flexMessage, quickReplyMessage])
    line_bot_api.reply_message(event.reply_token, messages)


def sorry(event):
    '''
        傳送抱歉訊息
    '''
    messages = []
    textMessage = TextMessage(text='我聽不懂，再說一次啦')
    messages.append(textMessage)
    messages.append(quickReplyMessage)
    line_bot_api.reply_message(event.reply_token, messages)


