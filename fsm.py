import random

from IgnScraper import IgnScraper
from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_url, send_template, send_multiple_text_message
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage, TemplateSendMessage, ButtonsTemplate,PostbackTemplateAction, MessageTemplateAction, URITemplateAction,ImageSendMessage

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_draw(self, event):
        text = event.message.text
        return text.lower() == "draw"

    def is_going_to_game_news(self, event):
        text = event.message.text
        return text.lower() == "game news"

    def is_going_to_ps4(self, event):
        text = event.message.text
        return text.lower() == "ps4"

    def is_going_to_xbox_one(self, event):
        text = event.message.text
        return text.lower() == "xbox_one"

    def is_going_to_pc(self, event):
        text = event.message.text
        return text.lower() == "pc"

    def is_going_to_nintendo_switch(self, event):
        text = event.message.text
        return text.lower() == "nintendo_switch"

    def on_enter_draw(self, event):
        reply_token = event.reply_token
        self.machine.get_graph().draw("fsm.jpg", prog="dot", format="jpg")
        send_image_url(reply_token, 'fsm.jpg')
        self.back()

    def on_exit_draw(self):
        print("leave draw")

    def on_enter_game_news(self, event):
        print("I'm entering state1")
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='console type',
                text='Choose which you want to know',
                thumbnail_image_url='https://cdn.mos.cms.futurecdn.net/yH5Zqu34tw3UpRDByq5gu-970-80.jpg',
                actions=[
                    MessageTemplateAction(
                        label='ps4',
                        text='ps4'
                    ),
                    MessageTemplateAction(
                        label='xbox_one',
                        text='xbox_one'
                    ),
                    MessageTemplateAction(
                        label='pc',
                        text='pc'
                    ),
                    MessageTemplateAction(
                        label='nintendo_switch',
                        text='nintendo_switch'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        send_template(reply_token, buttons_template)

    def on_enter_ps4(self, event):
        scraper = IgnScraper('ps4')
        scraper.asyncGetPages()
        titleList = scraper.getTitleLists()
        msg = []
        for index in range(len(titleList)):
            msg.append(scraper.getBasicInfo(titleList[index]['url']))

        reply_token = event.reply_token
        send_text_message(reply_token, msg[random.randint(0, len(msg) - 1)])
        self.go_back()

    def on_exit_ps4(self):
        print('ps4 leaving')

    def on_enter_xbox_one(self, event):
        scraper = IgnScraper('xbox-one')
        scraper.asyncGetPages()
        titleList = scraper.getTitleLists()
        msg = []
        for index in range(len(titleList)):
            msg.append(scraper.getBasicInfo(titleList[index]['url']))

        reply_token = event.reply_token
        send_text_message(reply_token, msg[random.randint(0, len(msg) - 1)])
        self.go_back()

    def on_exit_xbox_one(self):
        print('xbox-one leaving')

    def on_enter_pc(self, event):
        scraper = IgnScraper('pc')
        scraper.asyncGetPages()
        titleList = scraper.getTitleLists()
        msg = []
        for index in range(len(titleList)):
            msg.append(scraper.getBasicInfo(titleList[index]['url']))

        reply_token = event.reply_token
        send_text_message(reply_token, msg[random.randint(0, len(msg) - 1)])
        self.go_back()

    def on_exit_pc(self):
        print('pc leaving')

    def on_enter_nintendo_switch(self, event):
        scraper = IgnScraper('nintendo-switch')
        scraper.asyncGetPages()
        titleList = scraper.getTitleLists()
        msg = []
        for index in range(len(titleList)):
            msg.append(scraper.getBasicInfo(titleList[index]['url']))

        reply_token = event.reply_token
        send_text_message(reply_token, msg[random.randint(0, len(msg) - 1)])
        self.go_back()

    def on_exit_nintendo_switch(self):
        print('nintendo-switch leaving')

