import os
import asyncio
from ast import literal_eval
#import pandas as pd
import urllib.request
import requests

def DownloadDatabase():
    urllib.request.urlretrieve("http://skillattack.com/sa4/data/master_music.txt", "master_music.txt")
    #urllib.request.urlretrieve("https://p.eagate.573.jp/game/ddr/ddra/p/images/binary_jk.html?img="%s % (code),"sample.jpg")

def DownloadImages(code, i):
    print (i)
    urllib.request.urlretrieve("https://p.eagate.573.jp/game/ddr/ddra/p/images/binary_jk.html?img=%s" % code, "%d.jpg" % i)
    #print("https://p.eagate.573.jp/game/ddr/ddra/p/images/binary_jk.html?img=%s" % code)
    #i += 1

def ReadFile():
    i = 0
    with open("master_music.txt","r",encoding="Shift_JIS") as DDRSongs:
        for line in DDRSongs.readlines():
            Song = line.split("	")
            print(Song[11],Song[5])

'''
The following are information from Data:
0 = listing number
1 = code
2 = BeSP
3 = BSP
4 = DSP
5 = ESP
6 = CSP
7 = BDP
8 = DDP
9 = EDP
10= CDP
11= Song Name
12= Artist

Sample page of image: https://p.eagate.573.jp/game/ddr/ddra/p/images/binary_jk.html?img=186dd6DQq891Ib9Ilq8Qbo8lIqb0Qoll
'''

DownloadCommand = input("Download new database? ")
if DownloadCommand == "yes":
    DownloadDatabase()
    print("Download complete")


DownloadCommand2 = input("Download images? ")
if DownloadCommand2 == "yes":
    i = 0
    with open("master_music.txt","r",encoding="Shift_JIS") as codes:
        for line in codes.readlines():
            Song = line.split("	")
            print (Song[1])
            print (".")
            h = urllib.request.urlopen("https://p.eagate.573.jp/game/ddr/ddra/p/images/binary_jk.html?img=%s" % Song[1])
            content_length = h.info()['Content-Length']
            print(content_length)
            if int(content_length) > 3000:  # 3KB
                urllib.request.urlretrieve("https://p.eagate.573.jp/game/ddr/ddra/p/images/binary_jk.html?img=%s" % Song[1], "%d.jpg" % i)
                print("https://p.eagate.573.jp/game/ddr/ddra/p/images/binary_jk.html?img=%s" % Song[1])
                DownloadImages(Song[1],i)
                i += 1
        print("Download complete")
