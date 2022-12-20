from lineBot_api import *
from flask import url_for
from wiki_crawler import *

import json

# 共用變數
celebName = '無'
basicStr = '告訴我他的基本資料ㄅ'
filmStr = '真想知道他最近演了什麼...'
socialStr = '哀居拿來!'
newsStr = '八卦一下好了'

celebImageURL = ""
soup = BeautifulSoup()

# 快速回覆選單
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
    global celebName
    global celebImageURL
    global soup
    celebName = "keanu reaves"
    soup = BeautifulSoup(requests.get(
        GetWikiURL(celebName)).text, "html.parser")
    celebImageURL = GetWikiPhotoURL(soup)
    buttonsMessage = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=celebImageURL,
            title=f'我看出他是{celebName}了，哈!!',
            text='你想知道關於他的什麼事?\n或是要重新傳圖片也行的!',
            actions=[
                MessageAction(
                    label='基本資料',
                    text=basicStr
                ),
                MessageAction(
                    label='最新作品',
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
    height, weight, born, nationality, spouse = "180", "61", GetBirthDay(
        soup), "台灣", "無"
    messages = []

    with open('static/basicJson.txt', 'r', encoding='UTF-8') as f:
        s = f.read()
    message = json.loads(s)

    message['hero']['url'] = celebImageURL
    message['body']['contents'][0]['text'] = celebName
    message['body']['contents'][1]['contents'][0]['contents'][1]['text'] = height
    message['body']['contents'][1]['contents'][1]['contents'][1]['text'] = weight
    message['body']['contents'][1]['contents'][2]['contents'][1]['text'] = born
    message['body']['contents'][1]['contents'][3]['contents'][1]['text'] = nationality
    message['body']['contents'][1]['contents'][4]['contents'][1]['text'] = spouse

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
    imdb.Movie.Movie
    filmURL, filmTitle, filmYear = [], [], []
    movies = GetLatestMovies(GetIMDbPersonID(celebName))
    for i in range(0, 3):
        if movies[i] == 'none': 
            filmURL.append('https://www.macmillandictionary.com/us/external/slideshow/full/Grey_full.png')
            filmTitle.append('尚無資訊')
            filmYear.append('尚未上映')
            continue
        movieStr = movies[i]['long imdb title']
        filmTitle.append(movieStr[0: movieStr.index('(') - 1])
        year = movieStr[movieStr.index('(') + 1: movieStr.index(')')]
        if year == 'None':
            filmYear.append('尚未上映')
        else: filmYear.append(year)
        movieImg = GetIMDbMovieImg(movies[i].movieID)
        if movieImg == 'no thumbnail':
            filmURL.append('https://www.macmillandictionary.com/us/external/slideshow/full/Grey_full.png')
        else: filmURL.append(movieImg)
    messages = []

    with open('static/filmJson.txt', 'r', encoding='UTF-8') as f:
        s = f.read()
    message = json.loads(s)

    message['contents'][0]['body']['contents'][0]['url'] = filmURL[0]
    message['contents'][1]['body']['contents'][0]['url'] = filmURL[1]
    message['contents'][2]['body']['contents'][0]['url'] = filmURL[2]

    message['contents'][0]['body']['contents'][1]['contents'][0]['contents'][0]['text'] = filmTitle[0]
    message['contents'][1]['body']['contents'][1]['contents'][0]['contents'][0]['text'] = filmTitle[1]
    message['contents'][2]['body']['contents'][1]['contents'][0]['contents'][0]['text'] = filmTitle[2]

    message['contents'][0]['body']['contents'][1]['contents'][1]['contents'][0]['text'] = filmYear[0]
    message['contents'][1]['body']['contents'][1]['contents'][1]['contents'][0]['text'] = filmYear[1]
    message['contents'][2]['body']['contents'][1]['contents'][1]['contents'][0]['text'] = filmYear[2]

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
    messages = []

    image_carousel_template_message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyEIbO969AFYuv4KPFhH_74lDZu8aYQtKLjg&usqp=CAU',
                    action=URIAction(
                        label='facebook',
                        uri='https://www.google.com/search?q=facebook+icon&rlz=1C1GCEA_enTW955TW955&sxsrf=ALiCzsbNQO_GfzL6uKttyikKu_QY2H4seg:1671524651289&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiW6crI4of8AhUHSPUHHceAA9EQ_AUoAXoECAEQAw&biw=1638&bih=838&dpr=1.56'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://cdn-icons-png.flaticon.com/512/124/124021.png',
                    action=URIAction(
                        label='twitter',
                        uri='https://www.google.com/search?q=facebook+icon&rlz=1C1GCEA_enTW955TW955&sxsrf=ALiCzsbNQO_GfzL6uKttyikKu_QY2H4seg:1671524651289&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiW6crI4of8AhUHSPUHHceAA9EQ_AUoAXoECAEQAw&biw=1638&bih=838&dpr=1.56'
                    )
                ),
                ImageCarouselColumn(
                    image_url=url_for('static', filename='ig.png', _scheme='https'),
                    action=URIAction(
                        label='instagram',
                        uri='https://www.google.com/search?q=facebook+icon&rlz=1C1GCEA_enTW955TW955&sxsrf=ALiCzsbNQO_GfzL6uKttyikKu_QY2H4seg:1671524651289&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiW6crI4of8AhUHSPUHHceAA9EQ_AUoAXoECAEQAw&biw=1638&bih=838&dpr=1.56'
                    )
                )
            ]
        )
    )
    messages.extend([image_carousel_template_message, quickReplyMessage])
    line_bot_api.reply_message(event.reply_token, messages)


def news(event):
    '''
        傳送最近新聞訊息
    '''
    messages=[]
    
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            title='最近新聞',
            text='來看看有什麼新聞...',
            actions=[
                URIAction(
                label='查詢官網',
                uri='https://www.ncu.edu.tw/'
                ),
                URIAction(
                label='查詢官網',
                uri='https://www.ncu.edu.tw/'
                ),
                URIAction(
                label='查詢官網',
                uri='https://www.ncu.edu.tw/'
                ),
                URIAction(
                label='查詢官網',
                uri='https://www.ncu.edu.tw/'
                )
            ]
        )
    )

    messages.extend([buttons_template_message, quickReplyMessage])
    line_bot_api.reply_message(event.reply_token, messages)


def sorry(event):
    '''
        傳送抱歉訊息
    '''
    messages=[]
    if celebName != '無':
        textMessage=TextMessage(text='我聽不懂，再說一次啦')
        messages.append(textMessage)
        messages.append(quickReplyMessage)
        line_bot_api.reply_message(event.reply_token, messages)
    else:
        line_bot_api.reply_message(event.reply_token, TextMessage(text='請傳送圖片歐'))
