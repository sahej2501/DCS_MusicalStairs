# -*- coding: utf-8 -*-
import logging
import threading
import vlc
import RPi.GPIO as GPIO
import time
def play_audio(pin):
    media_player = vlc.MediaPlayer()
    media_player.set_mrl("input/{}.mp3".format(pin))
    media_player.play()
    time.sleep(1)
    media_player.stop()
    
pins_list = [10, 36]
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# time sensitivity
iter_timer = 1
# set to 0 if prod
global_timer = 0
def trip_wire(pins_list):
    
    start_time = time.time()
    
    iter_time = start_time
    glob_time = start_time
    
    while True:
        
        try:
            for pin in pins_list:
                #print('start loop for pin {}'.format(pin))
                count = 0
              
                #Output on the pin for 
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)
                time.sleep(0.1)
                #Change the pin back to input
                GPIO.setup(pin, GPIO.IN)
              
                #Count until the pin goes high
            
                while (GPIO.input(pin) == GPIO.LOW):
                    #print(count)
                    count += 1
                    
                    # exit in dark lighting conditions
                    if count > 10000:
                        #print('exiting loop because it\'s too dark')
                        break
                
                print(count)
                # if 
                if (count) > 500 and (time.time() - iter_time > 1):
                    
                    print('playing audio on pin: {}'.format(pin))
                    #play_audio(pin)
                    
                    x = threading.Thread(target=play_audio, args=(pin,))
                    x.start()
                    
                    iter_time = time.time()
                        
                if time.time() - glob_time > global_timer and global_timer != 0:
                    print('exiting on global timeout: {}'.format(str(global_timer)))
                    return
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    
    print('beginning program')
    
    '''
    for pin in pins_list:
        x = threading.Thread(target=trip_wire, args=(pin,))
        x.start()
    '''
    
    # test function without threading 
    trip_wire(pins_list)