import serial

# establish connection with Arduino
ser = serial.Serial('COM3', 9600, timeout=1)

# set voltage and current estimates
voltage_est = 18
current_est = 3


while True:
    # read data from Arduino
    data = ser.readline().decode().strip()
    # data should be in the format "voltage,current"
    values = data.split(",")
    voltage = float(values[0])
    current = float(values[1])

    print(voltage , current, values)

    # calculate voltage and current ratios
    # vr = voltage / voltage_est
    # ir = current / current_est
    # ocr = 1.01

    # # print the ratios
    # print("Voltage ratio: ", vr)
    # print("Current ratio: ", ir)
    # print("Open ckt ratio: ", ocr)

    # # write the ratios to a file
    # with open('ratios.txt', 'w') as f:
    #     f.write(f"vr: {vr}\n")
    #     f.write(f"ir: {ir}\n")
    #     f.write(f"ocr: {ocr}\n")
