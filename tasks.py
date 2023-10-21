
# https://gist.github.com/arjunv/2bbcca9a1a1c127749f8dcb6d36fb0bc
# https://itnext.io/how-you-can-control-your-android-device-with-python-45c3ab15e260

# pip install pure-python-adb -U

from ppadb.client import Client as AdbClient
import time, json, os

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]
    print(f'Connected to {device}')
    return device, client

device, client = connect()


with open("keyevents.json", "r") as json_file:
    my_dict = json.load(json_file)
    
# print(' '.join(my_dict['key_events']['key_power'].split()[2:]))


def browser_search():
    search_bar = '440 200' # x y

    query = input('What word do you want to find the definition of: ')
    search_query = f'what is the definition of {query}'

    device.shell('input keyevent 64')
    time.sleep(0.25) # wait for browser to load
    device.shell(f'input tap {search_bar}')

    # make sure you have the quotation marks around your text
    device.shell(f'input text "{search_query}"')

    device.shell('input keyevent 66')
    time.sleep(3) # wait for results to load


def click_photo():
    # open up camera app
    device.shell('input keyevent 27')

    # wait 5 seconds
    time.sleep(5)

    # take a photo with volume up
    device.shell('input keyevent 24')
    
    print('Taken a photo!')
    time.sleep(5)


def screen_shot():
    screenshot = device.screencap()
    filename = time.time()

    # save the screenshot
    with open(f'screenshots/{filename}.png', 'wb') as f:
        f.write(screenshot)
        print('Saved screenshot!')

    time.sleep(5)


if __name__ == '__main__':
    # pass 

    click_photo()
    # browser_search()
    screen_shot()

    cmd = my_dict['key_events']['key_power']
    os.system(cmd)

    # device.shell('input keyevent 26') # '26' is for power button
    print('Powered Off')


'''
python main.py

Connected to <ppadb.device.Device object at 0x000001CEAD579F40>
Taken a photo!
Saved screenshot!
Powered Off
'''
