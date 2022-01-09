from flask import Flask, json, request, jsonify
import os
import sys
import json
from flask_cors import CORS

sys.path.append('../src/InformedSearchAlgorithm/.')
sys.path.append('../src/UninformedSearchAlgorithm/.')
sys.path.append('../src/LocalSearchAlgorithm/.')

from AStarAlgorithm import AStarAlgorithm
from BreadthFirstSearch import BreadthFirstSearch
from HillClimbing import HillClimbing

from Settings import Settings
from Output import Output, OutputEncoder
from CreateBoard import CreateBoard
from Node import Node
sys.setrecursionlimit(10**6)

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def main():
    data = {"Ok": True}
    return formatResponse(app, data=data, code=200)

def guessProblem(problem: str, hardness: int, shuffle: int):
    architect = CreateBoard()
    obj = {
        "NPuzzle": lambda hard, shuf: architect.createPuzzle(hard, shuf),
        "NQueen": lambda hard, shuf: architect.createQueen(hard)
    }
    return obj[problem](hard=hardness, shuf=shuffle)


def guessAlgo(algo: str):
    obj = {
        "HillClimbing": lambda : HillClimbing(),
        "A*": lambda: AStarAlgorithm(),
        "BreadthFirstSearch": lambda: BreadthFirstSearch()
    }
    return obj[algo]()

def argToObj(request):
    obj = {
        "problem": request.args.get("problem"),
        "hardness":int(request.args.get("size")),
        "shuffle" : int(request.args.get("shuffle")),
        "algo" : request.args.get("algorithm"),
        "mode": request.args.get("mode"),
        "maxMove": int(request.args.get("maxMove"))
    }
    return obj

@app.route("/solve", methods=['GET'])
def solve():
    try:
        #[Http Get] -- gathering parameter
        print(request.args)
        req = argToObj(request=request)

        #[Board] -- Creation of the board and algorithm
        board = guessProblem(req["problem"], req["hardness"], req["shuffle"])
        way = guessAlgo(req["algo"])

        print(board)

        #[Settings] -- Creation of settings based on Http request parameter
        sett = Settings(isGraph=(req["mode"] == "graph"), maxIter=req["maxMove"], isQueen=(req["problem"] == "NQueen"))
        out = way.engine(state=board, settings=sett)

        #[Output] -- Format Output
        out.toList()
        tmp = json.dumps(out, cls=OutputEncoder)
        data = {"Ok": True, "stuff": json.loads(tmp)}
        return formatResponse(app, data=data, code=200)
    except Exception as e:
        data = {"Ok": False, "message": "🤷[Error] The request is bad", "Exception": str(e)}
        return formatResponse(app, data=data, code=400)

def formatResponse(app, data, code):
    return app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9010, debug=True)