from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'CI Pipeline Sample App', 'status': 'ok'})

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a', '0'))
        b = float(request.args.get('b', '0'))
    except ValueError:
        return jsonify({'error': 'invalid input'}), 400
    return jsonify({'result': a + b})

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        a = float(request.args.get('a', '0'))
        b = float(request.args.get('b', '0'))
    except ValueError:
        return jsonify({'error': 'invalid input'}), 400
    return jsonify({'result': a - b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
