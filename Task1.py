import json

def inputGraph():
    with open("Graph.json") as f:
        Gdict = json.load(f)
    return Gdict

def begin():
    graph = inputGraph()

    print()