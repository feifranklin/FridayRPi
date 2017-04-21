import RPi.GPIO as GPIO
import datetime         # datetime.datetime.now()
import time             # sleep()
buttonPIN = 13 

#define callback function
def my_callback(pin):
    if GPIO.input(pin) == GPIO.HIGH:
        print "UP at ", str(datetime.datetime.now())
    else:
        print "DOWN at ", str(datetime.datetime.now())

#m main function
try: 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(buttonPIN, GPIO.BOTH, callback=my_callback)
    message = raw_input("press any key to exit")
finally:
    GPIO.cleanup()


print "done"


