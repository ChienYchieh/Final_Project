from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import random
import The_girls_url 
ran_num = random.randint(1, 62)
result1 = Girl_Array[ran_num][0]
result2=result1+".jpg"
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


@handler.add(MessageEvent, message=TextMessage)
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
    if('黑人問號' in get):
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/zTOnfAi.jpg',
            preview_image_url='https://i.imgur.com/zTOnfAi.jpg'
        )
    if('抽' in get):
        message = ImageSendMessage(
            original_content_url=result2,
            preview_image_url=result2
        )
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()
