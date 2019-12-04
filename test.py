from IgnScraper import IgnScraper
from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_url,send_template
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage, TemplateSendMessage, ButtonsTemplate,PostbackTemplateAction, MessageTemplateAction, URITemplateAction,ImageSendMessage



print("I'm entering state1")
scraper = IgnScraper('ps4')
scraper.asyncGetPages()
titleList = scraper.getTitleLists()
reply_msg = ""
buttons_template = TemplateSendMessage(
    alt_text='Buttons Template',
    template=ButtonsTemplate(
        title='choose console type',
        text='console list',
        # thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
        actions=[ MessageTemplateAction( label= key, text= key) for key in titleList ]
    )
)
print(buttons_template)