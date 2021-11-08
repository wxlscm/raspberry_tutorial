import serial
import sys

recvBuf=b''
recvBufindex=0
sendBuf=b'\xA0\x05\x01\x72\x01\x00\xE0'
ser=serial.Serial('/dev/ttyS0',115200)


while True:
    try:
        if not ser.is_open:
            ser.open()
        recvBufindex=0
        recvBuf+=ser.read(size=2)
        recvBufindex+=2
        if recvBuf[0]==0xA0 :
            recvBuf+=ser.read(size=recvBuf[1])
            recvBufindex=0
            if recvBuf[recvBuf[1]+1]==0xE0 and recvBuf[3]==0x72:
                print("received firmware version command!")
                ser.write(sendBuf)
    except KeyboardInterrupt:
        print("caught keyboard interrupt")
        sys.exit(1)
    finally:
        print("exit finally")
        ser.close()







