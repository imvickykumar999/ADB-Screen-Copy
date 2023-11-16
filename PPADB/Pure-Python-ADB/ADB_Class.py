
# https://github.com/Swind/pure-python-adb#examples

def get_version():
    from ppadb.client import Client as AdbClient
    # Default is "127.0.0.1" and 5037

    client = AdbClient(host="127.0.0.1", port=5037)
    print(client.version())
    # client.remote_disconnect()


def connect_device():
    from ppadb.client import Client as AdbClient
    # Default is "127.0.0.1" and 5037

    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("192.168.0.103:5555") # edit ip-address
    print(device)


def install_apk():
    from ppadb.client import Client as AdbClient
    apk_path = "static/example.apk"

    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()

    for device in devices:
        device.install(apk_path)


def shell_echo():
    from ppadb.client import Client as AdbClient
    # Default is "127.0.0.1" and 5037

    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("192.168.0.103:5555")
    device.shell("echo hello world !")


def screenshot():
    from ppadb.client import Client as AdbClient
    client = AdbClient(host="127.0.0.1", port=5037)

    device = client.device("192.168.0.103:5555")
    result = device.screencap()

    with open("static/ppadb.png", "wb") as fp:
        fp.write(result)


def push_file():
    from ppadb.client import Client as AdbClient
    client = AdbClient(host="127.0.0.1", port=5037)

    device = client.device("192.168.0.103:5555")
    # device.push("static/", "/sdcard/Download/Telegram/static/") # push folder
    device.push("static/example.apk", "/sdcard/Download/Telegram/example.apk")


def pull_file():
    from ppadb.client import Client as AdbClient
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("192.168.0.103:5555")

    device.shell("screencap -p /sdcard/Download/Telegram/DARE2COMPETE HACKATHON.pdf")
    device.pull("/sdcard/Download/Telegram/DARE2COMPETE HACKATHON.pdf", "static/DARE2COMPETE HACKATHON.pdf")

