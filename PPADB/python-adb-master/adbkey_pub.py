
# https://github.com/google/python-adb/releases
# pip install adb-1.3.0.tar.gz

import os.path as op
from adb import adb_commands
from adb import sign_cryptography

# KitKat+ devices require authentication
signer = sign_cryptography.CryptographySigner(
    op.expanduser('~/.android/adbkey'))

# Connect to the device
device = adb_commands.AdbCommands()
device.ConnectDevice(rsa_keys=[signer])

# Now we can use Shell, Pull, Push, etc!
for i in range(10):
  print(device.Shell('echo %d' % i))
