from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'This is a simple Flask application:)'

@app.route('/api/<name>')
def api(name):
    result = 'hello this is ' + name
    return result

if __name__ == '__main__':
    app.run(debug=True)