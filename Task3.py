from tracemalloc import start
import IOParser
from queue import PriorityQueue
from math import cos,sin,acos

def heuristic(CostDict, CoordDict, curnode, end, child, distancet, budget):
    #calculate great circle distance
    r = 6371 #km
    a , x = CoordDict[child]
    b , y = CoordDict[end]
    greatCircleDist = r*acos(cos(a) * cos(b) * cos(x-y) + sin(a) * sin(b))

    return distancet+greatCircleDist

def aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    visited = set(())
    openlist = PriorityQueue()
    openlist.put((0,start))
    distance = 0

    while not openlist.empty():
        curnode = openlist.get()[1]
        if curnode!=start:
            distance+=DistDict[min(start,curnode),max(start,curnode)]
        visited.add(curnode) #move curnode into visited list
        if curnode==end:
            break;
        for child in GDict[curnode]:

            if child not in visited:
                
                openlist.put(
                    (
                        heuristic(CostDict, CoordDict, curnode, end, child, DistDict[curnode,child]+distance, budget),
                        child
                    )
                )
    return list(visited),distance,0

def begin(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    return IOParser.outputParser(aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget))
