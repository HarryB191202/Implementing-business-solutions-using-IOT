# Testing Results

## Overview
This section outlines the testing results for the network and IoT devices installed and configured as per the project specifications. Each test is detailed with outcomes, issues, and resolutions.

---

## Network Connectivity
### Connectivity Test Results
| **Source Device** | **Destination Device** | **Source IP** | **Destination IP** | **Ping Result** | **Performance Requirements** | **Requirements Met (Y/N)** |
|-------------------|-------------------------|----------------|---------------------|------------------|-----------------------------|--------------------------|
| PC               | Server                 | 192.168.1.10   | 192.168.1.128      | Success          | 4 packets transmitted successfully, each under 25ms | Y                        |
| PC               | Raspberry Pi           | 192.168.1.10   | 192.168.137.22     | Success          | Stable internet connectivity; < 25ms | Y |

**Screen Capture Placeholder:**
- ![Ping Test](https://imgur.com/P0dp27t)

---

## IoT Device Connectivity

### Results and Issues
| **IoT Device**               | **Test Performed**                  | **Test Result** | **Description of Result**                                                                                                 | **Mitigation (if any)**                           |
|-------------------------------|-------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Raspberry Pi                 | Stressberry test for heat dissipation | FAIL            | Temperature exceeded nominal 50°C.                                                | Improved ventilation and added cooling fan. |
| Raspberry Pi                 | PiDoctor SD card test               | PASS            | SD card healthy and operational.                                                                                         | N/A                                               |
| PIR Motion Sensor & Camera   | Motion sensor and video recording   | PASS            | Detected motion; video recorded and saved to Cloud Server.                                                              | N/A                                               |
| Temperature & Humidity Sensor | Systemd journal storage             | PASS            | Data stored successfully; service enabled on boot.                                                                      | N/A                                               |
| Fingerprint Sensor           | Authentication                      | PASS            | Successfully enrolled and authenticated fingerprints.                                                                    | N/A                                               |

**Screen Captures:**
- ![Stressberry Result](https://i.imgur.com/xqaQOpU.png)
- ![Systemd Journal Data](https://i.imgur.com/5pYJ3U4.png)
- ![Fingerprint Authentication](https://i.imgur.com/wJFYWrl.png)

---

## Observations and Recommendations
1. **System Upgrades:**
    - **OS Upgrade:** Update Raspberry Pi to the latest OS (Bullseye 32-bit) using `sudo apt update && sudo apt full-upgrade`.
    - **Software Packages:** Install Python libraries, network tools, and database management systems as needed.
2. **Enhancing Functionality:**
    - Integrate fingerprint sensor with a time and attendance system.
    - Secure biometric data storage to comply with GDPR.

---
