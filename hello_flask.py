from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world from flask'

app.run(port=1111)