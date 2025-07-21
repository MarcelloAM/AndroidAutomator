import uiautomator2 as u2
import adbutils as a2
import time
from packaging.licenses import EXCEPTIONS
from ppadb.client import Client as AdbClient
import xml.etree.ElementTree as ET

from uiautomator2 import XPathElementNotFoundError


class Android:
    client = AdbClient(host='127.0.0.1', port=5037)

    def __init__(self, deviceid: str):
        self.deviceid = deviceid
        self.d = u2.connect(self.deviceid)
        self.a = a2.AdbClient(self.deviceid)

    def unlock_screen(self):
        return  self.d.keyevent('wakeup')

    def quick_panel(self):
        return self.d.open_quick_settings()

    def wait(self, number: int):
        return time.sleep(number)

    def settings_cell(self):
        return self.d.shell('am start -n com.android.settings/.Settings')

    def open_app(self, application: str):
        return self.d.app_start(f'{application}')

    def search(self):
        self.d.keyevent('search')

    def input_text(self, text: str):
        self.d.shell(f'input text "{text}"')

    def click_by_text(self, text: str):
        self.d.xpath(f'//*[@text="{text}"').click()

    def click_by_resource_id(self, resource_id: str):
        self.d.xpath(f'{resource_id}').click()

    def click_by_position(self, x, y):
        return self.d.click(x, y)

    def swipe_up(self):
        self.d.swipe(0.1    , 0.9, 0.9, 0.1)

    def close_all_apps(self):
        self.d.keyevent('app_switch')
        time.sleep(2)
        try:
            self.click_by_resource_id('com.sec.android.app.launcher:id/clear_all')
        except XPathElementNotFoundError:
            pass

        return 0
