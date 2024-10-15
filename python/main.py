from flask import Flask
from dummy import dummy

app = Flask(__name__)

@app.route('/dummy')
def dummy_local():
    return dummy()

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)