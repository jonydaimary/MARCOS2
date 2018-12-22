
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = Bot(description="DarkBot Bot is best", command_prefix=">", pm_help = True)
client.remove_command('help')




@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Dark BOT')
    print('Created by Utkarsh')
    client.loop.create_task(status_task())


  

def is_owner(ctx):
    return ctx.message.author.id == "498378677512437762"


@client.command(pass_context = True)
async def tweet(ctx):
    await client.say('```tweet <name> <text>```')

    

client.run(os.getenv('Token'))
