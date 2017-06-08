from hal_rest_client import RESTClient
from hal_ws_client import WSClient
from hal_ws_handler import HALWSHandler
from exception import HALException
from constants import *


class HALClient:

    def __init__(self):
        self.rest_client = None

    def _get_rest_client(self):
        if self.rest_client is None:
            self.rest_client = RESTClient()
        return self.rest_client

    def get_list_usb_to_serial_devices(self):
        return self._get_rest_client().get_list_usb_to_serial_devices()

    def get_lscpu_info(self):
        return self._get_rest_client().get_lscpu_info()

    def get_lspci_info(self):
        return self._get_rest_client().get_lspci_info()

    def get_lshw_info(self):
        return self._get_rest_client().get_lshw_info()

    def get_lsusb_info(self):
        return self._get_rest_client().get_lsusb_info()

    def get_proc_cpu_info(self):
        return self._get_rest_client().get_proc_cpu_info()

    @staticmethod
    def connect_to_usb_to_serial(config, usb_to_serial_handler):
        if HAL_USB_TO_SERIAL_PORT_PROPERTY_NAME not in config:
            raise HALException('Port is required to open USB-to-Serial connection.')
        if not isinstance(usb_to_serial_handler, HALWSHandler):
            raise HALException('Provided handler is not instance of HALWSHandler.')
        try:
            ws_client = WSClient(config=config, handler=usb_to_serial_handler)
            ws_client.connect()
            return ws_client
        except Exception as e:
            raise HALException(message=str(e))

