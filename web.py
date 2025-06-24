import flask
from flask import request, jsonify

#create a flask app object
app = flask.Flask(__name__)

#tell the server to reload each time the code changes
app.config["DEBUG"] = True

#load student dictionaries

#create a route to display our name
@app.route('/', methods = ['GET'])
def index():
    return "<h1> My name is Ryka Herbert</h1>"
#create 2 routes
#- one route will return all student data
#- one route will return students by major

#run the application
app.run()
