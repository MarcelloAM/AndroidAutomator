import uiautomator2 as u2
import adbutils as a2
import time
from ppadb.client import Client as AdbClient
import xml.etree.ElementTree as ET

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

    def close_apps(self):
        return  self.d.app_stop_all()

    def settings_cell(self):
        return self.d.shell('am start -n com.android.settings/.Settings')

    def open_whats(self):
        self.d.app_start('com.whatsapp')

    def search(self):
        self.d.keyevent('search')

    def input_text(self, text: str):
        self.d.shell(f'input text "{text}"')

    def click_by_text(self, text: str):
        self.d.xpath(f'//*[@text="{text}"').click()


