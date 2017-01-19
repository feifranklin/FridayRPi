# Import all the libraries we need to run
import sys
import os
import Adafruit_DHT
import urllib2
import RPi.GPIO as GPIO
from time import sleep

# Setup the pin we connect to
DHTpin = 4

#Setup our API and delay
myAPI = "insert_here_your_thingspeak_channel_key"
myDelay = 5 #how many seconds between posting data

def getSensorData():
    RHW, TW = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)

    #Convert from Celius to Farenheit
    TWF = 9/5*TW+32

    # return dict
    return (str(RHW), str(TW),str(TWF))

# main() function
def main():
    print 'starting...'
    #baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    #print baseURL

    while True:
        try:
            RHW, TW, TWF = getSensorData()
            #f = urllib2.urlopen(baseURL +"&field1=%s&field2=%s&field3=%s" % (TW, TWF, RHW))
            #print f.read()
            print "tempC " + TW + ", tempF " + TWF+ ", humidity " + RHW
            #f.close()

            sleep(int(myDelay))
        except KeyboardInterrupt:
            GPIO.cleanup()
            print "catch keyboard interrupt"
        except:
            print 'exiting.'


# call main

if __name__ == "__main__":
    main()
