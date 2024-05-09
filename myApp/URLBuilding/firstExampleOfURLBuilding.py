from flask import Flask

app = Flask(__name__)

@app.route("/")
def defaultUrl():
    return "This is The Default Url "

@app.route('/loginpage')
def loginPage():
    return "This is the Url Used for The Login pages "

@app.route("/signUpPage")
def signUppage():
    return "this is the Url used for the Sign Up pages"


if __name__ =='__main__':  
    app.run(debug = True)