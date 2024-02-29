# pyCandapter
pyCandapter is a Python module for interfacing with the [Candapter](https://www.candapter.com/) USB to CAN adapter. It uses the [pySerial](https://pyserial.readthedocs.io/en/latest/) module to communicate with the Candapter. The [python-can](https://python-can.readthedocs.io/en/stable/) module is used to create and read CAN messages. The module is designed to be used with Python 3.8 and above.
## Usage
<ul>
<li>

Install required modules. 
```bash
pip install pyserial
pip install python-can
```
</li>
<li>

Download the [pyCandapter](./pyCandapter.py) module and place it in the same directory as your Python script.
</li>
<li> 

Import necessary modules.
```python
import pyCandapter
import can
import signal
```
</li>
<li>

Identify the COM port and baud rate of the Candapter. (This can be found through the Device Manager in Windows). Also define the CAN baud rate.
```python
PORT = 'COM7'
SERIALBAUDRATE = 9600
CANBAUDRATE = 250000
```
</li>
<li>

Create a Candapter object and open the CAN bus on the Candapter.
```python
candapter = pyCandapter.pyCandapter(PORT, SERIALBAUDRATE)
candapter.openCANBus(CANBAUDRATE)
```
</li>
<li>

Set up a signal handler to close the CAN bus and serial port when the script is terminated.
```python
def signal_handler(sig, frame):
    candapter.closeCANBus()
    exit(0) 

signal.signal(signal.SIGINT, signal_handler)
```
</li>
<li>

To receive CAN messages, use the following code.
```python
while True:
    message = candapter.readCANMessage()
    if message is not None:
        print(message)
```
The message is a python-can message object. The documentation for the same can be found [here](https://python-can.readthedocs.io/en/stable/message.html).
</li>
<li>

To send a CAN message, use the following code.
```python
message = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)
candapter.sendCANMessage(message)
```
</li>
</ul>

The full file can be found [here](./example.py).

## Known Issues
<ul>
<li>
If the error "Error setting baudrate" appears, it is likely that the previous connection was not closed properly. Disconnect the Candapter and reconnect it, then try again.
</li>
<li>
If the error "SerialException: could not open port 'COMx': PermissionError(13, 'Access is denied.', None, 5)" is encountered, it is likely that the COM port is already open in another application. Close the application and try again.
</li>
<li>
If the error "SerialException: could not open port 'COMx': FileNotFoundError(2, 'The system cannot find the file specified.', None, 2)" is encountered, it is likely that the COM port is not connected to the computer. Connect the Candapter and try again.
</li>
<li>
There is no support for reading extended CAN messages at the moment.
</li>
</ul>