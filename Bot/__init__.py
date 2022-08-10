import os, sys, logging
from pyrogram import Client 


#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5439505484:AAFvPErSWaSBcrkaKHtnumPG6nxm2w1JCQk') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 4665778)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', '10e3ed833b0d09699973420d45359409')# Telgram App hash  
OWNER_ID = os.environ.get('OWNER_ID', 5531584953)
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://ok:lol@cluster1.udhzs7r.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1001775110866)
BOT_NAME = os.environ.get('BOT_NAME', 'Garou')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoRename', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
