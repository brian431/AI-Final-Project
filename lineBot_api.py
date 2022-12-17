from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

line_bot_api = LineBotApi('CPjCoPUgV7Z1iS+EyPQhTiKHL13Unq/vSf3s3AflAoPsjzSFaXZOE5C4IQhNJaF7MDKLEs3modBk9k3rpWQjyMRvmCQaNB+C8wePLDhe4PETQe4YWdVTilMlN60NHKhXL7u1hWoxx1Y1vI7BG4yW6AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b6aacdfb9993ddaf7de28073d558ab1a')