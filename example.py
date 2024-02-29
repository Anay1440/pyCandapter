import pyCandapter
import can
import signal

#Port and baudrate for serial communication with the Candapter
PORT = 'COM7'
SERIALBAUDRATE = 9600
CANBAUDRATE = 250000

candapter = pyCandapter.pyCandapter(PORT, SERIALBAUDRATE)
candapter.openCANBus(CANBAUDRATE)

def signal_handler(sig, frame):
    candapter.closeCANBus()
    exit(0) 

signal.signal(signal.SIGINT, signal_handler)

#For receiving
while True:
    message = candapter.readCANMessage()
    if message is not None:
        print(message)

#For sending
message = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)
candapter.sendCANMessage(message)