from mcpi.minecraft import Minecraft
from picamera import PiCamera
from time import sleep

mc = Minecraft.create()
camera = PiCamera()

mc.postToChat("Hello world")
