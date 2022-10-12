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
    return distancet + eu  # We used Euclidean Distance

def aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    visited = {}                                #stores {node : cost remaining from that node}
    pq = PriorityQueue()
    pq.put( (0, (start,[], 0, 0) ) )            #(fvalue, (node, path, gvalue, Cost) )
    distance = -1
    numberOfVisited = 0
    
    while not pq.empty():
        curnode,path,distFromStart,cost = pq.get()[1]
        if visited.get(curnode)!=None and cost>visited[curnode]:
            continue
        numberOfVisited += 1
        visited[curnode] = cost
        if curnode==end:                        # Reached end node
            distance = distFromStart
            path+=[curnode]
            break

        for child in GDict[curnode]:
            distStartToChild = distFromStart+DistDict[curnode,child]
            childcost= cost + CostDict[curnode, child]
            if childcost>budget:  #check if not enough budget
                continue
            pq.put(
                (
                    heuristic( 
                    CoordDict,
                    end, child, 
                    distStartToChild, 
                    ),
                    (child,path+[curnode],distStartToChild, childcost)
                )
            )
    return path,distance,budget,numberOfVisited

def begin(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    return IOParser.outputParser(aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget))