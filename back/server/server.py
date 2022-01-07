from flask import Flask, json, request, jsonify
import os
import sys
import json

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

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    data = {"Ok": True}
    return formatResponse(app, data=data, code=200)

@app.route("/solve", methods=['GET'])
def nPuzzle():
    architect = CreateBoard()
    node = Node()
    board = None
    way = None
    problem = request.args.get("problem")
    hardness = request.args.get("nPuzzle")
    shuffle = request.args.get("shuffle")
    algo = request.args.get("algorithm")
    tree = request.args.get("tree")
    

    if problem == "puzzle": 
        board = architect.createPuzzle(int(hardness), int(shuffle))
    if algo == "HillClimbing": 
        way = HillClimbing()


    sett = Settings(isGraph=not(bool(tree)), maxIter=100000, isQueen=(problem == "queen"))
    out = way.engine(state=board, settings=sett)
    out.toList()
    tmp = json.dumps(out, cls=OutputEncoder)
    data = {"Ok": True, "stuff": json.loads(tmp)}
    return formatResponse(app, data=data, code=200)

def formatResponse(app, data, code):
    return app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype='application/json')

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=9010, debug=True)