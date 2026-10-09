from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Ahoj z Dockeru! Verze 1.0</h1>"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



