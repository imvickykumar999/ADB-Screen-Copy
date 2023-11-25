
# https://stackoverflow.com/a/69838814/11493297

import websocket
  
def on_message(ws, message):
    print(message) # sensor data here in JSON format

def on_error(ws, error):
    print("### error ###")
    print(error)

def on_close(ws, close_code, reason):
    print("### closed ###")
    print("close code : ", close_code)
    print("reason : ", reason  )

def on_open(ws):
    print("connection opened")
    

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://192.168.0.102:8082/sensor/connect?type=android.sensor.accelerometer",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()
