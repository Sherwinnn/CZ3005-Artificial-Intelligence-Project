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
    path = []
    travelled = {}
    openlist = PriorityQueue()
    openlist.put( (0, (start,start,0) ) ) #(fvalue, (node, parent, gvalue) )
    distance = 0

    while not openlist.empty():
        curnode,parent,distFromStart = openlist.get()[1]
        # print(curnode)
        travelled[curnode] = parent
        if curnode==end:
            distance = distFromStart
            while (curnode!=start):
                path.append(curnode)
                curnode = travelled[parent]
            path = path[::-1]
            break;
        for child in GDict[curnode]:
            if child not in travelled:
                # print("child:",child)
                distStartToChild = distFromStart+DistDict[min(curnode,child),max(curnode,child)]
                openlist.put(
                    (
                        heuristic(CostDict, 
                        CoordDict, 
                        curnode, end, child, 
                        distStartToChild, 
                        budget),
                        (child,curnode,distStartToChild)
                    )
                )
    return path,distance,0

def begin(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    return IOParser.outputParser(aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget))