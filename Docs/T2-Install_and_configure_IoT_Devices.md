# Project Task 2: Install and Configure IOT Devices

# Task 1: Install required networks

### 1.  Install the networks according to the specifications provided.

  -----------------------------------------------------------------------
  **Parameters**
 
  Wi-Fi                               1

  Protocol                            IPv4

  IPv4 address - PC                   192.168.1.10

  Connect PC to Cloud Server          VMnet8
  -----------------------------------------------------------------------

**Provide [four]{.underline} screenshots showing the configurations.**

-   **Network Properties -- showing Protocol configured**

![Protocol configured](https://imgur.com/tbIhAKf.png)



-   **Network Properties -- showing IPV4 Address Configured**

![Imgur](https://imgur.com/VjfnsKU.png)
![Imgur](https://imgur.com/OycGKN2.png)



-   **Network Status -- VMnet8 connectivity**
  
![Imgur](https://imgur.com/p6jUAGY.png)



-   **Network Status -- PC connected to Cloud Server**

![Imgur](https://imgur.com/sRrJeWJ.png)



# Task 2: Connect and Configure IoT devices and Sensors to the network

Everything_IoT has purchased IoT devices and sensors to meet their
organisation needs. You have been asked to install and configure these
devices and sensors according to the specifications they have provided.

Raspberry Pi with the following:

### PIR Motion Sensor and the Camera Module

These will be used to monitor the security to their Storeroom. The device will be installed on the main entrance so when employees access the storeroom, the sensor will detect motion, video recording, and save it to Cloud Server

### Temperature and Humidity Sensor

This will be installed in the server room to measure the temperature and humidity ratio to keep it to the optimum level. The temperature should not exceed the recommended guidelines of between 65- and 75-degrees Fahrenheit (18- to 24-degrees Celsius). The humidity should not exceed the recommended guidelines of between 40 percent and 60 percent. The organisation would like to make sure that temperature and
humidity is always at the optimum level hence they would like temperature and humidity to be read at intervals of ½ minute.

### Fingerprint Sensor

To record attendance at Senior Leaders monthly meetings held every Monday between 4.00pm -- 5.00pm



### Initial Configuration

### 1. **Connect the Raspberry Pi and the Sensors to the network** 

  ![Imgur](https://imgur.com/8LCsm9S.png)



### 2. **Configure the Raspberry Pi as following:**

-   **Set Locale and set the country to Australia. Provide a
    screenshot.**

    ![Imgur](https://imgur.com/mgvQdbw.png)


    
-   **Set the Time zone to Australia/Adelaide. Provide a screenshot**.

    ![Imgur](https://imgur.com/fNoEbBL.png)



-   **Set Password for the default user (pi) to: ICT501. Provide a
    screenshot.**

    ![Imgur](https://imgur.com/3rauKUC.png)



-   **Create two new users. Provide a screenshot showing the users have
    been created**

    -   **Username: UserPi1; Password: Pi501**
    -   **Username: UserPi2; Password: Pi502**
 
      ![Imgur](https://imgur.com/y8znCaj.png)


    
-   **SSH: enabled. Provide a screenshot.**
  ![Imgur](https://imgur.com/CAkP2rF.png)



-   **Configure Wi-Fi. Provide a screenshot showing Wi-Fi
    connectivity!**

Wifi country code:

![Imgur](https://imgur.com/d6jmU5p.png)



Wifi connectivity success:

![Imgur](https://imgur.com/SE6qGWb.png)



### Configure the Sensors as following:

- **Raspberry Pi GPIO Sensing: Motion Detection and Recording video with Python code.** 

- **The sensor is to detect motion when a person is entering through a door.** 

  ### To demonstrate that Sensor and Wi-Fi camera is operational, provide the following:

    -   **A snippet of the programming script**
    
```
import os
from picamera import PiCamera  # Use PiCamera from picamera module
import RPi.GPIO as GPIO
from datetime import datetime, timedelta
from time import sleep

# Setup the directory for saving video recordings
recording_directory = "/home/harrypi/ICTIOT_Camera_Recording"
if not os.path.exists(recording_directory):
    os.makedirs(recording_directory)

# Setup GPIO for motion detection
GPIO.setmode(GPIO.BCM)
PIR_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)

# Initialize the camera
picam = PiCamera()
picam.resolution = (1920, 1080)  # Set camera resolution
picam.framerate = 30  # Set video framerate
```

  You can find the entirety of the programming script [Here](Implementing-business-solutions-using-IOT/Code/MotionCaptureVideo.py)


-   **A screenshot showing data recording has been saved to Cloud Server
    in the ICTIOT_Camera Recording folder with the filename
    ICTIOT_Video**

    ![Imgur](https://imgur.com/oqy2d3B.png)

- **CLI while code is being ran demonstrating that the .h264 files are
saved to the given directory:**

  - Files uploaded to the Cloud server:
    ![Imgur](https://imgur.com/118mk5U.png)


-   **File: ICTIOT_Video. Links to the video Below (Videos have been converted to mp4 to assist with viewing):**
    - [Video 1](Docs/ICTIOT_Video_20240620_124401.mp4)
    - [Video 2](Docs/ICTIOT_Video_20240620_124542.mp4)

  ### Monitor the temperature and humidity with Raspberry Pi using Prometheus

  - Import Gauge and start_http_server from prometheus_client
  - Determine the read interval for the temperature and humidity
  - Create the gauges to store the humidity and temperature data
  - Create a formula to determine the temperature
  - Initialise with both Celsius and Fahrenheit values
  - Configure the Python logger to send logs to the systemd journal 
  - Start the Prometheus metrics server to display the metrics data

  ###  To demonstrate that temperature and humidity Sensor is operational, provide the following:
  
  - **A Snppet of the Programming Script:**


```
#!/usr/bin/env python3
 
import logging
import time
 
import Adafruit_DHT
 
from prometheus_client import Gauge, start_http_server
from systemd.journal import JournalHandler
 
# Setup logging to the Systemd Journal
log = logging.getLogger('dht22_sensor')
log.addHandler(JournalHandler())
log.setLevel(logging.INFO)
 
# Initialize the DHT22 sensor
# Read data from GPIO4 pin on the Raspberry Pi
SENSOR = Adafruit_DHT.DHT22
SENSOR_PIN = 4
 
# The time in seconds between sensor reads
READ_INTERVAL = 30.0
 
# Create Prometheus gauges for humidity and temperature in
# Celsius and Fahrenheit
gh = Gauge('dht22_humidity_percent',
          'Humidity percentage measured by the DHT22 Sensor')
gt = Gauge('dht22_temperature',
          'Temperature measured by the DHT22 Sensor', ['scale'])
```

You can find the entirety of the programming script [Here](Implementing-business-solutions-using-IOT/Code/sensor-metrics2.py)


### **Check the metrics target by analysing and providing:**

  ### 1. **A screen capture showing temperature and humidity metrics**
  ![Imgur](https://imgur.com/R6mNRko.png)



  ### 2. **The query used to get the temperature and humidity data:**
  ![Imgur](https://imgur.com/NR4L7gS.png)



  ### 3. **Prometheus loaded in the cli (top), the code being ran with the sensor metrics being served (left) and the Prometheus web gui (right):**
  ![Imgur](https://imgur.com/GkLt9PK.png)


  ### 4. **The raw DHT Humidity and temperature data at localhost:8000:**
  ![Imgur](https://imgur.com/AcmBAol.png)
    


### Interfacing Fingerprint Sensor with Raspberry Pi

### Configure the sensor (Preparation)

  - Baud rate: 9600

  - Fingerprint imaging time: 1.0s

  - False Acceptance Rate: 0.001% (Security Level 3)

  - False Reject Rate: 1.0% (Security level 3)

  - Install drivers and Fingerprint library



### Enrol Fingerprint:

  - Initialise the Fingerprint Sensor

  - Enrol new finger

  - Store it in charbuffer as an image

  - Fingerprint is checked for a match with the existing print

  - Error: enrol new finger again

  - Store it in charbuffer as an image

  - Fingerprint is checked for a match with the existing print

  - Download Fingerprint Image

  - download the image of the fingerprint which has been captured by the sensor.



  ### To demonstrate that fingerprint Sensor is operational, provide the following:

  ### 1. **A snippet of the Programming Script**
  
```

def get_fingerprint():
    """Get a finger print image, template it, and see if it matches!"""
    print("Waiting for image...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Templating...")
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
    print("Searching...")
    if finger.finger_search() != adafruit_fingerprint.OK:
        return False
    return True


# pylint: disable=too-many-branches
def get_fingerprint_detail():
    """Get a finger print image, template it, and see if it matches!
    This time, print out each error instead of just returning on failure"""
    print("Getting image...", end="")
    i = finger.get_image()
    if i == adafruit_fingerprint.OK:
        print("Image taken")
    else:
        if i == adafruit_fingerprint.NOFINGER:
            print("No finger detected")
        elif i == adafruit_fingerprint.IMAGEFAIL:
            print("Imaging error")
        else:
            print("Other error")
        return False

```
You can find the entirety of the programming script [Here](Implementing-business-solutions-using-IOT/Code/fingerprint_simpletest.py)


### 2. **Enrol Fingerprint**

  - The menu upon running the code:
  ![Imgur](https://imgur.com/qCLlDlW.png)



  - Fingerprint with ID #3 being enrolled, and then located using find print
  option, confidence is 157, fingerprint #3 located successfully:
  ![Imgur](https://imgur.com/NTFTBoc.png)


### 3. A screen capture of the following:

  - **Downloading Fingerprint Image**
    ![Imgur](https://imgur.com/hXtnUP9.png)



  - **Fingerprint image saved to /tmp/fingerprint.bmp:**
    ![Imgur](https://imgur.com/GJinbgs.png)

    

  - **Directory of fingerprint.bmp shown, alongside the actual fingerprint
    image, and the cli confirming that the image was saved:**
    ![Imgur](https://imgur.com/L7Gisqz.png)



# Task 3: Test connectivity

After the devices have been installed and configured you are required to
verify full functionality by testing the network and the IoT devices
against the specifications provided by the organisation 

To view task three, please refer to the Testing_Results.MD file, or click [Here](Implementing-business-solutions-using-IOT/Docs/Testing_Results.md)
