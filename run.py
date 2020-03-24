#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from holygun import create_bot
from config import configs


bot = create_bot()
config = configs['dev']


if __name__ == '__main__':
    bot.run(config.TOKEN)
