from flask import Flask, request, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login_page():
    name = request.form
    return name
if __name__ == '__main__':
    app.run(port = 8080, debug=True)