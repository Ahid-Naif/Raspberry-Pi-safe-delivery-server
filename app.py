from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World again!'


@app.route('/open_lock', methods = ['POST'])
def openLock():
    data = request.get_json()
    # data = data['lockStatus']
    # buzzer_off(data)

    return "Lock is ON"

if __name__ == '__main__':
    app.run(debug=True, port=80)