import json
import math
from queue import PriorityQueue
import sys
import IOParser


def dijkstra(GDict, DistDict, start, end):
    
    pq = PriorityQueue()
    pq.put([0, [start]])

    distanceDict = {start: sys.maxsize}
    travelledDict = {}
    
    while pq:
        FirstNode = pq.get()
        currentDist = FirstNode[0]
        currentPath = FirstNode[1]
        currentNode = currentPath[-1]
        travelledDict[currentNode] = 1

        if currentNode == end:
            return currentPath, currentDist

        for neighbour in GDict[currentNode]:
            if neighbour not in distanceDict:
                distanceDict[neighbour] = sys.maxsize

            newPath = currentPath[:]
            newPath.append(neighbour)
            newDistance = currentDist+ DistDict[min(currentNode,neighbour),max(currentNode,neighbour)]

            if neighbour not in travelledDict and distanceDict[neighbour] > newDistance:
                pq.put([newDistance, newPath])
                distanceDict[neighbour] = newDistance
    

def begin(GDict, DistDict, start, end):
    Path, Dist = dijkstra(GDict, DistDict, start, end)
    IOParser.outputParser((Path, Dist, 0))