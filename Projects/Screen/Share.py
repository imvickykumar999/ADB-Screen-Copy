
# https://stackoverflow.com/a/48831912/11493297

import os

os.system('''
adb shell screenrecord --bit-rate=16m --output-format=h264 --size 800x600 - | ffplay -framerate 60 -framedrop -bufsize 16M -
''')
