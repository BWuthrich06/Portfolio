"""Portfolio Server"""

import os
import secrets
from flask import Flask, render_template, redirect
from jinja2 import StrictUndefined

secret_key = os.environ['secret_key']

app = Flask(__name__)
app.secret_key = secret_key
app.jinja_env.undefined = StrictUndefined




@app.route('/')
def homepage():
    """View Homepage."""

    return render_template('homepage.html')


@app.route('/about_me')
def about_me():
    """View About Me."""

    return render_template('about_me.html')


@app.route('/projects')
def projects():
    """View Projects."""

    return render_template('projects.html')





if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)