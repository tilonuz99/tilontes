import  json
from pyrogram import Client

from pyrogram import Client, Filters
api_id = 1194939
api_hash = "d8ed4b10ed554767a4570cf59c3ea49e"

APP =  Client("my_account",api_id,api_hash)
APP.start()
@APP.on_message(Filters.private)
def get(cl,message):
    TXT = message.text
    if(TXT.find("t.me/c/") != -1):
        URL1 = TXT.replace("https://t.me/c/","")
        URL = URL1.split("/")
        USERNAME = URL[0]
        POSTID = URL[1]
        XABAR = APP.get_messages("-100"+str(USERNAME),int(POSTID))
        CALL = XABAR.reply_markup.inline_keyboard[0][0].callback_data
        JSONCALL = json.loads(CALL)
        JSONDUMP = json.dumps(JSONCALL["id"])
        message.reply("@like #"+eval(JSONDUMP))
        print("\n\n#"+eval(JSONDUMP)+"\n\n")
    else:
        URL1 = TXT.replace("https://t.me/","")
        URL = URL1.split("/")
        USERNAME = URL[0]
        POSTID = URL[1]
        XABAR = APP.get_messages(chat_id=str(USERNAME),message_ids=int(POSTID))
        CALL = XABAR.reply_markup.inline_keyboard[0][0].callback_data
        JSONCALL = json.loads(CALL)
        JSONDUMP = json.dumps(JSONCALL["id"])
        message.reply("@like #"+eval(JSONDUMP))
        print("\n\n#"+eval(JSONDUMP)+"\n\n")
