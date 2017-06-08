# container-sdk-python

HAL module documentation

This module lets you easily work with HAL (Hardware Layer Abstraction) micro-service.

## Code snippets: 

Import hal client and additional classes to your project:
```python
from iofog_container_sdk.hal.hal_client import HALClient
from iofog_container_sdk.hal.hal_ws_handler import HALWSHandler
from iofog_container_sdk.hal.constants import *
from iofog_container_sdk.hal.exception import HALException
```

Create HAL client:
```python
hal_client = HALClient()
```

#### REST calls

```python
try:
    usb_to_serials_list = hal_client.get_list_usb_to_serial_devices()
    lscpu_info = hal_client.get_lscpu_info()
    lspci_info = hal_client.get_lspci_info()
    lsusb_info = hal_client.get_lsusb_info()
    lshw_info = hal_client.get_lshw_info()
    proc_pu_info = hal_client.get_proc_cpu_info()
except HALException as e:
    # some error occurred, e contains description : e.code and e.reason
```
#### WebSocket API

To use websocket connections you should implement listeners as follows:
```python
class HALUSBtoSerialHandler(HALWSHandler):
    def __init__(self):
        return

    def connection_closed(self, code, reason):
        print(' -- WS -- Server Closed Connection: code = {}, reason = {}'.format(code, reason))
        return

    def connection_opened(self):
        print(' -- WS -- Connection Opened') 
        # this method is triggered after connection was established and signal to open connection with provided 
        # configuration to open connection was sent correctly 
        return

    def got_data(self, data):
        print(' -- WS -- Received data HAL: {}'.format(data))
```

Establish connection to USB-to-Serial devicem don't forget to provide config, where PORT property is required, and handler:
```python
handler = HALUSBtoSerialHandler()
config = {HAL_USB_TO_SERIAL_PORT_PROPERTY_NAME: '/dev/ttyUSB0'}
try:
    usb_to_serial_client = hal_client.connect_to_usb_to_serial(config, handler)
    # continue working with socket connection
except HALException as e:
    # some error occurred, e contains description : e.code & e.message
```
Each of those connections will be managed in a separate thread.
  
After successful connection to message websocket, you can check it via 'is_opened' property, you can send data (should 
be provided as bytearray):
```python
if usb_to_serial_client is not None:
    while not usb_to_serial_client.is_opened:
        time.sleep(0.2)
    data = bytearray()
    data.extend('Hello USB to Serial')
    usb_to_serial_client.send_data(data)
```