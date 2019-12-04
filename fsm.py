from IgnScraper import IgnScraper
from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_url,send_template
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage, TemplateSendMessage, ButtonsTemplate,PostbackTemplateAction, MessageTemplateAction, URITemplateAction,ImageSendMessage


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_game_news(self, event):
        text = event.message.text
        return text.lower() == "game news"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_ps4(self, event):
        text = event.message.text
        return text.lower() == "Ps4"

    def on_enter_game_news(self, event):
        print("I'm entering state1")
        scraper = IgnScraper('ps4')
        scraper.asyncGetPages()
        titleList = scraper.getTitleLists()
        reply_msg = ""
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Start',
                text='按下Go開始',
                thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Ps4',
                        text='Ps4'
                    ),
                    MessageTemplateAction(
                        label='xbox-one',
                        text='xbox-one'
                    ),
                    MessageTemplateAction(
                        label='pc',
                        text='pc'
                    ),
                    MessageTemplateAction(
                        label='NS',
                        text='nintendo-switch'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        send_template(reply_token, buttons_template)
        # self.go_back()

    def on_exit_game_news(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def one_enter_ps4(self):
        print('ps4')
        self.go_back()

    def one_exit_ps4(self):
        print('ps4 leaving')
