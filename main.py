import IOParser
import Task1
import Task2
import Task3

if __name__ == '__main__':

    start = 1
    end = 50
    budget = 287932

    GDict, DistDict, CostDict, CoordDict = IOParser.inputParser()
    
    #print(GDict['1'][0] == 1363)
    #print(DistDict)
    #print(DistDict['1,1363'])
    print("Starting Task 1: Dijkstra ... \n")
    Task1.begin(GDict,start,end)

    print("Starting Task 2: UCS... \n")
    Task2.begin(GDict, DistDict, CostDict, start, end, budget)

    print("Starting Task 3: ... \n")
    Task3.begin(GDict, DistDict, CostDict, CoordDict, start, end, budget)


    




