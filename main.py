import json
import Task1
import Task2
import Task3

if __name__ == '__main__':

    start = 1
    end = 50
    budget = 287932

    with open('G.json') as f:
        GDict = json.load(f)
    with open('Dist.json') as f:
        DistDict = json.load(f)
    with open('Cost.json') as f:
        CostDict = json.load(f)
    with open('Coord.json') as f:
        CoordDict = json.load(f)
    
    print("Starting Task 1: Dijkstra ... \n")
    Task1.begin(GDict,start,end)

    print("Starting Task 2: UCS... \n")
    Task2.begin(GDict, DistDict, CostDict, start, end, budget)

    print("Starting Task 3: ... \n")
    Task3.begin(GDict, DistDict, CostDict, CoordDict, start, end, budget)


    




