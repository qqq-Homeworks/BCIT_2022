from flask import Flask
import fibonachi

app = Flask(__name__)


@app.route('/<int:number>')
def response_subsequence(number):
    return list(fibonachi.fib(number))
