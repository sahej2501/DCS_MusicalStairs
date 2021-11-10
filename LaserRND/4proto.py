# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:06:21 2021

@author: joebl
"""

import RPi.GPIO as GPIO
import time
import vlc


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin1 = 8
pin2 = 36

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count


'''
pin3 = 10
pin4 = 10
pin5 = 10
pin6 = 10
pin7 = 10
pin8 = 10
'''


start_time = time.time()

time1 = start_time
time2 = start_time

'''
time3 = start_time
time4 = start_time
time5 = start_time
time6 = start_time
time7 = start_time
time8 = start_time
time9 = start_time
'''

while True:
    print('started')
    '''
    pin1_val = rc_time(pin1)
    #print('print1 val: {}'.format(pin1_val))
    
    if (pin1_val) < 1000 and (time.time() - time1 > 1):
        
        print('low')
        player = vlc.MediaPlayer("input/1.wav")
        player.play()
        time1 = time.time()
    '''
    print('getting pin value')
    pin2_val = rc_time(pin2)
    print('got pin value')
    print('print2 val: {}'.format(pin2_val))
    if (pin2_val) < 1000 and (time.time() - time2 > 1):
        
        print('low')
        player = vlc.MediaPlayer("piano_import_C.mp3")
        player.play()
        time2 = time.time()
        
    print()
