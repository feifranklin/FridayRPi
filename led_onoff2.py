import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

GPIO.output(7, True)
time.sleep(10)
# turn off pin #7
GPIO.output(7, False)


# must clean up
GPIO.cleanup()
