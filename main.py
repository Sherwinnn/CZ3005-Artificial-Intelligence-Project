import IOParser
import Task1
import Task2
import Task3
from datetime import datetime


#Statements


if __name__ == '__main__':

    start = 1
    end = 50
    budget = 287932

    GDict, DistDict, CostDict, CoordDict = IOParser.inputParser()
    
    print("Starting Task 1: Dijkstra ... \n")
    Task1.begin(GDict, DistDict, start, end)

    print("Starting Task 2: UCS... \n")
    startTime=datetime.now()
    Task2.begin(GDict, DistDict, CostDict, start, end, budget)
    print("The time used:",datetime.now()-startTime, "\n")

    print("Starting Task 3: ... \n")
    startTime=datetime.now()
    Task3.begin(GDict, DistDict, CostDict, CoordDict, start, end, budget)
    print("The time used:",datetime.now()-startTime, "\n")


    





