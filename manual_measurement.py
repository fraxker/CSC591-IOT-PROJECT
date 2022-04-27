from gpiozero import DistanceSensor, Device
from gpiozero.pins.pigpio import PiGPIOFactory
from math import pi, pow

if __name__ == "__main__":
    Device.pin_factory = PiGPIOFactory()
    
    sensor = DistanceSensor(23, 24, queue_len=50, threshold_distance=0.05)
    values = []

    input("Press enter to take initial measurement\n")

    initial = sensor.distance

    input("Press enter to take second measurement\n")

    second = sensor.distance

    oz = (second - initial) * 100 * pow(1.75, 2) * pi / 2.54 * 0.554
    print(oz)