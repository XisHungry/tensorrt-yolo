import serial
with serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1) as ser:
	while True:
		try:
			line = ser.readline().decode('ascii', errors = 'replace')
			lines = line.split(",")
			if lines[0] == "$GPRMC":
				text_file = open("GPS.txt", "w")
				text_file.write("Latitude=" + lines[3] + "," + "Longitude=" + lines[5])
				text_file.close()
		except KeyboardInterrupt:
			ser.close()
				
