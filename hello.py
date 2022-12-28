# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 17:28:02 2022

@author: federico
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"