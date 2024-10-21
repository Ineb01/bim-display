from flask import Flask
import requests
from dummy import dummy, dummy_bitmap

app = Flask(__name__)

@app.route('/dummy')
def dummy_local():
    return dummy()

@app.route('/dummybitmap')
def dummy_bitmap_local()
    return dummy_bitmap()

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)