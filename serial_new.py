import serial
from threading import Timer

ser = serial.Serial('COM3', 9600, timeout=1)
voltage_est = 18
current_est = 3

def read_data():
    try:
        # Read values from serial port
        line = ser.readline().decode().strip()
        values = line.split(",")

        # Extract voltage and current values
        voltage = ser.readline().decode().strip()
        current = ser.readline().decode().strip()

        # # Calculate voltage and current ratios
        # v_ratio = voltage / voltage_est
        # i_ratio = current / current_est

        # # Do some mathematical operations using the ratios
        # power = v_ratio * i_ratio
        # resistance = voltage / current

        # # Print the results
        print("Voltage: {voltage} V, Current: {current} A")
        # print(f"Power: {power:.2f} W, Resistance: {resistance:.2f} Ohms")

    except KeyboardInterrupt:
        # Close the serial port on interrupt
        ser.close()

while True:
    
    read_data()
