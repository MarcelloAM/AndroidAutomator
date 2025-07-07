import uiautomator2 as u2
import adbutils as a2
import time
from ppadb.client import Client as AdbClient

class Android:
    client = AdbClient(host='127.0.0.1', port=5037)

    def __init__(self, deviceid: str):
        self.deviceid = deviceid
        self.d = u2.connect(self.deviceid)
        self.a = a2.AdbClient(self.deviceid)


    def unlock_screen(self):
        return   self.d.shell('input keyevent 82')


    def quick_panel(self):
        return self.d.open_quick_settings()


    def wait(self, number: int):
        if number != int:
            print('Número precisa ser um inteiro.')
        else:
            time.sleep(number)


    def close_apps(self):
        pass
