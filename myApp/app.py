from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! I Have Started Working as Flask App Developer </p>"


if __name__ =='__main__':  
    app.run(debug = True)