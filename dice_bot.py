from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.dispatcher import Message

import re

@listen_to("Hello", re.IGNORECASE)

def hello(msg: Message):
    msg.send("world!!")

@respond_to("thank you", re.IGNORECASE)
def hi(msg: Message):
    msg.reply("Thank you too!!")
