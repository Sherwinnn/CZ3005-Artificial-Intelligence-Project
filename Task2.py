from queue import PriorityQueue

def UCS(GDict, DistDict, CostDict, start, end, budget):
    
    q = PriorityQueue()
    # item in queue (dist, (nodeId, budget) )
    q.put((0, (start,0)))
    # DIST and cost
    visited = {}
    while not q.empty():
        (curDist, _temp) = q.get()
        (u, curCost) = _temp
        if(u == end):
            return (curDist, curCost)
        if visited.get(u) != None and  curCost > visited[u]:
            continue
        visited[u] = curCost

        for v in GDict[u]:
            dist = DistDict[(min(u,v),max(u,v))] + curDist
            cost = CostDict[(min(u,v),max(u,v))] + curCost
            if cost > budget:
                continue
            q.put((dist,(v,cost)))
    
    print("CANNOT")

def begin(GDict, DistDict, CostDict, start, end, budget):
    (dist,cost) = UCS(GDict, DistDict, CostDict, start, end, budget)
    print(dist),
    print(cost)