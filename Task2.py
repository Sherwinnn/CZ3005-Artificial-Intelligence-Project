from queue import PriorityQueue
import IOParser

def UCS(GDict, DistDict, CostDict, start, end, budget):
    
    pq = PriorityQueue()
    pq.put((0, (start,[],0)))                                   # (Distance, (Node, path, energy cost))
    visited = {}                                                # Stored the cost of previous visit of a node        
    numberOfVisited = 0                                         # Stored the number of visited node (Including revisit node)
    while not pq.empty():
        (curDist, _temp) = pq.get()                             #  Get the lowest distance 
        (u, anc_path, curCost) = _temp                          # get the infromation from the node
        
        if visited.get(u) != None and  curCost > visited[u]:    # The claim & Observation mentioned in report
            continue
        numberOfVisited += 1
        visited[u] = curCost
        
        if(u == end):                                           # Reached End path
            ansDist, ansCost = curDist, curCost
            path = anc_path + [u]
            return (path,ansDist,ansCost,numberOfVisited)

        for v in GDict[u]:                                      # Expand the neighbour
            dist = DistDict[(u,v)] + curDist
            cost = CostDict[(u,v)] + curCost
            if cost > budget:                                   # If the cost exceed budget, ignore it,
                continue
            pq.put((dist,(v,anc_path+[u],cost)))

    

def begin(GDict, DistDict, CostDict, start, end, budget):
    IOParser.outputParser(UCS(GDict, DistDict, CostDict, start, end, budget))
    