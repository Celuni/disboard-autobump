# WARNING
# This script is designed to run on user accounts, which is not allowed by Discord (Terms of Service). Use this script at your own risk.
# ©2019 aper.me developers

import os
import logging
import asyncio
import discord
from discord.ext import commands 

logging.basicConfig(level='INFO')

bot = commands.Bot(description='DISBOARD.com Bumper bot. V1.0 - ©2019 aper.me', command_prefix=['bumper ', 'Bumper ']) 

TOKEN = os.environ["TOKEN"]

@bot.command(aliases=['bump'])
async def start(ctx):
    """Starts bumping every 2 hours."""
    while 1:
        bumpy=0
        bumpy=bumpy+1
        try:
            print('Processing a new bump...')
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            print(f'Bump nr. {bumpy} processed succesfully !')
        except:
            print(f'Couldn\'nt process bump nr. {bumpy}.')

@bot.event
async def on_connect():
    print('Successfully connected !')

@bot.event
async def on_ready():
    print('All systems fully operationnal !')

bot.run(TOKEN, bot=False)
