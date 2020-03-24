# -*- coding: utf-8 -*-
from holygun.bot import client as bot
import discord


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
