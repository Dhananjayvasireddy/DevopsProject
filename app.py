from flask import Flask

app = Flask(__name__)



@app.route('/')

def hello_world():

    return 'Hello There, Finally my project seems to be working!'
