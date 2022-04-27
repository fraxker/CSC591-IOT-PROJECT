from gpiozero import DistanceSensor, Device
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from math import pi, pow

if __name__ == "__main__":
    Device.pin_factory = PiGPIOFactory()
    
    sensor = DistanceSensor(23, 24, queue_len=50, threshold_distance=0.05)
    values = []

    while True:
        meters = sensor.distance
        cm = meters * 100
        print( cm, "cm")
        sleep(.5)
