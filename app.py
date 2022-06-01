from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import random
Girl_Array=['/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRixPnAeQ3VIhM864e1BAACAMHqN5jR32E9GNFcsy7ETJwekOlLNn2wD1FlXA&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIfrFB9potztJVKd5yGviXZi7Wpf7lD1Ewz-dYqc_AVT_munTSrcwvCLgG6w&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDlNOhyA5nOmDwAHzKwhz2UbI2OM44oftmlOVVgT7M7vQDQpF6E_I6Wf18-U0&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5IOdCzecJhMT1sx0qzOn33cI61MSFarRwGbI15ab5D4Z_oD_U-YlCT8DV0RY&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHS6J5CfdonfZWDqi-2mO1axz_9wUrSeuf1UqYOVNFQGbj7JEEN7HyAsC0GQ&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSD510ur7mPl_E4UlKVB8ZNbXRaKO2uRoN5tQheuTNPtM9hqZdNyLuyB6-jlA&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNqLtcRI01HyBOV-8Qzi1Exa_bJ6nSJDd28-orJhFtjAy4De3KDyAKSKSgSMM&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT62aujzJG_Zw3P4Q6M90Ys_rtti1xLlQgGDo3bBz1WZf8MTmHu1cuK2b6Z_w&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIfXB7vLIQ9gb59kwzXsX7z3aRf1Ivh3OKhkKdaSgZJtIlVEL-pSprmVQ7FQ&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh2lDENjqe4allaqoUejTI9BPkMXUYlFW0NKGtK2Xif1YPlYoRqO_CqkhbHA&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAw7cKO9-_trB2y6X3bKV_dJgQtnRNWgZFwgqqbf9a3nb9Sn-NaGhfiDOVb6g&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_kNitrhJMNz13Ag0Bxmh2iWNKIxg7H3ZrGLMjSyrLSySTLf3MVKkTK7hSG6Q&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAcM0jEOgQXmHT1mHEa90jkvBNJUYfwN_L7QEt4giIHZFd7f8pRHnHjHvQzrU&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnBGPFY8w-BZ3nrYxXSojVS0Fe3B5adLCvxR7juufUpkN-YU1OMbbuZ_oH3A&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2Cm6DhfRqDKDN0dYO7dwAn-yR4ap0MdLtLGxPT_whc4xZFdrh2MQCk7Bt0kU&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW_NNsHIqtCuFWajimGOv6RJneGaRM2-8h3hgGvOd4Mmq5xsstGO4Lqu24yj4&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiwqoGycNcwxiVqzz4T4_av7k2WFmHbOkyedY6yLeCQtRsjyRj9t5gC7xLK88&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzvb4h38_iIFAzlpkLWTHAA5ia49XolyuLCTmbDsOaPk4WTVRdi2Xgi-Nphg&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrs6U8hv6X5juBN1M_SPQUXFvjlKlenI0uPJVTIQmlYH2WHD2UnqPHXeCi8-8&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXwVlPmYgDMw7t8vwf1By8MxdSHii1-UlYR3NQSWBxQL01VC2IH4wpg683TQ&s.jpg', 
            '/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRixPnAeQ3VIhM864e1BAACAMHqN5jR32E9GNFcsy7ETJwekOlLNn2wD1FlXA&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIfrFB9potztJVKd5yGviXZi7Wpf7lD1Ewz-dYqc_AVT_munTSrcwvCLgG6w&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDlNOhyA5nOmDwAHzKwhz2UbI2OM44oftmlOVVgT7M7vQDQpF6E_I6Wf18-U0&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5IOdCzecJhMT1sx0qzOn33cI61MSFarRwGbI15ab5D4Z_oD_U-YlCT8DV0RY&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHS6J5CfdonfZWDqi-2mO1axz_9wUrSeuf1UqYOVNFQGbj7JEEN7HyAsC0GQ&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSD510ur7mPl_E4UlKVB8ZNbXRaKO2uRoN5tQheuTNPtM9hqZdNyLuyB6-jlA&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNqLtcRI01HyBOV-8Qzi1Exa_bJ6nSJDd28-orJhFtjAy4De3KDyAKSKSgSMM&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT62aujzJG_Zw3P4Q6M90Ys_rtti1xLlQgGDo3bBz1WZf8MTmHu1cuK2b6Z_w&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIfXB7vLIQ9gb59kwzXsX7z3aRf1Ivh3OKhkKdaSgZJtIlVEL-pSprmVQ7FQ&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh2lDENjqe4allaqoUejTI9BPkMXUYlFW0NKGtK2Xif1YPlYoRqO_CqkhbHA&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAw7cKO9-_trB2y6X3bKV_dJgQtnRNWgZFwgqqbf9a3nb9Sn-NaGhfiDOVb6g&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_kNitrhJMNz13Ag0Bxmh2iWNKIxg7H3ZrGLMjSyrLSySTLf3MVKkTK7hSG6Q&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAcM0jEOgQXmHT1mHEa90jkvBNJUYfwN_L7QEt4giIHZFd7f8pRHnHjHvQzrU&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnBGPFY8w-BZ3nrYxXSojVS0Fe3B5adLCvxR7juufUpkN-YU1OMbbuZ_oH3A&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2Cm6DhfRqDKDN0dYO7dwAn-yR4ap0MdLtLGxPT_whc4xZFdrh2MQCk7Bt0kU&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW_NNsHIqtCuFWajimGOv6RJneGaRM2-8h3hgGvOd4Mmq5xsstGO4Lqu24yj4&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiwqoGycNcwxiVqzz4T4_av7k2WFmHbOkyedY6yLeCQtRsjyRj9t5gC7xLK88&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzvb4h38_iIFAzlpkLWTHAA5ia49XolyuLCTmbDsOaPk4WTVRdi2Xgi-Nphg&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrs6U8hv6X5juBN1M_SPQUXFvjlKlenI0uPJVTIQmlYH2WHD2UnqPHXeCi8-8&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXwVlPmYgDMw7t8vwf1By8MxdSHii1-UlYR3NQSWBxQL01VC2IH4wpg683TQ&s.jpg', 
            '/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRixPnAeQ3VIhM864e1BAACAMHqN5jR32E9GNFcsy7ETJwekOlLNn2wD1FlXA&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIfrFB9potztJVKd5yGviXZi7Wpf7lD1Ewz-dYqc_AVT_munTSrcwvCLgG6w&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDlNOhyA5nOmDwAHzKwhz2UbI2OM44oftmlOVVgT7M7vQDQpF6E_I6Wf18-U0&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5IOdCzecJhMT1sx0qzOn33cI61MSFarRwGbI15ab5D4Z_oD_U-YlCT8DV0RY&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHS6J5CfdonfZWDqi-2mO1axz_9wUrSeuf1UqYOVNFQGbj7JEEN7HyAsC0GQ&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSD510ur7mPl_E4UlKVB8ZNbXRaKO2uRoN5tQheuTNPtM9hqZdNyLuyB6-jlA&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNqLtcRI01HyBOV-8Qzi1Exa_bJ6nSJDd28-orJhFtjAy4De3KDyAKSKSgSMM&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT62aujzJG_Zw3P4Q6M90Ys_rtti1xLlQgGDo3bBz1WZf8MTmHu1cuK2b6Z_w&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIfXB7vLIQ9gb59kwzXsX7z3aRf1Ivh3OKhkKdaSgZJtIlVEL-pSprmVQ7FQ&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh2lDENjqe4allaqoUejTI9BPkMXUYlFW0NKGtK2Xif1YPlYoRqO_CqkhbHA&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAw7cKO9-_trB2y6X3bKV_dJgQtnRNWgZFwgqqbf9a3nb9Sn-NaGhfiDOVb6g&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_kNitrhJMNz13Ag0Bxmh2iWNKIxg7H3ZrGLMjSyrLSySTLf3MVKkTK7hSG6Q&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAcM0jEOgQXmHT1mHEa90jkvBNJUYfwN_L7QEt4giIHZFd7f8pRHnHjHvQzrU&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnBGPFY8w-BZ3nrYxXSojVS0Fe3B5adLCvxR7juufUpkN-YU1OMbbuZ_oH3A&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2Cm6DhfRqDKDN0dYO7dwAn-yR4ap0MdLtLGxPT_whc4xZFdrh2MQCk7Bt0kU&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW_NNsHIqtCuFWajimGOv6RJneGaRM2-8h3hgGvOd4Mmq5xsstGO4Lqu24yj4&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiwqoGycNcwxiVqzz4T4_av7k2WFmHbOkyedY6yLeCQtRsjyRj9t5gC7xLK88&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzvb4h38_iIFAzlpkLWTHAA5ia49XolyuLCTmbDsOaPk4WTVRdi2Xgi-Nphg&s.jpg', 
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrs6U8hv6X5juBN1M_SPQUXFvjlKlenI0uPJVTIQmlYH2WHD2UnqPHXeCi8-8&s.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXwVlPmYgDMw7t8vwf1By8MxdSHii1-UlYR3NQSWBxQL01VC2IH4wpg683TQ&s.jpg']
# Channel Access Token
app = Flask(__name__)
line_bot_api = LineBotApi(
    'Oj5u1W0iXCh02EY/05XHu0SPSo9XbUH6aIak7CSPsZCK3tqPMJH2OLda5ucMIllli7vVe0L5bnItmLf34WrbH4Hkf1Db2aXuu2FDanzp3VGMtw1BO2g+5hqLE2sffbqtTqyrVdTNyLon9rWrEMP4ugdB04t89/1O/w1cDnyilFU=')
# or line_bot_api = 'Channel_token'

# Channel Secret
handler = WebhookHandler('d29ad32bdef2a6513f1ba6280e49627e')
# or handler = 'Channel_secret'

# 監聽所有來自 /callback 的 Post Request
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
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息


@handler.add(MessageEvent, message=TextMessage,message1=TextMessage,message2=TextMessage,message3=TextMessage)
def story(event):
    get = event.message.text
# event.gessage.text接收使用者文字訊息

    if get == "你幾歲":
        result = random.randint(0, 3)
        if result == 0:
            message = TextSendMessage(text="20")
        elif result == 1:
            message = TextSendMessage(text="30")
        elif result == 2:
            message = TextSendMessage(text="40")
        else:
            message = TextSendMessage(text="50")
    if('水瓶座' in get):
        message = TextSendMessage(
            text="水瓶是一個持著瓶子在酒吧的美少年蓋尼米德，他是特洛伊的王子。\n有一天，他替父親看羊時，我在天空經過，一看到他的臉就愛上他了，因為太愛他了，我就變身成一隻老鷹擄走他到奧林匹斯山跟我一起住。")
        # print("water")
    if('雙魚座' in get):
        message = TextSendMessage(
            text="希臘神話中雙魚座代表的是阿佛洛狄忒和厄洛斯在水中的化身。阿佛洛狄忒為了逃避大地女神蓋亞之子巨神提豐攻擊而變成魚躲在尼羅河（一說幼發拉底河）。之後她發現忘記帶上自己的兒子厄洛斯一起逃走，於是又上岸找到厄洛斯。為防止與兒子失散，她將兩人腳綁在一起，隨後兩人化為魚形，潛進河中。\n事後我將阿佛洛狄忒首先化身的魚提升到空中成為南魚座，而她和厄洛斯化身的綁在一起的兩條魚則稱為雙魚座。")
    if('金牛座' in get):
        message = TextSendMessage(text="金牛座是我的化身。因為我喜歡阿戈諾爾（Agenor）的女兒歐羅芭（Europa），她常在蘇爾沙灘上玩，我之後便要赫耳墨斯（Hermes）在附近的一個小丘上放牛，然後我就化身成牛混在牛群中，趁機靠近她。由於此牛十分雪白、牛角閃閃發光，歐羅芭深被牠吸引，白牛示意她騎上去，她無知中計，牠載歐羅芭渡過海洋，游到深水的地方，迫使歐羅芭抱著牠，終於在克里特島上露出真面目，宙斯得歐羅芭歡心，她也替我生了多個兒子，我為了紀念此事，金牛座是其化身的牛，並以歐羅芭的名字來命名大陸 - 歐羅芭洲，就是歐洲。星圖只顯示牛的上半身，下半身在水中，並不可見。金牛座七姊妹星團（Pleiades）的故事：七姊妹其實是阿特拉斯（Atlas）和普勒俄涅（Pleione）的七個女兒，分別是阿爾庫俄涅（Alcyone），斯忒羅珀（Sterope），刻萊諾（Calaeno），厄勒克特拉（Electra），邁亞（Maia），墨羅佩（Merope）及塔宇革忒（Taygete），阿爾庫俄涅及刻萊諾給波塞冬誘姦，最大的女兒邁亞替宙斯誕下了赫耳墨斯，並且成為阿卡斯（Arcas）的後母，厄勒克特拉替我生下特洛伊的建城者達爾達諾斯（Dardanus），塔宇革忒替宙斯生下斯巴達的建城者拉刻代蒙（Lacedaemon），斯忒羅珀被戰神阿瑞斯強暴並誕下皮薩（Pisa）皇俄諾瑪俄斯（Oenomaus），墨羅佩則嫁給了凡人、風神埃俄羅斯的兒子西敘福斯。七姊妹星團中只可看到六顆，一說墨羅佩由於嫁予凡人，故光芒最弱；一說是因為厄勒克特拉用手掩蓋自己的眼睛，不忍見到特洛伊的滅亡，但最暗的星其實是斯忒羅珀。")
    if('天蠍座' in get):
        message = TextSendMessage(text="天蠍座神話之一——太陽神阿波羅的兒子--法厄同，天生美麗而性感，他自己也因此感到自負，態度總是傲慢而無禮，太過好強的個性常使他無意間得罪了不少人。有一天，有個人告訴法厄同說：「你並非太陽神的兒子！」說完大笑揚長而去，好強的法厄同怎能吞得下這口氣，於是便問自己的母親：「我到底是不是阿波羅的兒子呢？」但是不管母親如何再三保證他的確就是阿波羅所生，法厄同仍然不相信他的母親，於是說：「取笑你的人是我的兒子，地位很高，如果仍然不相信，那麼去問太陽神阿波羅自己吧！」阿波羅聽了自己兒子的疑問，笑著說：「別聽他們胡說，你當然是我的兒子！」法厄同仍執意不信，其實他當然知道太陽神從不說謊，可是他卻另有目的—要求駕駛父親的太陽車，以證明自己就是阿波羅的兒子。「這怎麼行？」阿波羅大驚，太陽是萬物生息的主宰，一不小心就會釀巨禍，但拗不過法厄同，阿波羅正說明著如何在一定軌道駕駛太陽車時，法厄同心高氣傲，聽都沒聽立刻跳上了車，疾馳而去。結果當然很慘，地上的人們、動物、植物不是熱死就是凍死，也亂了時間，弄得天錯地暗，怨聲載道。眾神們為了遏止法厄同，由天后赫拉放出一支毒蠍，毒蠍向法厄同攻擊，法厄同根本來不及反應，毒蠍就咬住了法厄同的腳踝，而我則用可怕的雷霆閃電擊中了法厄同，只見法厄同慘叫一聲墮落到地面，法厄同最終死了，人間又恢復了寧靜，為了紀念那隻也被閃電擊斃的毒蠍，這個星座就被命名為「天蠍座」。")
    if('雙子座' in get):
        message = TextSendMessage(
            text="雙子座代表的是希臘神話中的天神我與斯巴達王后勒達所生的孿生子(雙胞胎)卡斯托耳和波魯克斯（合稱狄俄斯庫里兄弟），兩人一生充滿無數的英雄壯舉。但他們因和伊達斯和林叩斯分配戰利品時產生矛盾，互相反目成仇並開始決鬥，結果林叩斯被卡斯托耳殺死，卡斯托耳被伊達斯殺死，伊達斯又被波魯克斯殺死。波魯克斯向我哀求如果能讓卡斯托耳復活，他寧願放棄自己的不死之身。我被兄弟倆的友愛精神所感動，將他們提升到天界，成為雙子座。")
    if('白羊座' in get):
        message = TextSendMessage(
            text="在希臘神話裡，白羊座指的是一隻有神奇能力的羊，他幫助一對苦難的兄妹脫離險境。可憐的富利科索斯和克拉兄妹，是後母依諾的眼中釘，他不但常虐待這對兄妹，而且計畫要殺死他們。這對兄妹的親生母親涅菲麗知道以後，著急地祈求天帝宙斯解救兄妹倆。因為涅菲麗的虔誠祈求，於是我將一頭全身金毛，長著雙翅的羊送給這對兄妹，好讓兄妹乘著羊飛上天空，脫離依諾的控制。可惜，當他們飛到中途，妹妹克拉卻不慎落入海裡溺死了。於是這頭金羊一邊安慰傷心欲絕的哥哥，一面堅強地朝目的繼續前進。")
    if('獅子座' in get):
        message = TextSendMessage(
            text="涅墨亞獅子是半人半蛇的妖怪厄喀德娜生下的，到處吞食生靈。 赫拉克勒斯拿著他的弓箭和他常用的木棒，來到涅墨亞山谷，找到了這頭獅子，先用弓箭射他，箭卻反彈回來，再用木棒打他，粗木棒卻碎裂，原來涅墨亞獅子是刀槍不入的，無論是用石器，銅器還是鐵器，都無法傷害到它。")
    if('處女座' in get):
        message = TextSendMessage(
            text="室女座象徵著春神珀耳塞福涅的美麗與純潔，母親養育的麥穗，也成為她手持之物。 另有一說，室女座代表的是正義女神阿斯特莉亞，在對人類感到失望後回到天上變成室女座，而其手中為人類所做之善惡裁判時所用的天秤則成為了天秤座。")
    if('天秤座' in get):
        message = TextSendMessage(
            text="天秤座是希臘神話中的正義女神阿斯特莉亞在為人類所做善惡裁判時所用的天平，阿斯特莉亞一隻手持天平，一隻手握斬除邪惡的劍。 為求公正，所以眼睛皆矇著。 從前的眾神和人類是和平共處於大地上，神雖擁有永遠的生命，但人類壽命有限。 因此寂寞的神只有不斷創造人類，然而那時的人好爭鬥，惡業橫行，眾神在對人類失望之餘回到天上。")
    if('摩羯座' in get):
        message = TextSendMessage(text="相傳山野之神潘恩專司管理放牧宙斯的牛羊之職，它頭上長有兩隻角，而腳卻是羊蹄。雖然他長得不英俊，甚至是醜陋，但精力旺盛且多情的他卻愛上了美麗的仙子邱林克絲，邱林克絲卻懼怕他的相貌，每每遠遠發現他就躲得無影無蹤。潘恩滿腔的痴情無以發泄，於是就做了蘆笛，把一腔的思念用悠長的悲怨的笛聲吹奏了出來。我在一次舉行宴會時，眾多賓客被潘恩淒涼的笛聲打動，就把他叫過來為眾神吹奏，以助酒性。當這如怨如泣的笛聲越傳越遠時，惹惱了怪物傑凡。怪物傑凡有著無數張面孔，勇力驚人，而且每張面孔都有一張發出震耳巨音的大嘴。最可怕的是傑凡也暗戀著美麗的仙子邱林克絲，並知道潘恩在追邱林克絲而滿肚醋水。當他聽到笛聲並看到眾神同情和欣賞潘恩時，怒氣沖沖地大吼著衝過來，在震耳欲聾的吼叫聲中，眾神紛紛避讓。 有化作飛禽的，有變作野獸的，甚至直接成為一縷青煙而無影無蹤。潘恩當然也毫無例外地逃避，但因吹笛時入情太深反應稍微遲緩了一些，顯得措手不及，直到傑凡衝到身邊時才縱身跳入水中，想變成魚藏匿，可是水太淺了，只是下半身變成了魚。與此同時，宙斯拿出武器「雷霆」和「我的盾」出來拒敵了。未能完全變化逃匿的潘恩見宙斯迎戰傑凡，勇氣陡生，馬上回身沖向傑凡。只可惜雙方力量過於懸殊，一個照面就殞命於傑凡之手。傑凡殺了潘恩後，害怕我報復匆匆逃跑了。宙斯感謝潘恩忠誠和勇敢，就讓潘恩化作了星空中和他一模一樣的星群。到了秋天后，在夜空的西南方向就能找到摩羯座。")
    if('巨蟹座' in get):
        message = TextSendMessage(
            text="而「巨蟹座」（Cancer）也是起源於古希臘的神話，傳說宙斯的私生子海格力斯和萊爾納的九頭大蛇（長蛇座）戰鬥時，海格力斯的死對頭赫拉派出巨蟹偷偷攻擊海格力斯的腳，結果海格力斯一怒之下把巨蟹踩成碎片，之後赫拉將巨蟹的碎片抬起至天空，成為巨蟹座。")
    if('射手座' in get):
        message = TextSendMessage(
            text="有一天海格拉斯和族人起衝突，被追殺的他就逃入肯農家中，憤怒的海格拉斯就瞄準半馬半人族頻頻放箭，卻不知老師肯農也混在其中，而射到他的腳。 因箭端沾了不死之身，所以無法從痛苦中解放。 巨人神普羅米修斯乃廢了其不死之身，讓他安詳而死，而成為天上的射手座。")   
def girl(event):
    get = event.message.text
    if('抽' in get):
        ran_num = random.randint(1, 60)
        result1 = Girl_Array[ran_num]
        message = ImageSendMessage(
            original_content_url=result1,
            preview_image_url=result1
        )
def map(event):
    get = event.message.text
    if('觀星' in get):
        message = TextSendMessage(
            text="全台觀星景點｜北部\n★陽明山：擎天崗\n★基隆：大武崙砲台\n★桃園：拉拉山\n★雪霸國家公園\n合歡山暗空公園\n★宜蘭：太平山\n全台觀星景點｜中部\n★玉山國家公園\n★南投：清境\n★阿里山\n★恆春：貓鼻頭\n全台觀星景點｜東部\n★花蓮：大農大富森林\n★台東:嘉明湖\n★您可以查詢以上地點會有相關路線以及其介紹★"
    if('陽明山' in get):
        message1 = ImageSendMessage(
            original_content_url='https://www.travel.taipei/content/images/attractions/65473/1024x768_attractions-image-cxh_ib5zs0wq1c0iv6cooq.jpg',
            preview_image_url='https://www.travel.taipei/content/images/attractions/65473/1024x768_attractions-image-cxh_ib5zs0wq1c0iv6cooq.jpg'
        )
    if('陽明山' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n陽明山的夜景在臺北市頗負盛名，隨著仰德大道直上，沿路都可欣賞到臺北市夜晚燦爛星空與閃爍燈海相映的景象，觀賞夜景的好地方還包括白雲山莊、竹子湖觀景台、永公路前、林語堂故居，及繞過陽明山公園往頂湖或北投地區之處。另外，二子坪遊憩區、擎天崗由於視野遼闊，一望無際，也十分適合觀星賞月。極具代表性的則是文化大學後山，因為離臺北盆地近，加上角度夠陡，如同俯身看夜景般，有種讓人瞬間就墜入萬家燈火夢境裡的感覺。"
           )
    if('陽明山' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='陽明山',
            latitude=25.194876190356684,
            longitude=121.56119365161739)
    if('大武崙砲台' in get):
        message1 = ImageSendMessage(
            original_content_url='https://mapio.net/images-p/21705320.jpg',
            preview_image_url='https://mapio.net/images-p/21705320.jpg'
        )
    if('大武崙砲台' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n北海岸的大武崙砲台，距離基隆市區不遠，也是北台灣十分著名的觀星景點。大武崙砲台的地理位置處於高處，非常適合觀星，因此北海岸及觀音山國家風景區管理處近年也開始舉辦觀星活動，帶領大眾體驗觀星的樂趣。"
           )
    if('大武崙砲台' in get):
        messag3 = LocationSendMessage(
            title='my location',
            address='大武崙砲台',
            latitude=(25.15883956907141,
            longitude=121.7084027926998)
    if('拉拉山' in get):
        message1 = ImageSendMessage(
            original_content_url='https://pic.pimg.tw/mttt543/1469122650-382915528_wn.jpg',
            preview_image_url='https://pic.pimg.tw/mttt543/1469122650-382915528_wn.jpg'
        )
    if('拉拉山' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n拉拉山上不僅蔭地是秋、日照成夏，入了夜還有像被打翻整個夜空的星子，山上視野遼闊，光害少，是觀星的好去處，但偶爾雲霧繚繞山頭，遮擋了一些視線，約略要等到快晚上十一點天才會開，那速度快的像是扯掉一塊黑布，光度不等的的羅列星棋已就定位，再來就是接受人們的仰望與讚嘆。")
    if('拉拉山' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='桃園拉拉山',
            latitude=(24.730588931200863,
            longitude=121.43416666464796)
    if('雪霸國家公園' in get):
        message1 = ImageSendMessage(
            original_content_url='https://assetsv4.tripmoment.com/system/redactor_assets/pictures/22300/content_330bcdcf-530a-4269-acaf-95e14f8d0c2e.jpg',
            preview_image_url='https://assetsv4.tripmoment.com/system/redactor_assets/pictures/22300/content_330bcdcf-530a-4269-acaf-95e14f8d0c2e.jpg'
        )
    if('雪霸國家公園' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n高海拔的雪霸國家公園，不只擁有豐富的生態環境，也是非常適合觀星的地點，其中，以武陵農場、觀霧遊憩區及合歡山等都是極佳的觀星場所。一日遊的話以「武嶺停車場」（看地圖）和「合歡主峰第一觀景台」為兩大最受觀星愛好者歡迎。前者雖然常有車燈燈害的干擾，但仰望還是可以看得到滿天星。而後者則是主峰最受歡迎的觀星攝影地點，由於觀景台造型的特殊性，這邊非常適合做取景或是拍星軌。")
    if('雪霸國家公園' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='雪霸國家公園',
            latitude=(24.41025288704792,
            longitude=121.232322528505)
    if('合歡山暗空公園' in get):
        message1 = ImageSendMessage(
            original_content_url='https://im.marieclaire.com.tw/m800c533h100b0/assets/mc/202009/5F6786C1466181600620225.jpeg',
            preview_image_url='https://im.marieclaire.com.tw/m800c533h100b0/assets/mc/202009/5F6786C1466181600620225.jpeg'
        )
    if('合歡山暗空公園' in get):
        message2= TextSendMessage(
            text="★景點介紹★\n合歡山國際暗空公園 （Hehuan Mountain Dark Sky Park ，HMDSP），在台 14 甲線 22.1 公里處開始，至 37.1 公里處止。依道路沿線，往左右各兩側約略 500 公尺的區域，包含昆陽、鳶峰、鳶峰天文教育館、武嶺、松、合歡山、松雪樓、滑雪山莊、太魯閣國家公園管理處合歡山管理站等觀星的地點。從 2018 年開始著手處理與申請，於  2019 年 12 月通過國際暗空協會 （IDA） 認證，成為亞洲第三座國際認證的國際暗空公園，僅次於韓國的英陽郡螢火蟲生態公園，晚上這裡的星星很多，適合大眾攜家帶眷來觀賞。")
    if('合歡山暗空公園' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='合歡山暗空公園',
            latitude=(24.119619044460528,
            longitude=121.23788298056792)
    if('太平山' in get):
        message1 = ImageSendMessage(
            original_content_url='https://wpimg.tedlin.tw/2017/10/TED_2387.jpg',
            preview_image_url='https://wpimg.tedlin.tw/2017/10/TED_2387.jpg'
        )
    if('太平山' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n若是想要有老師帶領、講解觀星課程，非常推薦到宜蘭太平山一遊。林務局羅東林區管理處針對住宿在太平山國家森林遊樂區的旅客，規劃了定期的觀星活動，由專業老師帶領室內課程與室外活動，十分適合全家大小一起參加。")
    if('太平山' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='太平山',
            latitude=(24.498019857300292,
            longitude=121.53519850951673)
     if('玉山國家公園' in get):
        message1 = ImageSendMessage(
            original_content_url='https://img.ltn.com.tw/Upload/news/600/2019/04/24/2768745_3.jpg',
            preview_image_url='https://img.ltn.com.tw/Upload/news/600/2019/04/24/2768745_3.jpg'
        )
    if('玉山國家公園' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n非常受到天文迷歡迎的觀星地，位於玉山國家公園的塔塔加絕對榜上有名。每到夜晚，各個星座、星體都在塔塔加的天空出現，不只容易辨識，想要拍出超美的星空照也沒問題！像是夫妻樹、停車場、遊客中心都是十分受到歡迎的地點。")
    if('玉山國家公園' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='玉山國家公園',
            latitude=(23.47007226805115,
            longitude=120.95773699769175)
    if('清境' in get):
        message1 = ImageSendMessage(
            original_content_url='https://static.accupass.com/eventintro/2008020759261199236260.jpg',
            preview_image_url='https://static.accupass.com/eventintro/2008020759261199236260.jpg'
        )
    if('清境' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n高海拔的清境，擁有眾多歐風建築及大片草原，還有最接近天空的天空步道，白天散步在這裡感覺像漫步在天空中；晚上抬頭望著星空彷彿倘佯在宇宙中，與天空零距離的地方自然是觀星的首選。")
    if('清境' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='南投：清境',
            latitude=(24.055406320121055,
            longitude=121.16240492909596)
    if('阿里山' in get):
        message1 = ImageSendMessage(
            original_content_url='https://www.mook.com.tw/images/upload/article/18293/A18293_1530766231_2.jpg',
            preview_image_url='https://www.mook.com.tw/images/upload/article/18293/A18293_1530766231_2.jpg'
        )
    if('阿里山' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n阿里山不只能看日出，位於阿里山國家森林遊樂區的小笠原山觀景平台視野極佳，加上高海拔、少光害的特色，仰頭就能看到滿天星斗，若是搭配使用天文望遠鏡，則可看到更多行星，絕對是天文迷必去的口袋名單。")
    if('阿里山' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='嘉義：阿里山',
            latitude=(23.509559804545784,
            longitude=120.82286189830182)
    if('貓鼻頭' in get):
        message1 = ImageSendMessage(
            original_content_url='http://jdanews.com/blog/wp-content/uploads/2018/12/48395686_1325658220909387_6999618303777832960_n.jpg',
            preview_image_url='http://jdanews.com/blog/wp-content/uploads/2018/12/48395686_1325658220909387_6999618303777832960_n.jpg'
        )
    if('貓鼻頭' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n位於台灣最南端的恆春半島，一直以來都是十分受到歡迎的觀星地，而貓鼻頭觀景台的地理位置不只遠離光害，還能遠遠眺望許多恆春的知名景點，因此十分受到觀星族的喜愛。")
    if('貓鼻頭' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='恆春：貓鼻頭',
            latitude=(21.92218492616225,
            longitude=120.73794138722731)
    if('大農大富森林' in get):
        message1 = ImageSendMessage(
            original_content_url='https://www.welcometw.com/wp-content/uploads/2020/12/1-1-2-681x851.jpg',
            preview_image_url='https://www.welcometw.com/wp-content/uploads/2020/12/1-1-2-681x851.jpg'
        )
    if('大農大富森林' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n位於花蓮光復鄉的大農大富森林，不只有著廣闊的園區佔地，生態也保持得十分好，在這裡白天可以觀察各種生物、生態，夜晚就成為觀星的好去處。臺北市立天文科學教育館也在這裡舉辦天文營活動，帶領民眾了解天文知識。而另外在花蓮南邊富里鄉的六十石山也是花東縱谷另一個熱門的觀星景點之一。尤其在每年的八月九月六十石山金針花盛開時，超大面積金針花海搖曳，也由於此處地點空曠無光害也幾乎沒有居民，因此這邊晚上也是個絕佳的觀星點喔！")
    if('大農大富森林' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='花蓮：大農大富森林',
            latitude=(23.614972749304535,
            longitude=121.41769591118695)
    if('嘉明湖' in get):
        message1 = ImageSendMessage(
            original_content_url='https://cdntwrunning.biji.co/800_e3551bad7f2ebc2dbd87290c15482e5d.jpg',
            preview_image_url='https://cdntwrunning.biji.co/800_e3551bad7f2ebc2dbd87290c15482e5d.jpg'
        )
    if('嘉明湖' in get):
        message2 = TextSendMessage(
            text="★景點介紹★\n假日無處去？何不跟上觀星潮流，到全台各地觀星、露營，享受親近大自然的樂趣！在滿天熠熠星辰底下，悠閒的享受靜謐時光，洗滌疲憊、好好充電，才能迎接工作上、生活中的每一個挑戰！風景如畫的嘉明湖是您的好選擇!")
    if('嘉明湖' in get):
        message3 = LocationSendMessage(
            title='my location',
            address='台東：嘉明湖',
            latitude=(23.29353208694757,
            longitude=121.03399940933431)
    
    line_bot_api.reply_message(event.reply_token, message,message1,message2,message3)
    

if __name__ == "__main__":
    app.run()
