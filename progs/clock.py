#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import winsound
 
 
 
def draw(s,m,h):
        os.system("cls")
        print """
_____ _                 _    _____ _                    
/  ___(_)               | |  |_   _(_)                    
\ `--. _ _ __ ___  _ __ | | ___| |  _ _ __ ___   ___ _ __
`--. \ | '_ ` _ \| '_ \| |/ _ \ | | | '_ ` _ \ / _ \ '__|
/\__/ / | | | | | | |_) | |  __/ | | | | | | | |  __/ |  
\____/|_|_| |_| |_| .__/|_|\___\_/ |_|_| |_| |_|\___|_|  
                 | |                                    
                 |_|                                    
"""
        print ""
        print " Seconds         Μinutes         Hours"  
        print " ["+s+"]             ["+m+"]             ["+h+"]"
        print ""
 
 
 
 
 
def song():
   for i in range(1,10):    
     winsound.Beep(2500,1000)
     winsound.Beep(2000,1000)
     winsound.Beep(1500,1000)
 
 
 
 
 
 
 
 
               
choice=input("1)Clock\n2)Alarm Clock\n\nChoice ==> ")
 
 
 
if(choice==1):
  secValue = 0
  mValue = 0
  hValue = 0
  while True:
        secValue += 1
        time.sleep(0.9)
        draw(str(secValue),str(mValue),str(hValue))
 
        if(secValue == 59):
                secValue = 0
                mValue += 1
                if(mValue == 59):
                        mValue = 0
                        hValue += 1
       
                                                                                                       
 
 
 
 
 
elif(choice==2):
  print "\nEnter the seconds,minutes,hours that you want.\n"
  sec_alarm=input("Seconds: ")
  m_alarm=input("Minutes: ")
  h_alarm=input("Hours: ")
 
 
  secValue = 0
  mValue = 0
  hValue = 0
  while True:
        secValue += 1
        time.sleep(0.9)
        draw(str(secValue),str(mValue),str(hValue))
       
 
        if(sec_alarm==secValue and sec_alarm==secValue and sec_alarm==secValue):
                print "Alarm clock is stoped\n"
                song()
                break
 
 
        if(secValue == 59):
                secValue = 0
                mValue += 1
                if(mValue == 59):
                        mValue = 0
                        hValue += 1
 
                       
 
 
 
 
else:
      print "\nWrong Input.\nOpen the program and try again.\nThank you !!!"
  
