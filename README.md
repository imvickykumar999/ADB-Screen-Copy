
# `Quick Connect`

```bash
scrcpy --tcpip=192.168.0.103 -r "screen recording.mp4"
```

------------------

<br>

## `One Time Connect (TCP / IP)`

```bash
>>> adb devices
    * daemon not running; starting now at tcp:5037
    * daemon started successfully
    List of devices attached

>>> adb tcpip 5555
    restarting in TCP mode port: 5555

>>> adb devices
    List of devices attached
    RZ8N60JN0EE     device

>>> adb shell "ip addr show wlan0 | grep -e wlan0$ | cut -d\" \" -f 6 | cut -d/ -f 1"
    192.168.0.103

>>> adb connect 192.168.0.103:5555
    connected to 192.168.0.103:5555
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
