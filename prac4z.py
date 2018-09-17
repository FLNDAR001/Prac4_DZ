#!/usr/bin/python
import os
import sys
import RPi.GPIO as GPIO
import spidev
import time

spi = spidev.SpiDev() # create spi object
spi.open(0,0)
spi.max_speed_hz = 1000000

GPIO.setmode(GPIO.BCM)
switch_1 = 23
switch_2 = 22
switch_3 = 27
switch_4 = 17
switch_5 = 23


#GPIO setup
GPIO.setup(switch_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#Interrupts
GPIO.add_event_detect(switch_1,GPIO.FALLING,callback=callback1)
GPIO.add_event_detect(switch_2,GPIO.FALLING,callback=callback2)
GPIO.add_event_detect(switch_3,GPIO.FALLING,callback=callback3)
GPIO.add_event_detect(switch_4,GPIO.FALLING,callback=callback4)
