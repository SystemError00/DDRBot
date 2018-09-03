import discord
import asyncio
import DDRBotSet
import image
import random
from random import randint
import csv
import os, sys
import gc
import psutil

SetCount = 1
ResponseCount = 3
client = discord.Client()

#@client.event
#async def on_ready():
#        print("Beep Boop DDR Bot")
#        print("ID: ",client.user.id)
#        print("Up and runnin'!")
#        print('--------')

async def my_background_task():
    await client.wait_until_ready()
    #channel = discord.Object(id='396518242145009674')
    channel = discord.Object(id='374025686933045251')
    while not client.is_closed:
        await client.send_message(channel, "DDRBot Set of the Day Test!!")
        #Song_Of_The_Day = random.randint(1,784)
        #await client.send_file(channel, '/Users/err0r/Desktop/DDRBot/images/%d.jpg' % (Song_Of_The_Day))
        #print("Song of the day posted!")
        #del Song_Of_The_Day
        #print(" ")
        DDRBotSet.DDRSet()
        await client.send_file(channel, 'DDRBotSetOfTheWeek.jpg')
        print(process.memory_info().rss / 1024)  #I wanted to see how much memory was being used here.
        await asyncio.sleep(60) # task runs every 24 hours
        gc.collect()
        gc.garbage
        python = sys.executable
        os.execl(python, python, * sys.argv)    #Restart the program to try to keep memory usage low
        
@client.event
#channel = discord.Object(id='374025686933045251')

async def on_message(message):
        if message.content.startswith('Thank you, DDRBot!'):
                await client.add_reaction(message,'\U0001F621')
                print(process.memory_info().rss / 1024)


process = psutil.Process(os.getpid())
client.loop.create_task(my_background_task())
client.run("Mzc0MDE1NDAyOTgxNzIwMDc0.DNbS5Q.JbbNDrfUq-r1KgadRjD8PQo53dI")



#ThisIsAHardCodedPassphrase
