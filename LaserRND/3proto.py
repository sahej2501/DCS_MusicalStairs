import RPi.GPIO as GPIO
import time
import vlc


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#creating a new vlc instance
player = vlc.Instance()
player2 = vlc.Instance()  
# creating a new media list
media_list = player.media_list_new()
media_list2 = player.media_list_new()
# creating a media player object
media_player = player.media_list_player_new()
 
# creating a new media
step1 = player.media_new("piano_import_C.mp3")
step2 = player2.media_new("piano_import_F.mp3")  
# adding media to media list
media_list.add_media(step1)
media_list.add_media(step2)  
# setting media list to the mediaplayer
media_player.set_media_list(media_list)
  
# setting loop
player.vlm_set_loop("step1", True)


#define the pin that goes to the circuit
pin_to_circuit = 10

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
