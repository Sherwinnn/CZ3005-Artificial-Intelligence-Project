from queue import PriorityQueue
import IOParser

def UCS(GDict, DistDict, CostDict, start, end, budget):
    
    q = PriorityQueue()
    # item in queue (dist, (nodeId, parent(anc), budget) )
    q.put((0, (start,-1,0)))
    # DIST and cost
    visited = {}
    ansDist = 0 
    ansCost = 0
    while not q.empty():
        (curDist, _temp) = q.get()
        (u, anc, curCost) = _temp
        
        if visited.get(u) != None and  curCost > visited[u][0]:
            continue
        visited[u] = (curCost, anc)

        if(u == end):
            ansDist, ansCost = curDist, curCost
            break

        for v in GDict[u]:
            dist = DistDict[(min(u,v),max(u,v))] + curDist
            cost = CostDict[(min(u,v),max(u,v))] + curCost
            if cost > budget:
                continue
            q.put((dist,(v,u,cost)))
    
    path = []
    node = end
    while node != -1:
        path.append(node)
        node = visited[node][1]
    
    path.reverse()
    return (path,ansDist,ansCost)

def begin(GDict, DistDict, CostDict, start, end, budget):
    IOParser.outputParser(UCS(GDict, DistDict, CostDict, start, end, budget))
    