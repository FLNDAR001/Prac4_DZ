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

def callback1(channel):
    global timer
    timer = 0
    print ("\n" * 100)

#function to convert voltage to temperature
def Temperature (voltage):
    temp = voltage
    temp = int ((temp - 0.5)/0.01 )
    
    return temp

#function to convert voltage to %
def Percent (voltage):
    per = (int (voltage/3.1*100))

    return per

try:
    while 1:
        if(y == True):

            
            sensor_data1 = GetData (channel1)
            pot = ConvertVolts(sensor_data1,2)
            sensor_data2 = GetData (channel2)
            sensor_volt2 = ConvertVolts(sensor_data2,2)
            sensor_data3 = GetData (channel3)
            sensor_volt3 = ConvertVolts(sensor_data3,2)
            temp = Temperature (sensor_volt3)
            light = Percent(sensor_volt2)
            element = (str(time.strftime("%H:%M:%S   ")) + '00:00:' + str(timer)+ "     " + str(pot)+ 'V    ' + str(temp) + 'C     ' + str(light) +'%')
            arr.append(element) 
            print('_______________________________________________')
            print (time.strftime("%H:%M:%S  "),'00:00:' + str(timer),'   ',str(pot)+ 'V   ' , str(temp) + 'C   ', str(light) +'%')
        
        

        # Wait before repeating loop
        time.sleep(delay)
        timer = timer + delay
      
     
        
       
except KeyboardInterrupt:
    spi.close()
