import IOParser
from queue import PriorityQueue
from math import cos,sin,acos,sqrt

def heuristic(CoordDict, end, child, distancet):
    #calculate great circle distance
    #r = 6371 #km
    #a , x = CoordDict[child]
    #b , y = CoordDict[end]
    #greatCircleDist = r*acos(cos(a) * cos(b) * cos(x-y) + sin(a) * sin(b))

    #Calculate Chebyshew 
    # min((CoordDict[end][0]-CoordDict[child][0] ) , (CoordDict[end][1]- CoordDict[child][1]))
    return distancet + sqrt( (CoordDict[end][0]-CoordDict[child][0] )**2 + (CoordDict[end][1]- CoordDict[child][1])**2 )

def aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    path = []
    travelled = {} #stores {node : distance from start to that node}
    openlist = PriorityQueue()
    openlist.put( (0, (start,start, 0, budget) ) ) #(fvalue, (node, parent, gvalue, budgetRemaining) )
    distance = 0

    while not openlist.empty():
        curnode,parent,distFromStart,budgetRemaining = openlist.get()[1]
        if travelled.get(curnode)!=None and budgetRemaining<travelled[curnode][2]:
            continue
        
        travelled[curnode] = (parent,distFromStart,budgetRemaining)
        if curnode==end:
            distance = distFromStart
            budget -= budgetRemaining
            pathnode = end
            # while (pathnode!=start):
            #     path.append(pathnode)
            #     pathnode = travelled[pathnode]
            # path = path[::-1]
            break
        for child in GDict[curnode]:
            # print("child:",child)
            distStartToChild = distFromStart+DistDict[min(curnode,child),max(curnode,child)]
            budgetAfterDeduct = budgetRemaining-CostDict[min(curnode,child),max(curnode,child)]
            if budgetAfterDeduct<0:  #check if not enough budget
                continue
            openlist.put(
                (
                    heuristic( 
                    CoordDict,
                    end, child, 
                    distStartToChild, 
                    ),
                    (child,curnode,distStartToChild, budgetAfterDeduct)
                )
            )
    return path,distance,budget

def begin(GDict, DistDict, CostDict, CoordDict, start, end, budget):
    return IOParser.outputParser(aStar(GDict, DistDict, CostDict, CoordDict, start, end, budget))