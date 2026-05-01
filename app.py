from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'This is a simple Flask application:)'

@app.route('/add/<a>/<b>')
def add(a,b):
    result = int(a) + int(b)
    return str(result)

@app.route('/api')
def api():
    name = request.values.get('name')
    return f'Hello, {name}! This is a simple API endpoint.'

if __name__ == '__main__':
    app.run(port = 8080, debug=True)