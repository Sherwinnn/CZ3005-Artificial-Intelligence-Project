from queue import PriorityQueue
import sys
import IOParser


def dijkstra(GDict, DistDict, start, end):
    pq = PriorityQueue()
    pq.put([0, [start]])

    distanceDict = {start : sys.maxsize}
    travelledDict = {}
    
    while pq:
        FirstNode = pq.get()
        currentDist = FirstNode[0]                      # Setting the accumulated distance thus far as currentDist
        currentPath = FirstNode[1]                      # Obtaining the current path to be taken based on the dequeued node 
        currentNode = currentPath[-1]                   # Setting the current node as last taken node in currentPath
        travelledDict[currentNode] = 1                  # Setting values of current node in Travelled dict as 1 (visited)

        if currentNode == end:                          # Check if goal is reached
            return currentPath, currentDist             # Return the accumulated shortest path and distance thus far

        for adjNode in GDict[currentNode]:              # Parsing through each node connected to current node
            if adjNode not in distanceDict:
                distanceDict[adjNode] = sys.maxsize     # Setting maximum or infinite value if distance not stored in distanceDict yet

            newPath = currentPath[:]                    
            newPath.append(adjNode)                     # Adding the neighbouring node to the new path
            newDistance = currentDist+ DistDict[min(currentNode,adjNode),max(currentNode,adjNode)]

            if adjNode not in travelledDict and distanceDict[adjNode] > newDistance:    # Dijkstra algorithm's greedy approach to obtaining shortest path and distance
                distanceDict[adjNode] = newDistance                                     # Update the new found shorter distance to distanceDict
                pq.put([newDistance, newPath])                                          # Enqueue based on shortest newDistance 
                
    

def begin(GDict, DistDict, start, end):
    Path, Dist = dijkstra(GDict, DistDict, start, end)
    IOParser.outputParser((Path, Dist, 0))