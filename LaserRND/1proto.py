import RPi.GPIO as GPIO
import time
import vlc
#from playsound import playsound

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sound1 =vlc.MediaPlayer("piano_import_C.mp3")

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
       if(rc_time(pin_to_circuit) < 500):
           print("Detecting")
           sound1.play()
       else: 
           print("NOT") 
      # print(rc_time(pin_to_circuit))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup
