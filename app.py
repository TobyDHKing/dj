from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

"""
#
logo = ""
topbar = Navbar(logo,
                View('Home', 'get_home'),
                View('Book', 'get_book'),
                )

# registers the "top" menubar
nav = Nav()
nav.register_element('top', topbar)
"""
app = Flask(__name__)



@app.route('/book', methods=['GET'])
def get_book():
    return(render_template('book.html'))




@app.route('/home')
def get_home():
    return(render_template('home.html'))



if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_DEBUG'] = 1
    app.run(debug=True)