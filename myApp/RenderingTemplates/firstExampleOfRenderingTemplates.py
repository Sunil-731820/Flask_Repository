from flask import Flask

app = Flask(__name__)
'''
Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do 
the HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template 
engine for you automatically.

Templates can be used to generate any type of text file. For web applications, you’ll primarily be generating HTML pages, but you can also generate markdown, plain text for emails, and anything else.

For a reference to HTML, CSS, and other web APIs, use the MDN Web Docs.

To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. Here’s a simple example of how to render a template:

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

Case 1: a module:

/application.py
/templates
    /hello.html
Case 2: a package:

/application
    /__init__.py
    /templates
        /hello.html

'''

if __name__ == '__main__':
    app.run(debug=True)
    
    