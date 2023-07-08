import json
import sys
from random import randint
from time import time

import aiohttp
from Mitsuri import aiohttpsession 
from aiohttp import ClientSession

from Python_ARQ import ARQ

from Mitsuri import BOT_ID, OWNER_ID, ARQ_API_URL, ARQ_API_KEY
from Mitsuri import pbot

SUDOERS = OWNER_ID
ARQ_API_URL = "https://arq.hamker.in"

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

app = pbot
import socket
