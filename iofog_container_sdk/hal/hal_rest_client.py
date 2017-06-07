import json
import urllib2

from constants import *
from iofog_container_sdk.exception import IoFogHttpException


class RESTClient:
    def __init__(self):
        self.base_url = "{}://{}:{}".format(HTTP_PROTOCOL, HOST, HAL_REST_PORT)
        return

    def get_list_usb_to_serial_devices(self):
        return self._make_request_(self.base_url + HAL_USB_TO_SERIAL_GET_LIST_PATH)

    def get_lscpu_info(self):
        return self._make_request_(self.base_url + HAL_HWC_GET_LSCPU_INFO_PATH)

    def get_lspci_info(self):
        return self._make_request_(self.base_url + HAL_HWC_GET_LSPCI_INFO_PATH)

    def get_lshw_info(self):
        return self._make_request_(self.base_url + HAL_HWC_GET_LSHW_INFO_PATH)

    def get_lsusb_info(self):
        return self._make_request_(self.base_url + HAL_HWC_GET_LSUSB_INFO_PATH)

    def get_proc_cpu_info(self):
        return self._make_request_(self.base_url + HAL_HWC_GET_CPU_INFO_PATH)

    @staticmethod
    def _make_request_(url, body=None):
        try:
            if body is None:
                req = urllib2.Request(url)
            else:
                req = urllib2.Request(url, body, {'Content-Type': APPLICATION_JSON})
            response = urllib2.urlopen(req)
            return json.loads(response.read())
        except urllib2.HTTPError as http_e:
            print('HTTP Error: {}'.format(http_e))
            raise IoFogHttpException(http_e.code, http_e.read())
        except Exception as e:
            print('Error: {}'.format(e))
            raise IoFogHttpException(e.code, e.read())
