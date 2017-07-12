#!/usr/bin/env python3
from slacker import Slacker
import subprocess
import re

TIME = subprocess.Popen("date +%H:%M:%S", shell=True, stdout=subprocess.PIPE, )
TIME = TIME.communicate()[0]
FINAL_TIME = TIME.decode('utf-8')

slack = Slacker('API_KEY')

# Send a message to #general channel
slack.chat.post_message('#site-notifications', 'The server is down. Time: ' + str(FINAL_TIME))
