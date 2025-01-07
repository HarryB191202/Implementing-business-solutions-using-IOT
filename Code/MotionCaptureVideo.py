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

# Initialize debounce variables
last_motion_time = datetime.now()
motion_detected = False
debounce_timeout = 1  # Debounce timeout in seconds
record_duration = 5  # Duration of each recording in seconds

try:
    while True:
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            if not motion_detected:
                print("Motion detected...")
                motion_detected = True
                
                # Generate timestamped filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                video_filename = os.path.join(recording_directory, f"ICTIOT_Video_{timestamp}.h264")
                
                # Record video for up to 5 seconds
                picam.start_recording(video_filename)
                print(f"Recording video: {video_filename}")
                
                # Set timer for recording duration
                start_time = datetime.now()
                while (datetime.now() - start_time).seconds < record_duration:
                    picam.wait_recording(0.1)
                
                # Stop recording after specified duration
                picam.stop_recording()
                print(f"Saved video: {video_filename}")
        
        else:
            if motion_detected:
                # Motion has stopped
                motion_detected = False
                picam.stop_recording()
                print(f"Saved video: {video_filename}")

        # Debounce logic to avoid false positives
        if (datetime.now() - last_motion_time).seconds > debounce_timeout:
            motion_detected = False

        last_motion_time = datetime.now()

        # Sleep briefly to manage CPU usage
        sleep(2)

finally:
    picam.close()
    GPIO.cleanup()
