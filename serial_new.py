import serial
from threading import Timer

ser = serial.Serial('COM3', 9600, timeout=1)
voltage_est = 18
current_est = 3

def read_data():
    try:
        # Read values from serial port

        line = ser.readline().decode().strip()
        voltage = 0
        current = 0
        if line != '':
            # print(line.split(','))
            splitted = line.split(',')
            if len(splitted) == 2:
                # print("Voltage:", splitted[0])
                voltage = float(splitted[0])
                if splitted[1] != '':
                    # print("Current:", splitted[1])
                    current = float(splitted[1])
            elif len(splitted) == 1 :
                # print("Current:", splitted[0])
                    current = float(splitted[0])
                        
        # print(voltage, current)
        # Extract voltage and current values
        # voltage = ser.readline().decode().strip()
        # current = ser.readline().decode().strip()

        # # Calculate voltage and current ratios
        # v_ratio = voltage / voltage_est
        # i_ratio = current / current_est

        # # Do some mathematical operations using the ratios
        # power = v_ratio * i_ratio
        # resistance = voltage / current

        # Print the results
        print("Voltage: " + str(voltage) +  "V" +  " Current: " + str(current) + "mA")
        # print(f"Power: {power:.2f} W, Resistance: {resistance:.2f} Ohms")

       

    except KeyboardInterrupt:
        # Close the serial port on interrupt
        ser.close()

while True:
    
    read_data()
