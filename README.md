# CSC591-IOT-PROJECT

## Environment Settings:
This project uses a raspberry pi as well as a JSN-SR04T sensor to measure water levels of a water bottle. FOr this system to work you must have python 3 installed with the required libraries (These can be installed using `pip3 install -r requirements.txt`) as well as the [pigpio](https://abyz.me.uk/rpi/pigpio/index.html) daemon. A wiring diagram for the pi can be found in the final report. In addition, you need to generate an ifttt key to be able to send notifications to a phone

## Running the code:
The code is split into 4 files testing different subsystems of the project:
* Ultrasonic_test.py tests the ultra sonic sensor and outputs the current data from the sensor
* Manual_measurement.py prompts you to measure the output of the sensor data to calculate how much water you have drunk
* Notification_test.py tests sending notifcations using http requests
* Auto_measurement.py automatically measures water dranken based on sensor data and can send reminders to drink water

## Interpreting results
All scripts output results to the console and showcase the capabilities for ther system

## Other information
Originally the design included a web app which was not completed due to time constraints, mockups of this web app can be found in the final report.