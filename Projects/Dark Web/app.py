
# from HostTor import VicksTor
import VicksTor as vix
vix.run_server('flask')

from flask import (
    Flask,
    render_template, 
    send_from_directory
)

import os
from datetime import datetime

app = Flask(__name__, template_folder='./')
path = 'ScreenRecord'

@app.route(f'/{path}/<path:filename>')  
def send_file(filename):
    return send_from_directory(f'./{path}', filename)

@app.route('/')
def hello_world():
    mod = []
    files = os.listdir(f'./{path}')

    for i in files:
        t = os.path.getmtime(f'./{path}/{i}')
        t = datetime.fromtimestamp(t).strftime('%d-%m-%Y %H:%M:%S')

        s = os.path.getsize(f'./{path}/{i}') / 1048576
        s = round(s, 2)
        mod.append((i, t, s))

    return render_template(
        'index.html', 
        path=path,
        files=mod, 
    )

if __name__ == '__main__':
    app.run(debug = False)
