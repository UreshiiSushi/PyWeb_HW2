from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/feedback')
def send_feedback():
    return 'TY for your feedback!'

if __name__ == '__main__':
    app.run(host= '127.0.0.1', port='5000', debug=True)