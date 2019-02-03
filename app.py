#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from fibonacci import Fibonacci

app = Flask(__name__)

viewedFibonacci = {}

@app.route('/')
def index():
    return "Hello & Welcome!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Sorry! Couldn\'t find that one.'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Ah! Bad request! Please try again. Use /fib/help for availble commands'}), 400)

@app.route('/fib', methods = ['GET'])
def get_fibonaccis():
    return jsonify({ 'Previously calculated fibonaccis:': viewedFibonacci })

@app.route('/fib/help', methods = ['GET'])
def get_help_menu():
    available_commands = {
            "GET": "Will return all previously viewed fibonacci numbers and their position in the sequence",
            "POST" : "Pass in an int N and view the corresponding fibonacci number in the sequence at position N",
            "DELETE": "Pass in an int N and delete the previously viewed fibonacci number at that position. This will result in a smaller set of numbers being returned with the GET command",
            }
    return jsonify(available_commands), 202

@app.route('/fib', methods = ['POST'])
def get_single_fibonacci():
    if not request.json or not 'position' in request.json:
        abort(400)
    position = request.json['position']
    fib_algo = Fibonacci()
    viewedFibonacci[position] = fib_algo.calc_fib(position)
    return jsonify({ 'Position %s'%position: viewedFibonacci[position] }), 201

@app.route('/fib/<int:position>', methods = ['DELETE'])
def delete_fibonacci(position):
    if position in viewedFibonacci:
        viewedFibonacci.pop(position)
    else:
        abort(404)
    return jsonify({ 'Position %s has been removed'%position: viewedFibonacci }), 201

if __name__ == '__main__':
    app.run(debug=True)
