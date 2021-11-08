import serial
import sys
sendBuf=b'\xA0\x03\x01\x72\xE0'
ser=serial.Serial('COM5',115200)

while True:
    try:
        recvBuf=bytearray(b'')
        if not ser.is_open:
            ser.open()
        while(input("Please input 'version' to send:")!='version' ):
            pass
        ser.write(sendBuf)
        recvBuf+=ser.read(size=2)
        if recvBuf[0]==0xA0 :
            recvBuf+=ser.read(size=recvBuf[1])
            if recvBuf[recvBuf[1]+1]==0xE0 and recvBuf[3]==0x72:
                 print("Firmware version is ", repr(recvBuf[4]),".",
                           repr(recvBuf[5]) )
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
        sys.exit(1)
    finally:
        print("exit finally")
        ser.close()