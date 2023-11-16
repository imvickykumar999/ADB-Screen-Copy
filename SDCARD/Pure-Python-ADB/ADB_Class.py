
# https://github.com/Swind/pure-python-adb#examples
# Default serial is "127.0.0.1" and 5037


import os
from ppadb.client import Client as AdbClient


class Manuipulate_sdcard():
    def __init__(self, host, port) -> None:

        print(f'\nConnecting ...')
        os.system(f'adb connect {host}')

        self.client = AdbClient(
            host="127.0.0.1", 
            port=5037
        )

        self.serial = f'{host}:{port}'
        self.device = self.client.device(self.serial)


    def all_devices(self):
        print('\nList of Connected Devices.')

        for device in self.client.devices():
            print('\t', device.serial)


    def get_version(self):
        print('\nVersion:', self.client.version())


    def disconnect(self):
        self.client.remote_disconnect(self.serial)
        print('\nADB Disconnected.')


    def screenshot(self):
        result = self.device.screencap()

        with open("static/screenshot.png", "wb") as fp:
            fp.write(result)
            print('\nScreenshot saved.')


    def install_apk(self, apk):
        apk_path = f"static/{apk}"

        print('\nInstalling APK ...')
        self.device.install(apk_path)
        print('APK Installed.')


    # def shell_echo(self):
    #     self.device.shell("echo hello world !")


    # def push_file(self):
    #     # self.device.push("static/", "/sdcard/Download/Telegram/static/") # push folder
    #     self.device.push("static/example.apk", "/sdcard/Download/Telegram/example.apk")


    # def pull_file(self):
    #     self.device.shell("screencap -p /sdcard/Download/Telegram/DARE2COMPETE HACKATHON.pdf")
    #     self.device.pull("/sdcard/Download/Telegram/DARE2COMPETE HACKATHON.pdf", "static/DARE2COMPETE HACKATHON.pdf")


if __name__ == '__main__':
    host, port = "192.168.0.103", 5555
    sdcard = Manuipulate_sdcard(host, port)

    # sdcard.get_version()
    sdcard.all_devices()

    apk = 'example.apk'
    # sdcard.install_apk(apk)

    sdcard.screenshot()
    # sdcard.disconnect()
