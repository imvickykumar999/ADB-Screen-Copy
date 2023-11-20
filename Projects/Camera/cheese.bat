
adb shell "am start -a android.media.action.STILL_IMAGE_CAMERA"
timeout 3
adb shell "input keyevent 27"
