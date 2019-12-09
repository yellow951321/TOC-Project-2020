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

    def is_going_to_choose_platform(self, event):
        text = event.message.text
        return text.lower() == "recommend"

    def is_going_to_recommend_ps4(self, event):
        text = event.message.text
        return text.lower() == "ps4"

    def is_going_to_recommend_xbox_one(self, event):
        text = event.message.text
        return text.lower() == "xbox_one"

    def is_going_to_recommend_pc(self, event):
        text = event.message.text
        return text.lower() == "pc"

    def is_going_to_recommend_nintendo_switch(self, event):
        text = event.message.text
        return text.lower() == "nintendo_switch"

    def is_going_to_codmw(self, event):
        text = event.message.text
        return text.lower() == "fps"

    def is_going_to_p5(self, event):
        text = event.message.text
        return text.lower() == "jrpg"

    def is_going_to_mhw(self, event):
        text = event.message.text
        return text.lower() == "arpg"

    def is_going_to_rdr2(self, event):
        text = event.message.text
        return text.lower() == "tps"

    def is_going_to_online_game(self, event):
        text = event.message.text
        return text.lower() == "online_game"

    def is_going_to_hollow_knight(self, event):
        text = event.message.text
        return text.lower() == "metroidvania"

    def on_enter_draw(self, event):
        reply_token = event.reply_token
        send_image_url(reply_token, "https://portertoc.herokuapp.com/show-fsm")
        self.go_back()

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

    def on_enter_choose_platform(self, event):
        print("I'm entering choose_platform")
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='choose platform',
                text='Choose which platform you want to know',
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

    def on_enter_recommend_ps4(self, event):
        print("I'm entering recommend_ps4")
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='choose game type',
                text='Choose which type of game you want to know',
                thumbnail_image_url='https://media.playstation.com/is/image/SCEA/playstation-4-pro-vertical-product-shot-01?$native_t$',
                actions=[
                    MessageTemplateAction(
                        label='fps',
                        text='fps'
                    ),
                    MessageTemplateAction(
                        label='jrpg',
                        text='jrpg'
                    ),
                    MessageTemplateAction(
                        label='arpg',
                        text='arpg'
                    ),
                    MessageTemplateAction(
                        label='tps',
                        text='tps'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        send_template(reply_token, buttons_template)

    def on_enter_recommend_xbox_one(self, event):
        print("I'm entering recommend_xbox_one")
        reply_token = event.reply_token
        send_text_message(reply_token, "我沒買，想玩自己買")
        self.go_back()

    def on_enter_recommend_pc(self, event):
        print("I'm entering recommend_pc")
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='choose game type',
                text='Choose which type of game you want to know',
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/1200px-Steam_icon_logo.svg.png',
                actions=[
                    MessageTemplateAction(
                        label='online_game',
                        text='online_game'
                    ),
                    MessageTemplateAction(
                        label='arpg',
                        text='arpg'
                    ),
                    MessageTemplateAction(
                        label='metroidvania',
                        text='metroidvania'
                    ),
                    MessageTemplateAction(
                        label='fps',
                        text='fps'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        send_template(reply_token, buttons_template)

    def on_enter_recommend_nintendo_switch(self, event):
        print("I'm entering recommend_nintendo_switch")
        reply_token = event.reply_token
        send_text_message(reply_token, "任天堂的遊戲買就對了")
        self.go_back()

    def on_enter_codmw(self, event):
        print("I'm entering codmw")
        reply_token = event.reply_token
        send_text_message(reply_token, "Call of Duty Morden warfare")
        self.go_back()

    def on_enter_p5(self, event):
        print("I'm entering p5")
        reply_token = event.reply_token
        send_text_message(reply_token, "Persona 5")
        self.go_back()

    def on_enter_mhw(self, event):
        print("I'm entering mhw")
        reply_token = event.reply_token
        send_text_message(reply_token, "Monster Hunter World")
        self.go_back()

    def on_enter_rdr2(self, event):
        print("I'm entering rdr2")
        reply_token = event.reply_token
        send_text_message(reply_token, "red dead redemption 2")
        self.go_back()

    def on_enter_online_game(self, event):
        print("I'm entering online_game")
        reply_token = event.reply_token
        send_text_message(reply_token, "問朋友想玩啥")
        self.go_back()

    def on_enter_hollow_knight(self, event):
        print("I'm entering online_game")
        reply_token = event.reply_token
        send_text_message(reply_token, "hollow knight")
        self.go_back()

