import json

def inputParser():
    with open('G.json') as f:
        GDict = json.load(f)

    GDictParse = {}
    for k,nodeList in GDict.items():
        GDictParse[int(k)] = []
        for node in nodeList:
            GDictParse[int(k)].append(int(node))

    with open('Dist.json') as f:
        DistDict = json.load(f)

    DistDictParse = {}
    for k,v in DistDict.items():
        uvpair = k.split(',')
        DistDictParse[int(uvpair[0]),int(uvpair[1])] = v
        DistDictParse[int(uvpair[1]),int(uvpair[0])] = v

    
    with open('Cost.json') as f:
        CostDict = json.load(f)
    
    CostDictParse = {}
    for k,v in CostDict.items():
        uvpair = k.split(',')
        CostDictParse[int(uvpair[0]),int(uvpair[1])] = v
        CostDictParse[int(uvpair[1]),int(uvpair[0])] = v

    

    with open('Coord.json') as f:
        CoordDict = json.load(f)

    CoordDictParse = {}
    for k,v in list(CoordDict.items()):
        CoordDictParse[int(k)] = ((int(v[0]), int(v[1]) ))

    return GDictParse, DistDictParse, CostDictParse, CoordDictParse

def outputParser(out):
    (path, Dist, Cost, numberOfVisited) = out
    print("Shortest path:", "->".join([str(int) for int in path]),".")
    print("Shortest Distance:", Dist)
    print("Total Energy Cost:", Cost)
    print("Total Number of Visited Node:", numberOfVisited)