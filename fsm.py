from IgnScraper import IgnScraper
from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_url, send_template, send_multiple_text_message
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
        return text.lower() == "ps4"

    def is_going_to_get_info(self, event):
        text = event.message.text
        try:
            int(text)
            return True
        except:
            return False


    def on_enter_game_news(self, event):
        print("I'm entering state1")
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Start',
                text='按下Go開始',
                thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='ps4',
                        text='ps4'
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
                        label='nintendo-switch',
                        text='nintendo-switch'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        send_template(reply_token, buttons_template)
        # self.go_back()

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_ps4(self, event):
        scraper = IgnScraper('ps4')
        scraper.asyncGetPages()
        titleList = scraper.getTitleLists()
        msg = []
        for index in range(len(titleList)):
            msg.append(scraper.getBasicInfo(titleList[index]['url']))

        reply_token = event.reply_token
        send_multiple_text_message(reply_token, msg)
        self.go_back()

    def on_exit_ps4(self):
        print('ps4 leaving')

