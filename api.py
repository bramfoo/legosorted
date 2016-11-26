import logging
import json
import os
import pickle
from flask import Flask, Response, request, render_template
#from magician import Magician
from recogniser.shape import Shape
from recogniser.color import Color
from box.sort import Sort
from box.dimension import Dimension

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/api/stop")
def stop():
    if not os.path.isfile('magician.pickles'):
        return as_json({"result": False})
    os.remove('magician.pickles')
    return as_json({"result": True})


@app.route("/api/start")
def start():
    if os.path.isfile('magician.pickles'):
        return as_json({"result": False})

    shape = Shape.from_string(request.args.get('shape'))
    color = Color.from_string(request.args.get('color'))
    sort = Sort.from_string(request.args.get('sort'))
    length = request.args.get('length')
    width = request.args.get('width')

    if length == "":
        length = None

    if width == "":
        width = None

    pickle.dump({
        "shape": shape,
        "color": color,
        "sort": Sort.color if sort is None else sort,
        "dimension": None if length is None or width is None else Dimension(int(length), int(width))
    }, open('magician.pickles', "wb"))
    return as_json({"result": True})


@app.route("/")
def index():
    return render_template('index.html')


def as_json(data):
    return Response(json.dumps(data), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()
