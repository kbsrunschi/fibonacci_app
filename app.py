#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from fibonacci_app.fibonacci import Fibonacci

app = Flask(__name__)

viewedFibonacci = {}

@app.route('/')
def index():
    """ Landing page """
    return "Hello & Welcome!"

@app.route('/fib', methods=['GET'])
def get_fibonaccis():
    """ GET all previously calculated fibs """
    return jsonify({'Previously calculated fibonaccis:': viewedFibonacci})

@app.route('/fib/help', methods=['GET'])
def get_help_menu():
    """ GET Help menu """
    available_commands = {
        "GET": "Will return all previously viewed fibonacci numbers and their position",
        "POST" : "Pass in an int N and view the corresponding fibonacci number",
        "DELETE": "Pass in an int N and delete the previously viewed fibonacci number",
    }
    return jsonify(available_commands), 202

@app.route('/fib', methods=['POST'])
def get_single_fibonacci():
    """ POST new fibonnaci number """
    if not request.json or not 'position' in request.json:
        abort(400)
    position = request.json['position']
    viewedFibonacci[position] = Fibonacci().calc_fib(position)
    return jsonify({'Position %s'%position: viewedFibonacci[position]}), 201

@app.route('/fib/<int:position>', methods=['DELETE'])
def delete_fibonacci(position):
    """ DELETE previously calculated fib number """
    if position in viewedFibonacci:
        viewedFibonacci.pop(position)
    else:
        abort(404)
    return jsonify({'Position %s has been removed'%position: viewedFibonacci}), 201

@app.errorhandler(404)
def not_found():
    """ Gracefully handle 404 HTTP errors """
    return make_response(jsonify({'error': 'Sorry! Couldn\'t find that one.'}), 404)

@app.errorhandler(400)
def bad_request():
    """ Gracefully handle 400 HTTP errors """
    error_message = 'Ah! Bad request! Please try again. Use /fib/help for availble commands'
    return make_response(jsonify({'error': error_message}), 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
