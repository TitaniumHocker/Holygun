# -*- coding: utf-8 -*-
from holygun.bot import client as bot
from datetime import datetime
import asyncio


timetable = {
    '08-45': 'Доброе утро! Обращаю Ваше внимание, что занятия начнутся через 15 минут.',
    '09-00': 'Началась первая пара.',
    '10-30': 'Пара закончилась, перемена.',
    '10-40': 'Перемена закончилась, началась вторая пара.',
    '12-10': 'Пара закончилась, большая перемена. "НЯМ-НЯМ"',
    '12-40': 'Перемена закончилась, началась третья пара.',
    '14-10': 'Пара закончилась, перемена.',
    '14-20': 'Перемена закончилась, началась четвертая пара.',
    '15-50': 'Четвертая пара закончилась. До встречи).'
}


async def bell():
    await bot.wait_until_ready()
    while not bot.is_closed():
        current_time = datetime.today().strftime('%H-%M')
        current_weekday = datetime.today().weekday()
        channel = bot.get_channel(691958207484264498)
        if current_weekday < 5 and current_time in timetable.keys():
            await channel.send(timetable[current_time])
            await asyncio.sleep(65)
        else:
            await asyncio.sleep(1)


bot.loop.create_task(bell())
