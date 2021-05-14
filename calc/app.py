from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/math/<operation>')
def calc(operation):
    math = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{math[operation](a, b)}"
