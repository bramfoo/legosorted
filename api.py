import logging
import json
import os
import pickle
from flask import Flask, Response, request
from magician import Magician
from recogniser.shape import Shape
from recogniser.color import Color
from box.sort import Sort
from box.dimension import Dimension

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/api/stop")
def stop():
    if not os.path.isfile(Magician.lock_file):
        return as_json({"result": False})
    os.remove('magician.pickles')
    return as_json({"result": True})


@app.route("/api/start")
def start():
    if os.path.isfile(Magician.lock_file):
        return as_json({"result": False})

    shape = Shape.from_string(request.args.get('shape'))
    color = Color.from_string(request.args.get('color'))
    sort = Sort.from_string(request.args.get('sort'))
    length = request.args.get('length')
    width = request.args.get('width')

    pickle.dump({
        "shape": shape,
        "color": color,
        "sort": sort,
        "dimension": None if length is None or width is None else Dimension(int(length), int(width))
    }, open(Magician.lock_file, "wb"))
    return as_json({"result": True})


def as_json(data):
    return Response(json.dumps(data), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()
