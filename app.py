
import os
import sys

from fsm import TocMachine
from utils import send_text_message

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


load_dotenv()


machine = TocMachine(
    states=['user', 'draw', 'game_news', 'ps4', "xbox_one", "pc", "nintendo_switch", "choose_platform", "recommend_ps4", "recommend_xbox_one", "recommend_pc", "recommend_nintendo_switch", "rdr2", "p5", "codmw", "mhw", "online_game", "hollow_knight"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "draw",
            "conditions": "is_going_to_draw",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "game_news",
            "conditions": "is_going_to_game_news",
        },
        {
            "trigger": "advance",
            "source": "game_news",
            "dest": "ps4",
            "conditions": "is_going_to_ps4",
        },
        {
            "trigger": "advance",
            "source": "game_news",
            "dest": "xbox_one",
            "conditions": "is_going_to_xbox_one",
        },
        {
            "trigger": "advance",
            "source": "game_news",
            "dest": "pc",
            "conditions": "is_going_to_pc",
        },
        {
            "trigger": "advance",
            "source": "game_news",
            "dest": "nintendo_switch",
            "conditions": "is_going_to_nintendo_switch",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "choose_platform",
            "conditions": "is_going_to_choose_platform",
        },
        {
            "trigger": "advance",
            "source": "choose_platform",
            "dest": "recommend_ps4",
            "conditions": "is_going_to_recommend_ps4",
        },
        {
            "trigger": "advance",
            "source": "choose_platform",
            "dest": "recommend_xbox_one",
            "conditions": "is_going_to_recommend_xbox_one",
        },
        {
            "trigger": "advance",
            "source": "choose_platform",
            "dest": "recommend_pc",
            "conditions": "is_going_to_recommend_pc",
        },
        {
            "trigger": "advance",
            "source": "choose_platform",
            "dest": "recommend_nintendo_switch",
            "conditions": "is_going_to_recommend_nintendo_switch",
        },
        {
            "trigger": "advance",
            "source": "recommend_ps4",
            "dest": "codmw",
            "conditions": "is_going_to_codmw",
        },
        {
            "trigger": "advance",
            "source": "recommend_ps4",
            "dest": "p5",
            "conditions": "is_going_to_p5",
        },
        {
            "trigger": "advance",
            "source": "recommend_ps4",
            "dest": "mhw",
            "conditions": "is_going_to_mhw",
        },
        {
            "trigger": "advance",
            "source": "recommend_ps4",
            "dest": "rdr2",
            "conditions": "is_going_to_rdr2",
        },
        {
            "trigger": "advance",
            "source": "recommend_pc",
            "dest": "online_game",
            "conditions": "is_going_to_online_game",
        },
        {
            "trigger": "advance",
            "source": "recommend_pc",
            "dest": "mhw",
            "conditions": "is_going_to_mhw",
        },
        {
            "trigger": "advance",
            "source": "recommend_pc",
            "dest": "hollow_knight",
            "conditions": "is_going_to_hollow_knight",
        },
        {
            "trigger": "advance",
            "source": "recommend_pc",
            "dest": "codmw",
            "conditions": "is_going_to_codmw",
        },
        {"trigger": "go_back", "source": ["draw", "game_news", "ps4", "xbox_one", "pc", "nintendo_switch", "recommend_xbox_one", "recommend_nintendo_switch", "the_outer_world", "rdr2", "p5", "codmw", "mhw", "hollow_knight", "online_game"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.jpg", prog="dot", format="jpg")
    return send_file("fsm.jpg", mimetype="image/jpg")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
