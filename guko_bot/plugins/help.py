from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import json
import random

helps = on_command('help',priority=5)

@helps.handle()
async def help(bot: Bot, event: Event, state: dict):
    helpContent = await get_help()
    await helps.finish(helpContent)


async def get_help():
    return '鸽子姬进化啦！以下是鸽子姬的食用说明:\n1. .help查看Dice!的使用方法\n2. .eatwhathelp查看今天吃啥的帮助\n3. 搜图模式 或者 @鸽子姬 开启搜图模式\n4. .fu获取来自fulao的人生指导\n5. /help查看来自獭.net的奇妙指令\n6. .gu获取一张咕咕表情包\n7. .clock [事件] [时间]添加一个提醒事件（在做了）'