from IgnScraper import IgnScraper
from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_url,send_template
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage, TemplateSendMessage, ButtonsTemplate,PostbackTemplateAction, MessageTemplateAction, URITemplateAction,ImageSendMessage



scraper = IgnScraper('ps4')
scraper.asyncGetPages()
titleList = scraper.getTitleLists()
msg = ''
for index in range(len(titleList)):
    msg += scraper.getBasicInfo(titleList[index]['url'])
    if index != range(len(titleList)):
        msg += '\n'

print(msg)