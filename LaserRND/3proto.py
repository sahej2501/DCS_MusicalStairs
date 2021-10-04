import RPi.GPIO as GPIO
import time
import vlc


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin_to_circuit = 10


#fuction makes vlc instances for each step
def vlc_instance( fname):
    player = vlc.Instance()
    media_list = player.media_list_new()
    media_player = player.media_list_player_new()
    step = player.media_new(fname)
    media_list.add_media(step)
    media_player.set_media_list(media_list)
    player.vlm_set_loop("step", True)
 

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

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
       if(rc_time(pin_to_circuit) > 500):
           print("Detecting")
           media_player.play()
           time.sleep(0.7)
       else: 
           print("NOT") 
      # print(rc_time(pin_to_circuit))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup
