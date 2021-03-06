"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def menu():
    """Renders a sample page."""
    return render_template("menu.html")

@app.route('/criminal-psychology')
def criminalPsychology():
    return render_template("criminal-psychology.html")

@app.route('/criminal-psychology/core-theory-one')
def criminalPsychologyCoreTheoryOne():
    return render_template("criminal-psychology/core-theory-one.html")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
