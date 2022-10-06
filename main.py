import json
import Task1
import Task2
import Task3

if __name__ == '__main__':
    start = '1'
    end = '50'
    budget = 287932

    with open('G.json') as f:
        G = json.load(f)
    with open('Dist.json') as f:
        Dist = json.load(f)
    with open('Cost.json') as f:
        Cost = json.load(f)
    with open('Coord.json') as f:
        Coord = json.load(f)
    
    print("Starting Task 1... \n")
    Task1.begin(start,end)

    print("Starting Task 2... \n")
    Task2.begin(start,end)

    print("Starting Task 2... \n")
    Task3.begin(start,end)


    




