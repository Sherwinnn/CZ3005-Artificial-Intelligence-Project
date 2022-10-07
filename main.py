import json
import Task1
import Task2
import Task3

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
        DistDictParse[(min(int(uvpair[0]),int(uvpair[1])), max(int(uvpair[0]),int(uvpair[1])) )] = int(v)

    
    with open('Cost.json') as f:
        CostDict = json.load(f)
    
    CostDictParse = {}
    for k,v in CostDict.items():
        uvpair = k.split(',')
        CostDictParse[(min(int(uvpair[0]),int(uvpair[1])), max(int(uvpair[0]),int(uvpair[1])) )] = int(v)

    

    with open('Coord.json') as f:
        CoordDict = json.load(f)

    CoordDictParse = {}
    for k,v in CoordDict.items():
        CostDictParse[int(k)] = ((int(v[0]), int(v[1]) ))

    return GDictParse, DistDictParse, CostDictParse, CoordDictParse

if __name__ == '__main__':

    start = 1
    end = 50
    budget = 287932

    GDict, DistDict, CostDict, CoordDict = inputParser()
    
    #print(GDict['1'][0] == 1363)
    #print(DistDict)
    #print(DistDict['1,1363'])
    print("Starting Task 1: Dijkstra ... \n")
    Task1.begin(GDict,start,end)

    print("Starting Task 2: UCS... \n")
    Task2.begin(GDict, DistDict, CostDict, start, end, budget)

    print("Starting Task 3: ... \n")
    Task3.begin(GDict, DistDict, CostDict, CoordDict, start, end, budget)


    




