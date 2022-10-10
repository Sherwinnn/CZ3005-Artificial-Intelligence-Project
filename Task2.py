from queue import PriorityQueue
import IOParser

def UCS(GDict, DistDict, CostDict, start, end, budget):
    
    q = PriorityQueue()
    q.put((0, (start,-1,0)))
    visited = {}
    parent = {}
    ansDist = 0 
    ansCost = 0
    numberOfVisited = 0
    while not q.empty():
        (curDist, _temp) = q.get()
        (u, anc, curCost) = _temp
        
        if visited.get(u) != None and  curCost > visited[u]:
            continue
        numberOfVisited += 1
        visited[u] = curCost
        if(parent.get(u) == None):
            parent[u] = {}
        if(parent[u].get(int(curDist)) == None):
            parent[u][int(curDist)] = []
        parent[u][int(curDist)].append(anc)

        if(u == end):
            ansDist, ansCost = curDist, curCost
            break

        for v in GDict[u]:
            dist = DistDict[(u,v)] + curDist
            cost = CostDict[(u,v)] + curCost
            if cost > budget:
                continue
            q.put((dist,(v,u,cost)))
    
    path = []
    node = end
    distV = ansDist
    while node != -1:
        #print(node)
        path.append(node)
        oldnode = parent[node][int(distV)][0]
        
        #print(len(parent[node][int(distV)]), " ".join([str(int) for int in parent[node][int(distV)]]))
        if(oldnode == -1):
            break
        distV -= DistDict[(node,oldnode)]
        node = oldnode
    
    path.reverse()
    costV = 0
    distV = 0
    last = -1
    for node in path:
        if last == -1:
            last = node 
            continue
        # if(node ==986):
        #     print("CHANGE")
        #     node = 988
        distV += DistDict[(last,node)]
        costV += CostDict[(last,node)]
        last = node
    print(distV,costV)
    return (path,ansDist,ansCost,numberOfVisited)

def begin(GDict, DistDict, CostDict, start, end, budget):
    IOParser.outputParser(UCS(GDict, DistDict, CostDict, start, end, budget))
    