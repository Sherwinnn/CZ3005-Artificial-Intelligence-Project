import IOParser
from queue import PriorityQueue
from math import cos,sin,acos,sqrt,dist

def heuristic(CoordDict, end, child, distancet):
    #calculate great circle distance
    r = 6371 #km
    a , x = CoordDict[child]
    b , y = CoordDict[end]
    greatCircleDist = r*acos(cos(a) * cos(b) * cos(x-y) + sin(a) * sin(b))
    #calculate euclidean 
    eu = sqrt( (CoordDict[end][0]-CoordDict[child][0] )**2 + (CoordDict[end][1]- CoordDict[child][1])**2 )
    #Calculate Chebyshew 
    che = min((CoordDict[end][0]-CoordDict[child][0] ) , (CoordDict[end][1]- CoordDict[child][1]))
    # Calculate mahathan distance
    man = abs(CoordDict[end][0]-CoordDict[child][0] ) + abs(CoordDict[end][1]- CoordDict[child][1])
    return distancet + che

def aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    travelled = {} #stores {node : cost remaining from that node}
    openlist = PriorityQueue()
    openlist.put( (0, (start,[], 0, 0) ) ) #(fvalue, (node, path, gvalue, Cost) )
    distance = -1
    numberOfVisited = 0

    while not openlist.empty():
        curnode,path,distFromStart,cost = openlist.get()[1]
        if travelled.get(curnode)!=None and cost>travelled[curnode]:
            continue
        numberOfVisited += 1
        travelled[curnode] = cost
        if curnode==end:
            distance = distFromStart
            path+=[curnode]
            break
        for child in GDict[curnode]:
            distStartToChild = distFromStart+DistDict[curnode,child]
            childcost= cost + CostDict[curnode, child]
            if childcost>budget:  #check if not enough budget
                continue
            openlist.put(
                (
                    heuristic( 
                    CoordDict,
                    end, child, 
                    distStartToChild, 
                    ),
                    (child,path+[curnode],distStartToChild, childcost)
                )
            )
    return path,distance,cost,numberOfVisited

def begin(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    return IOParser.outputParser(aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget))