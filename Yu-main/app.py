from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import random



app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Oj5u1W0iXCh02EY/05XHu0SPSo9XbUH6aIak7CSPsZCK3tqPMJH2OLda5ucMIllli7vVe0L5bnItmLf34WrbH4Hkf1Db2aXuu2FDanzp3VGMtw1BO2g+5hqLE2sffbqtTqyrVdTNyLon9rWrEMP4ugdB04t89/1O/w1cDnyilFU=')
#or line_bot_api = 'Channel_token'

# Channel Secret
handler = WebhookHandler('d29ad32bdef2a6513f1ba6280e49627e')
#or handler = 'Channel_secret'

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage,message1=TextMessage)
def handle_message(event):
    get = event.message.text
    get1 = event.message1.text
#event.gessage.text接收使用者文字訊息

    if get == "求籤":
        result = random.randint(0,3)
        if result == 0:
            message = TextSendMessage(text = "大吉")
        elif result == 1:
            message = TextSendMessage(text = "吉")
        elif result == 2:
            message = TextSendMessage(text = "中")
        else:
            message = TextSendMessage(text = "凶")
    if get == "請問今年脫單機率":
        result = random.randint(0,100)
        message = TextSendMessage(text = str(result) + "%")
    if get == "0":
        message = TextSendMessage(text = "0%")
    if('水瓶座' in get1):
        message1 = ImageSendMessage(
            original_content_url = 'https://i0.wp.com/guidelinehk.com/wp-content/uploads/2021/02/age-of-aquarius-community.jpg?resize=800%2C445&ssl=1.jpg',
            preview_image_url = 'https://i0.wp.com/guidelinehk.com/wp-content/uploads/2021/02/age-of-aquarius-community.jpg?resize=800%2C445&ssl=1.jpg'
        )
    if('水瓶座' in get):
        message = TextSendMessage(text = "水瓶是一個持著瓶子在酒吧的美少年蓋尼米德，他是特洛伊的王子。\n有一天，他替父親看羊時，我在天空經過，一看到他的臉就愛上他了，因為太愛他了，我就變身成一隻老鷹擄走他到奧林匹斯山跟我一起住。")
    if('黑人問號' in get):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/zTOnfAi.jpg',
            preview_image_url = 'https://i.imgur.com/zTOnfAi.jpg'
        )
    
    if get == "hello 你好嗎":    
        message = TextSendMessage(text = "衷心感謝")
        
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
