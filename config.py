#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7333917667:AAEhebM87s2TOcHDqWkq1xayBPgYWJ4mg_g")
    API_ID = int(os.environ.get("API_ID", "27215374"))
    API_HASH = os.environ.get("API_HASH", "b4495d7b9db5bb280121b4eeeb68331c")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6762856879")
