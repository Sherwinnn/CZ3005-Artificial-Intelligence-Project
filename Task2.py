from queue import PriorityQueue
import IOParser

def UCS(GDict, DistDict, CostDict, start, end, budget):
    
    q = PriorityQueue()
    q.put((0, (start,[],0)))
    visited = {} # Stored the cost
    ansDist = 0 
    ansCost = 0
    numberOfVisited = 0
    path = []
    while not q.empty():
        (curDist, _temp) = q.get()
        (u, anc_path, curCost) = _temp
        
        if visited.get(u) != None and  curCost > visited[u]:
            continue
        numberOfVisited += 1
        visited[u] = curCost
        
        if(u == end):
            ansDist, ansCost = curDist, curCost
            path = anc_path + [u]
            break

        for v in GDict[u]:
            dist = DistDict[(u,v)] + curDist
            cost = CostDict[(u,v)] + curCost
            if cost > budget:
                continue
            q.put((dist,(v,anc_path+[u],cost)))

    return (path,ansDist,ansCost,numberOfVisited)

def begin(GDict, DistDict, CostDict, start, end, budget):
    IOParser.outputParser(UCS(GDict, DistDict, CostDict, start, end, budget))
    