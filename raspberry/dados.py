import serial
import time
ser = serial.Serial('/dev/ttyACM0',9600)


def leSensor(sensor):
    if ser.is_open :
        ser.write(str(sensor))
        read_serial = ""
        while read_serial == "":
            read_serial=ser.readline()
            print read_serial
            
    return read_serial
