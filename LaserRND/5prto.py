import RPi.GPIO as GPIO
import time
import vlc
from audioplayer import AudioPlayer

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def playAudio(sound):
    audioplayer.AudioPlayer(sound)
    play(loop=False, block=False)
'''
def createMedia(sound):
    player = vlc.Instance()
  
    # creating a new media list
    media_list = player.media_list_new()

    # ceating a media player object
    media_player = player.media_list_player_new()
  
    # creating a new media
    media = player.media_new(sound)
  
    # adding media to media list
    media_list.add_media(media)
  
    # setting media list to the mediaplayer
    media_player.set_media_list(media_list)
  
    # setting loop
    player.vlm_set_loop("death_note", True)
    
    #play sound
    media_player.play()

    del player, media_list, media_player, media    
'''

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.09)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
        if(count > 250):
          return count

    return count


def main():
    stepInfo = [[36, 0, "piano_import_C.mp3"], [10, 0, "piano_import_F"]]
    try:
        while True:
            for i in range(0,2):
                print(i)
                if rc_time(stepInfo[i][0]) > 200:
                    playAudio(stepInfo[i][2])
                    print("Detecting")
                    time.sleep(0.1)
                else:
                    print("NOT")
#                i = i + 1

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup

main()
