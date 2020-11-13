from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


# Just an exampel of handling HTTP POST request
# @app.route('/buzzer_off', methods = ['POST'])
# def buzzerOFF():
#     data = request.get_json()
#     data = data['buzzerStatus']
#     buzzer_off(data)

#     return "buzzer is turned off"

if __name__ == '__main__':
    app.run(debug=True, port=80)