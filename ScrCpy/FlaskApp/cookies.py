
from flask import (
    Flask, 
    request, 
    make_response, 
    render_template
)
app = Flask(__name__) 

# Using set_cookie( ) method to set the key-value pairs below. 
@app.route('/setcookie') 
def setcookie(): 
	
	# Initializing response object 
	resp = make_response('Setting the cookie') 
	resp.set_cookie('GFG','ComputerScience Portal') 
	return resp 

# getting cookie from the previous set_cookie code 
@app.route('/getcookie') 
def getcookie(): 
    GFG = request.cookies.get('GFG') 
    return 'GFG is a '+ GFG 

@app.route('/', methods = ['GET']) 
def Login(): 
   return render_template('login.html') 
  
@app.route('/details', methods = ['GET','POST']) 
def login(): 
    if request.method == 'POST': 
        name = request.form['username'] 
        output = 'Hi, Welcome '+name+ '' 
        resp = make_response(output) 
        resp.set_cookie('username', name) 
    return resp 

app.run(debug=True)
