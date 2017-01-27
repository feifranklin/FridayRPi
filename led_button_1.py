# import the GPIO module
import RPi.GPIO as GPIO

# use board pin naming convention
GPIO.setmode(GPIO.BOARD)

# define PIN
inputPIN = 11
outputPIN = 7

# pull down resistor
GPIO.setup(inputPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# setup pin 7 to output - control LED
GPIO.setup(outputPIN, GPIO.OUT)

# intialize pin 7 state as low
GPIO.output(outputPIN, 0)

try: 
    while True:
        if (GPIO.input(inputPIN) == 1):
            GPIO.output(outputPIN, 1)
        else:
            GPIO.output(outputPIN, 0)
except KeyboardInterrupt:
    GPIO.cleanup()
