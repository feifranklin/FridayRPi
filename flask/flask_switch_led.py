import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
     7  : {'name' : 'led 1', 'state' : GPIO.LOW},
    12 : {'name' : 'led 2', 'state' : GPIO.LOW},
    16 : {'name' : 'led 3', 'state' : GPIO.LOW}   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)


# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."
   if action == "toggle":
      # Read the pin and set it to whatever it isn't (that is, toggle it):
      GPIO.output(changePin, not GPIO.input(changePin))
      message = "Toggled " + deviceName + "."
 # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'message' : message,
      'pins' : pins
   }
   return render_template('main.html', **templateData)

# @app.route("/<puissance>")
# def puissance(puissance):
# # For each pin, read the pin state and store it in the pins dictionary:   
#    for pin in pins:
#       pins[pin]['state'] = GPIO.input(pin)
#       LED = GPIO.PWM(pin, 50)
#       LED.start(0)
#       LED.ChangeDutyCycle(int(puissance))
#       time.sleep(5)
#    # Put the pin dictionary into the template data dictionary:
#  templateData = {
#       'pins' : pins
#       }
#    return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8088, debug=True)


