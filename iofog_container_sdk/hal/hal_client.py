from hal_rest_client import RESTClient
from hal_ws_client import WSClient
from hal_ws_handler import HALWSHandler
from constants import *


class HALClient:

    def __init__(self):
        self.rest_client = None

    def _get_rest_client(self):
        if self.rest_client is None:
            self.rest_client = RESTClient()
        return self.rest_client

    def get_list_usb_to_serial_devices(self):
        try:
            return self._get_rest_client().get_list_usb_to_serial_devices()
        except Exception as e:
            self._handle_exception_(e, 'Error retrieving list of USB to Serial devices')
            return None

    def connect_to_usb_to_serial(self, config, usb_to_serial_handler):
        if HAL_USB_TO_SERIAL_PORT_PROPERTY_NAME not in config:
            print('Port is required to open for USB to Serial.')
            return
        if not isinstance(usb_to_serial_handler, HALWSHandler):
            print('Provided handler is not instance of HALWSHandler.')
            return
        try:
            ws_client = WSClient(config=config, handler=usb_to_serial_handler)
            ws_client.connect()
            return ws_client
        except Exception as e:
            self._handle_exception_(e, 'USB to Serial error')

    @staticmethod
    def _handle_exception_(ex, msg):
        print((msg + ': %s') % str(ex))
