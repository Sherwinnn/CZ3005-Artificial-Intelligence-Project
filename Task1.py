import json
import math
from queue import PriorityQueue
import sys
import IOParser


def dijkstra(GDict, DistDict, start, end):
    
    pq = PriorityQueue()

    # push the starting index and path
    pq.put([0, [start]])

    # dictionary to keep track of visited node
    travelled = {}

    # dictionary to keep track of the node distance
    # for checking if there's another shortest path
    distanceDict = {start: sys.maxsize}
    
    # while the queue is not empty
    while pq:

        # pop the element with the highest priority
        e = pq.get()

        # get the current distance
        currentDist = e[0]

        # get the current path
        currentPath = e[1]

        # set the current node to the last node in the path
        currentNode = currentPath[-1]

        # mark current ndoe as travelled
        travelled[currentNode] = 1

        # check if current node is the endination node
        if currentNode == end:
            # return the path and the total distance from source to destination node
            return currentPath, currentDist

        # check for adjacent node
        for neighbour in GDict[currentNode]:
            
            # if the distance for this not is not initialized
            if neighbour not in distanceDict:
                # initialized the node distance
                distanceDict[neighbour] = sys.maxsize
            
            # clone current path to a new path to 
            # prevent appending to the current path
            newPath = currentPath[:]
            # append the adjacent node to the new path
            newPath.append(neighbour)

            # calculate the new distance
            newDistance = currentDist+ DistDict[min(currentNode,neighbour),max(currentNode,neighbour)]
            ##newDist = cur_dist + dist[f"{cur_node},{neighbour}"]

            # if adjacent node is not in visted and if the new distance smaller than the old distance
            if neighbour not in travelled and distanceDict[neighbour] > newDistance:
                # push adjacent node with it's distance and path into priority pq
                pq.put([newDistance, newPath])
                # update the distance of the node
                distanceDict[neighbour] = newDistance
    

def begin(GDict, DistDict, start, end):
    Path, Dist = dijkstra(GDict, DistDict, start, end)
    IOParser.outputParser((Path, Dist, 0))