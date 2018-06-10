import discord
import asyncio
import DDRSetImage
from PIL import Image
import random
from random import randint
import csv
import os

client = discord.Client()

@client.event
async def on_ready():
        print("Beep Boop DDR Bot")
        print("ID: ",client.user.id)
        print("Up and runnin'!")
        print('--------')

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='xxxxxxxxxxxxxxxxxx')
    while not client.is_closed:
        #await client.send_message(channel, "Beep boop, DDRBot Set Of The Week!")
        First = random.randint(1,746)
        Second = random.randint(1,746)
        Third = random.randint(1,746)
        DDRSetImage.DDRSet(First, Second, Third)
        await client.send_file(channel, 'DDRBotSetOfTheWeek.jpg')        
        await asyncio.sleep(8400) # task runs every 24 hours

        
client.loop.create_task(my_background_task())
client.run("ID")



#ThisIsAHardCodedPassphrase
