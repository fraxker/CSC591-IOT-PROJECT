from gpiozero import DistanceSensor, Device
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from math import pi, pow
import yaml
import requests

if __name__ == "__main__":
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    key = config["key"]
    Device.pin_factory = PiGPIOFactory()
    
    sensor = DistanceSensor(23, 24, queue_len=50, threshold_distance=0.05)
    values = []
    still_cnt = 0
    old_cm = sensor.distance * 100

    while True:
        cm = sensor.distance * 100
        if cm < 21:
            continue

        if abs(old_cm - cm) < .1:
            still_cnt += 1

        if still_cnt >= 10:
            cm_diff = cm - old_cm
            if cm_diff > 0:
                oz = pow(1.75, 2) * pi * cm_diff / 2.54 * 0.554
                print(f"You drank {oz} oz")
                still_cnt = 0
                old_cm = cm
                

        if still_cnt >= 100:
            requests.post(f"https://maker.ifttt.com/trigger/Water_Bottle_Notification/with/key/{key}", json={"value1": "Please drink some water"})
            still_cnt = 0
        
        sleep(.5)
