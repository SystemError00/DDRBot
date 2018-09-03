import asyncio
import DDRSetImage
import image
import random
from random import randint
import os

def DDRSet():
        try:
                First = random.randint(1,784)
                Second = random.randint(1,784)
                Third = random.randint(1,784)
                DDRSetImage.DDRSet(First, Second, Third)
                del First, Second, Third
        except:
                print("Error building DDR Set")
                DDRSet()

#ThisIsAHardCodedPassphrase
