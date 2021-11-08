#!/usr/bin/env python3

import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()
sendBuf=b'\xA0\x03\x01\x72\xE0'
RecvBuf=[]
sendFlag=False

def start_connections(host, port):
    server_addr = (host, port)
    print("starting connection to ",  server_addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    data = types.SimpleNamespace(
            outb=b"",
    )
    sel.register(sock, events,data=data)


def service_connection(key, mask):

    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print("received", repr(recv_data) )
            if recv_data[0]==0xA0 and recv_data[recv_data[1]+1]==0xE0 and recv_data[3]==0x72:
                print("Firmware version is ", repr(recv_data[4]),".", repr(recv_data[5]) )
                print("closing connection")
                sel.unregister(sock)
                sock.close()

        elif not recv_data:
            print("closing connection")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        global sendFlag
        if sendFlag==True:      
            data.outb = sendBuf
            print("sending", repr(data.outb), "to connection", host, port)
            sent = sock.send(data.outb)  # Should be ready to write
            sendFlag=False


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port> ")
    sys.exit(1)

host, port = sys.argv[1:3]


while True:
    try:
        while(input("Please input 'version' to send:")!='version' ):
            pass
        start_connections(host, int(port))
        sendFlag=True
        while True:
            events = sel.select(timeout=1)
            if events:
                for key, mask in events:
                    service_connection(key, mask)
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
        sys.exit(1)
    finally:
        sel.close()
