
# https://www.geeksforgeeks.org/flask-cookies/

from flask import Flask, render_template, request, redirect, url_for
import scrcpy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        device_id = request.form['device_id']
        scrcpy_server = scrcpy.ScrcpyServer(device_id)
        scrcpy_server.start()
        return redirect(url_for('stream'))
    else:
        return render_template('index.html')

@app.route('/stream')
def stream():
    device_id = request.args.get('device_id')
    scrcpy_server = scrcpy.ScrcpyServer(device_id)
    stream = scrcpy_server.get_stream()
    return stream

if __name__ == '__main__':
    app.run(debug=True)