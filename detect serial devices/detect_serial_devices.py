# you need to install pyserial 
# you can install it using this comman (pip install pyserial)

# this functions i used in django while working in web application that configure and monitor devices via wifi and usb

import serial.tools.list_ports

# this function to detect which com u connected the usb device
def get_usb_devices():
    ports = serial.tools.list_ports.comports()
    portsList = []
    for onePort in ports:
        portsList.append(str(onePort))
    if(len(portsList)==0):
        print("no serial port available")
        return portsList
    else:
        for x in range(0,len(portsList)):
            # to detect com3,com4, ..., com14,... 
            comName=portsList[x]
            if comName[4]!=' ':
                comName=comName[:5]
            else :
                comName=comName[:4]
            ser=serial.Serial(comName,baudrate=115200)# you can use some options like baudrate, timeout, ...
            msg=ser.readline() # to read serial data
            
        return msg
# this function to open the serial connection to read and write in it
def write_data_to_usb(com,data):
    ser=serial.Serial(com,baudrate=9600,timeout=5)
    ser.write(data.encode("Hex")) # you can choose anotehr encoding to write to serial
    rec=ser.read() # read serial data
    ser.close() # 
    if(rec=="") :
        rec="sry there is something wrong"
    return rec