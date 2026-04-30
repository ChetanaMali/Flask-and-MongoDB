from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'This is a simple Flask application:)'

@app.route('/about')
def about():
    return 'this is a about page:)'

if __name__ == '__main__':
    app.run(debug=True)