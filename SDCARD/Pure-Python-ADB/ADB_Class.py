
# https://github.com/Swind/pure-python-adb#examples
# Default serial is "127.0.0.1" and 5037


import os
from ppadb.client import Client as AdbClient


class Manuipulate_sdcard():
    def __init__(self, host, port) -> None:
        os.system(f'adb connect {host}')

        self.client = AdbClient(host="127.0.0.1", port=5037)
        self.serial = f'{host}:{port}'
        self.device = self.client.device(self.serial)


    def all_devices(self):
        print([device.serial for device in self.client.devices()])


    def get_version(self):
        print(self.client.version())


    def disconnect(self):
        self.client.remote_disconnect(self.serial)


    def screenshot(self):
        result = self.device.screencap()

        with open("static/ppadb.png", "wb") as fp:
            fp.write(result)


    # def install_apk(self):
    #     apk_path = "static/example.apk"
    #     self.device.install(apk_path)


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

    # sdcard.all_devices()
    # sdcard.get_version()

    sdcard.screenshot()
    # sdcard.disconnect()
