# Teensy Potentiometer Mouse Control

## Overview
This project allows you to control mouse movements or generate beep sounds using an Arduino and three potentiometers. The potentiometers are connected to the Arduino, which reads their values and sends them to a Python script via serial communication. The Python script uses **PyAutoGUI** or an alternative library to perform actions based on the potentiometer values.

## Components Required
- Arduino board (e.g., Arduino Uno) or Teensy 4.1
- 3 Potentiometers
- Jumper wires
- Breadboard (optional)
- USB cable to connect Arduino to the computer

## Setup Instructions

### Hardware Connections
1. Connect the three potentiometers to the Arduino:
   - Potentiometer 1: Connect the middle pin to **A0**, one side pin to **GND**, and the other side pin to **3.3V**.
   - Potentiometer 2: Connect the middle pin to **A1**, one side pin to **GND**, and the other side pin to **3.3V**.
   - Potentiometer 3: Connect the middle pin to **A2**, one side pin to **GND**, and the other side pin to **3.3V**.

### Python Script
Install the required libraries if you haven't already:
```bash
pip install pyautogui
```

## Usage
1. Connect the Arduino to your computer via USB.
2. Upload the Arduino code to the board.
3. Run the Python script. Adjust the potentiometers to control the mouse movement or generate beeps.

## Troubleshooting
- Ensure the correct serial port is specified in the Python script.
- Check the connections of the potentiometers.
- If using **PyAutoGUI**, ensure you have the necessary permissions to control the mouse.

---

Feel free to modify any sections to better fit your project specifics or add any additional information that may be relevant!
