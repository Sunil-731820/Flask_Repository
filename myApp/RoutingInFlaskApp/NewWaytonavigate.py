from flask import Flask

app = Flask(__name__)
def about():  
    return "This is about page Done By Sunil Using new methods !";  

def about1():  
    return "This is about page Done By Sunil Using new methods for Other Functions !";  
app.add_url_rule("/about","about",about)
app.add_url_rule("/about1","about1",about1)
if __name__=='__main__':
    app.run(debug=True)