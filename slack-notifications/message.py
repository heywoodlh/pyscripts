#!/usr/bin/env python3
from slacker import Slacker

slack = Slacker('token')

# Send a message to #general channel
slack.chat.post_message('#general', 'Hello fellow slackers!')
