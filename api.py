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
    os.remove(Magician.lock_file)
    return as_json({"result": True})


@app.route("/api/start")
def start():
    if os.path.isfile(Magician.lock_file):
        return as_json({"result": False})

    shape = request.args.get('shape')
    color = request.args.get('color')
    sort = request.args.get('sort')
    length = request.args.get('length')
    width = request.args.get('width')

    pickle.dump({
        "shape": None if shape is None else Shape[shape],
        "color": None if color is None else Color[color],
        "sort": Sort.color if sort is None else Sort[sort],
        "dimension": None if length is None or width is None else Dimension(length, width)
    }, open(Magician.lock_file, "wb"))
    return as_json({"result": True})


def as_json(data):
    return Response(json.dumps(data), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()
