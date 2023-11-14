
echo off
set num=%1
shift
for /f "tokens=1,* delims= " %%a in ("%*") do set ALL_BUT_FIRST=%%b
echo %ALL_BUT_FIRST%
adb shell service call isms 5 s16 "com.android.mms" s16 "%num%" s16 "+01000000000" s16 "%ALL_BUT_FIRST%" i32 0 i32 0
