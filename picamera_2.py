from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=200)
sleep(10)

camera.rotation = 90

sleep(10)

camera.rotation = 180

sleep(10)

camera.rotation = 0

camera.stop_preview()


