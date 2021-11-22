# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:55:40 2021

@author: JordanSchlak
"""

import RPi.GPIO as GPIO
import time
import vlc


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin1 = 36


start_time = time.time()

time1 = start_time

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
        if(count > 1000):
          return count

    return count

while True:
    
    pin1_val = rc_time(pin1)
    print('low')
    player = vlc.MediaPlayer("piano_import_C.mp3")
    player.play()
    time1 = time.time()
    
    
    