import json


# 4 Dictionaries needed
G = {}
Dist = {}
Cost = {}
Coord = {}

if __name__ == '__main__':
    with open('G.json') as f:
        G = json.load(f)
    with open('Dist.json') as f:
        Dist = json.load(f)
    with open('Cost.json') as f:
        Cost = json.load(f)
    with open('Coord.json') as f:
        Coord = json.load(f)

    start = '1'
    end = '50'
    budget = 287932




