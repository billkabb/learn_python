## ixos sthn python video77
#import winsound

#winsound.Beep(100,400)
#import os
#os.system('play --no-show-progress --null --channels 1 synth %s sine %f' %(400,100))
from pygame import mixer
mixer.init()
alert=mixer.Sound('boom.wav')
alert.play()
