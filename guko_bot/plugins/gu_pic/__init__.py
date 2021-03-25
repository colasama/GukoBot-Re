from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import time
import urllib
from aiocqhttp import MessageSegment
import requests
import random
import os

gupic = on_command('gu',priority=5)

@gupic.handle()
async def gu(bot: Bot, event: Event, state: dict):
    path="C:/Users/colan/OneDrive/Codes/Guko_Bot/Nonebot2/guko_bot/plugins/guPic/guDB/"
    imgs = []
    for x in os.listdir(path):
        if x.endswith('jpg'):
            imgs.append(x)

    what=path+random.sample(imgs,k=1)[0]
    seq = MessageSegment.image(what.format('8531'))
    await gupic.finish(seq)