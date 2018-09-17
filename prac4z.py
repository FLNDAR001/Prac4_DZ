#!/usr/bin/python
import os
import sys
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
switch_1 = 23
switch_2 = 22
switch_3 = 27
switch_4 = 17
switch_5 = 23

# function to read ADC data from a channel
def GetData(channel): # channel must be an integer 0-7
    adc = spi.xfer2([1,(8+channel)<<4,0]) # sending 3 bytes
    data = ((adc[2]&3) << 8) + adc[1]
    return data


# function to convert data to voltage level (ALSO function for pot)
# places: number of decimal places needed
def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,places)
    return volts


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
