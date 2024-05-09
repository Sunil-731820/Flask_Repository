'''Modern web applications use meaningful URLs to help users. Users are more likely to like a page and
come back if the page uses a meaningful URL they can remember and use to directly visit a page.
Use the route() decorator to bind a function to a URL.
'''

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/bye')
def By():
    return "this is bye Word from The Sunil "

if __name__ =='__main__':  
    app.run(debug = True)