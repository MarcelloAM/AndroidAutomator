import time

from ppadb.client import Client as AdbClient
from AutomatorAndroid import Android

def teste(device):
    device.unlock_screen()
    device.quick_panel()
    time.sleep(2)
    device.d.keyevent('home')


if __name__ == '__main__':
    print('Lista de devices:')
    client = AdbClient(host="127.0.0.1", port=5037)
    celulares = client.devices()
    for celular in celulares:
        print(celular.serial)

    serial = input('Informe o serial do device para o teste:\n')
    print(f'Conectado a {serial}')
    device = Android(serial)

    teste(device=device)