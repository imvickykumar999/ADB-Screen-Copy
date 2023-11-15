
# https://github.com/Swind/pure-python-adb#examples
# https://pypi.org/project/pure-python-adb/
# pip install -U pure-python-adb

def get_version():
    from ppadb.client import Client as AdbClient
    # Default is "127.0.0.1" and 5037

    client = AdbClient(host="127.0.0.1", port=5037)
    print(client.version())
    # client.remote_disconnect()

# get_version()
# >>> 41

def connect_device():
    from ppadb.client import Client as AdbClient
    # Default is "127.0.0.1" and 5037

    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("192.168.0.103:5555") # edit ip-address
    print(device)

# connect_device()
# >>> <ppadb.device.Device object at 0x00000291B2452E80>

def install_apk():
    from ppadb.client import Client as AdbClient
    apk_path = "static/example.apk"

    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()

    for device in devices:
        device.install(apk_path)

# install_apk()

def shell_echo():
    from ppadb.client import Client as AdbClient
    # Default is "127.0.0.1" and 5037

    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("192.168.0.103:5555")
    device.shell("echo hello world !")

# shell_echo()

def screenshot():
    from ppadb.client import Client as AdbClient
    client = AdbClient(host="127.0.0.1", port=5037)

    device = client.device("192.168.0.103:5555")
    result = device.screencap()

    with open("screen.png", "wb") as fp:
        fp.write(result)

# screenshot()

def push_file():
    from ppadb.client import Client as AdbClient
    client = AdbClient(host="127.0.0.1", port=5037)

    device = client.device("192.168.0.103:5555")
    device.push("static/screen.png", "/sdcard/Download/Telegram/screen.png")

# push_file()

def pull_file():
    from ppadb.client import Client as AdbClient
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("192.168.0.103:5555")

    device.shell("screencap -p /sdcard/Download/Telegram/DARE2COMPETE HACKATHON.pdf")
    device.pull("/sdcard/Download/Telegram/DARE2COMPETE HACKATHON.pdf", "static/DARE2COMPETE HACKATHON.pdf")

# pull_file()
