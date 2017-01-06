import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

# turn on pin #7
GPIO.output(7, True)

# pause 5 seconds
time.sleep(5)

# turn off pin #7
GPIO.output(7, False)


# must clean up
GPIO.cleanup()

print("done")
