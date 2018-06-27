# Authored by void (@ry0id)
# Licensed under MIT

from libgravatar import Gravatar
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

"""
@app.route('/end_result')
def end_result():
    #return render_template('end_result.html')
    #write gravatar url to end_result.html when request is received
"""

if __name__ == '__main__':
    app.run(port=8080)
