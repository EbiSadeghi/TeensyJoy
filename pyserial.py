import serial
import time
import pyautogui
pyautogui.FAILSAFE = False

# Open Serial Port
ser = serial.Serial('/dev/ttyACM0', 9600)  # Change 'COM3' to your Arduino port
time.sleep(2)  # Wait for the connection to establish

# define the static potentiometer readings
center_pot1 = 487
center_pot2 = 552
center_pot3 = 480
noise_margin = 30
debug = True

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if debug:
            print(line)
        potValues = line.split(",")
        
        if len(potValues) == 3:
            # Convert to integers
            pot1 = int(potValues[0])
            pot2 = int(potValues[1])
            pot3 = int(potValues[2])

            # Example actions based on potentiometer values
            # Map potentiometer values to mouse movement
            # Assuming pot1 controls X-axis and pot2 controls Y-axis
            error_1 = pot1 - center_pot1
            error_2 = pot2 - center_pot2
            
            x_move = 0
            y_move = 0
            if abs(error_1) > noise_margin:
                x_move = error_1 * 0.1  # Scale down the movement
                print(f"x_move: {x_move}")
            if abs(error_2) > noise_margin:
                y_move = error_2 * 0.1  # Scale down the movement
                print(f"y_move: {y_move}")
            # theta_move = pot3 * 0.1 
            
            # Move the mouse
            pyautogui.moveRel(int(x_move),int(y_move))  # Move mouse relative to current position
            
            # Example: Use pot3 to control a key press
            # if pot3 > 600:  # If pot3 is above a certain threshold
            #    pyautogui.hotkey('ctrl', '+')  # Zoom in
            # elif pot3 < 200:  # If pot3 is below a certain threshold, zoom out
            #    pyautogui.hotkey('ctrl', '-')  # Zoom out

ser.close()

