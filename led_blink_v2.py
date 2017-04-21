import RPi.GPIO as GPIO
import time
pinID=7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # if BOARD, pin is 7
#GPIO.setmode(GPIO.BCM) # if BCM, pin is GPIO 4 
GPIO.setup(pinID, GPIO.OUT)

def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(.5)
    if (GPIO.input(pin)):
        print("LED is about to switch off")
    GPIO.output(pin, GPIO.LOW)
    time.sleep(.5)
    if not GPIO.input(pin):
        print("LED is about to switch on")
        
    return # optional

try:
    for i in range(100):
        print("loop: ", i)
        blink(pinID)
except KeyboardInterrupt:
    GPIO.cleanup()
    print "user interrupt"
    
# must clean up
GPIO.cleanup()
print "clean up"
