# -*- coding: utf-8 -*-
from holygun.bot import client as bot


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'Pong in {round(bot.latency * 1000)} ms!')
