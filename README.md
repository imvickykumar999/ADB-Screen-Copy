
# `ScrCpy GUI`

https://github.com/imvickykumar999/ADB-Screen-Copy/blob/d8dcceb25600d219055dc03862cf484ee9594df3/Projects/TkinterGUI/ScrCpy_GUI.py#L29

<br>

https://github.com/imvickykumar999/ADB-Screen-Copy/assets/50515418/08951c4e-979f-4dcb-bafb-bc69d60b0081

<br>

## `Set Environment Variable`

![Environment Variable](https://github.com/imvickykumar999/ADB-Screen-Copy/assets/50515418/c182b47f-30ba-418f-ac6b-b708422d7303)

<br>

## `Quick Start`

```bash
# ... to screen record connected device
>>> scrcpy --tcpip=192.168.0.102 -r "screen recording.mp4"

# ... audio forwarding
>>> scrcpy --tcpip=192.168.0.102 --audio-source=mic

# ... to press power key
>>> adb -s 192.168.0.102 shell input keyevent 26
```

<br>

## `Pairing Code` : [`Wireless debugging`](https://stackoverflow.com/a/73605270/11493297)

```bash
# Pair device with pairing code

>>> adb pair
   adb.exe: usage: adb pair HOST[:PORT] [PAIRING CODE]
```

<br>

## `One Time Connect (TCP / IP)`

```bash
>>> adb devices
    * daemon not running; starting now at tcp:5037
    * daemon started successfully
    List of devices attached

# Connect via USB

>>> adb usb
    restarting in USB mode

>>> adb tcpip 5555
    restarting in TCP mode port: 5555

# Disconnect USB

>>> adb devices
    List of devices attached
    RZ8N60JN0EE     device

>>> adb shell "ip addr show wlan0 | grep -e wlan0$ | cut -d\" \" -f 6 | cut -d/ -f 1"
    192.168.0.103

>>> adb connect 192.168.0.103:5555
    connected to 192.168.0.103:5555

>>> adb pair 192.168.0.103:40535
    Enter pairing code: 230630
    Successfully paired to 192.168.0.103:40535 [guid=adb-RZ8N60JN0EE-DzkZ1Q]
```

<br>

## `Remove USB (testing)`

```bash
>>> adb shell input keyevent 26

>>> adb shell input keyevent 17
>>> adb shell input text hello

>>> adb disconnect
```

<br>

## `Screen Copy (scrcpy)`

```bash
>>> adb devices -l
>>> adb connect 192.168.0.103

>>> scrcpy
>>> scrcpy --tcpip=192.168.0.103

# Run in Folder address bar to Power ON / OFF
>>> adb shell input keyevent 26
>>> scrcpy -r recording.mp4

>>> adb disconnect 192.168.0.103
>>> adb disconnect
```
