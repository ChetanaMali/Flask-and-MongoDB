from flask import Flask, request, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', today=date.today())

@app.route('/date')
def get_date():
    today = date.today()
    print(today)
    return str(today)

@app.route('/api')
def api():
    name = request.values.get('name')
    return f'Hello, {name}! This is a simple API endpoint.'

if __name__ == '__main__':
    app.run(port = 8080, debug=True)