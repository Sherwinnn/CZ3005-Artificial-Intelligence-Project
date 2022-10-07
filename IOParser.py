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
        DistDictParse[(min(int(uvpair[0]),int(uvpair[1])), max(int(uvpair[0]),int(uvpair[1])) )] = v

    
    with open('Cost.json') as f:
        CostDict = json.load(f)
    
    CostDictParse = {}
    for k,v in CostDict.items():
        uvpair = k.split(',')
        CostDictParse[(min(int(uvpair[0]),int(uvpair[1])), max(int(uvpair[0]),int(uvpair[1])) )] = v

    

    with open('Coord.json') as f:
        CoordDict = json.load(f)

    CoordDictParse = {}
    for k,v in CoordDict.items():
        CostDictParse[int(k)] = ((int(v[0]), int(v[1]) ))

    return GDictParse, DistDictParse, CostDictParse, CoordDictParse

def outputParser(out):
    (path, Dist, Cost) = out
    print("Shortest path:", "->".join([str(int) for int in path]),".")
    print("Shortest Distance:", Dist)
    print("Total Energy Cost:", Cost)
    print()