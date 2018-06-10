import discord
import asyncio
import DDRSetImage
import image
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

def DDRSet():
        try:
                First = random.randint(1,767)
                Second = random.randint(1,767)
                Third = random.randint(1,767)
                DDRSetImage.DDRSet(First, Second, Third)
        except:
                print("Error building DDR Set")
                DDRSet()

'''
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed:
        Phrases = ["Braaaaap", "Bopadopalous!", "Bep...", ">:(", "Womp...", "Beep beep~", "!"]
        Intro = random.choice(Phrases)
        await client.send_message(channel, Intro)
        await client.send_message(channel, "DDRBot Song of the Day!!")
        Song_Of_The_Day = random.randint(1,746)
        await client.send_file(channel, '%d.jpg' % (Song_Of_The_Day))
        print("This is a test output")
        await asyncio.sleep(86400) # task runs every 24 hours'''

        
@client.event
#channel = discord.Object(id='xxxxxxxxxxxxxxxxxx')

async def on_message(message):
        if message.content.startswith('phrase'):
                global SetCount
                if SetCount == 0:
                        await client.send_message(message.channel, "DDRBot limit reached for the day.")
                else:
                        DDRSet()
                        await client.send_file(message.channel, 'DDRBotSetOfTheWeek.jpg')
                        SetCount -= 1


#client.loop.create_task(my_background_task())
client.run("ID")
                


#ThisIsAHardCodedPassphrase
