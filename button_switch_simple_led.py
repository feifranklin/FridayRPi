import RPi.GPIO as GPIO
import datetime         # datetime.datetime.now()
import time             # sleep()
buttonPIN = 13 
ledPIN = 7 

#define callback function
def my_callback(pin):
    if GPIO.input(pin) == GPIO.HIGH:
        print "Push down at\t", str(datetime.datetime.now())
        GPIO.output(ledPIN, True)
    else:
        print "Push up at\t", str(datetime.datetime.now())
        GPIO.output(ledPIN, False)

#m main function
try: 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #GPIO.setup(buttonPIN, GPIO.IN)
    GPIO.setup(ledPIN, GPIO.OUT)
    GPIO.add_event_detect(buttonPIN, GPIO.BOTH, callback=my_callback)
    print "press swtich button"
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print "exit"
    GPIO.cleanup()


print "done"


