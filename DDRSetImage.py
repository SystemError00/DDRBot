import sys
import random
from PIL import Image
import numpy as np
import PIL

def DDRSet (First, Second, Third):
    list_im = ['%s.jpg' % (First), '%s.jpg' % (Second), '%s.jpg' % (Third)]
    imgs    = [ PIL.Image.open(i) for i in list_im ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

    #image save
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save( 'DDRBotSetOfTheWeek.jpg' )    
