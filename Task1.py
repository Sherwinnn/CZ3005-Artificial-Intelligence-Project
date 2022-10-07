class Node:
    def __init__(self, id, parent, dist, cost):
        self.id = id
        self.parent = parent  
        self.dist = dist
        self.cost = cost
    # to sort nodes in pqueue based on total distance
    def __lt__(self, next):
        return self.dist < next.dist

def dijkstra(GDict, start, end):
    return
    


def begin(GDict, start, end):
    pass
    # path, cost, numvisited = dijkstra(GDict,start,end)

    # print()