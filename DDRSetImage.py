import sys
import random
from PIL import Image
import numpy as np
import PIL

def DDRSet (First, Second, Third):
    list_im = ['/Users/err0r/Desktop/DDRBot/images/%s.jpg' % (First), '/Users/err0r/Desktop/DDRBot/images/%s.jpg' % (Second), '/Users/err0r/Desktop/DDRBot/images/%s.jpg' % (Third)]
    imgs    = [ PIL.Image.open(i) for i in list_im ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

    # save that beautiful picture
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save( 'DDRBotSetOfTheWeek.jpg' )

    # for a vertical stacking it is simple: use vstack
    #imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    #imgs_comb = PIL.Image.fromarray( imgs_comb)
    #imgs_comb.save( 'Trifecta_vertical.jpg' )
