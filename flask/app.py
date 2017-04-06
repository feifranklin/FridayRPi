from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/cakes')
def cakes():
    return 'I love cake'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

