
# TCP/IP ...

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


# Remove USB ...

    >>> adb shell input keyevent 17
        adb.exe: more than one device/emulator

    >>> adb shell input keyevent 17
    >>> adb shell input text hello

    >>> adb disconnect


# Screen Copy (scrcpy)

    >>> scrcpy
    >>> scrcpy -r recording.mp4
