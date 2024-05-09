from flask import Flask

app = Flask(__name__)

@app.route("/projects")
def projectData():
    return "this is the project Url page "


@app.route("/about")
def aboutPage():
    return "This is the project of About page"


if __name__ =='__main__':  
    app.run(debug = True)
    