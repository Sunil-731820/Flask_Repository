from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/defaultPage")
def defaultpage():
    return "this is the EXample of The Default page "

'''
Web applications use different HTTP methods when accessing URLs. 
You should familiarize yourself with the HTTP methods as you work with Flask. By default, 
a route only answers to GET requests. You can use the methods argument of the route() 
decorator to handle different HTTP method
'''

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        return "This is the Post method of If Condition is getting called "
    else:
        return "this is the get Method of else Condition is getting called"

if __name__== '__main__':
    app.run(debug=True)

