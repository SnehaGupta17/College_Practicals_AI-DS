import numpy as np

class Node:
    def __init__(self):
        self.dist = [0] * 20
        self.from_node = [0] * 20

route = [Node() for _ in range(10)]

def main():
    dm = np.zeros((20, 20), dtype=int)
    no = int(input("Enter no of nodes.\n"))
    print("Enter the distance matrix:")
    
    for i in range(no):
        for j in range(no):
            dm[i][j] = int(input())
            dm[i][i] = 0  # Set distance from i to i as 0
            route[i].dist[j] = dm[i][j]
            route[i].from_node[j] = j

    flag = True
    while flag:
        flag = False
        for i in range(no):
            for j in range(no):
                for k in range(no):
                    if route[i].dist[j] > route[i].dist[k] + route[k].dist[j]:
                        route[i].dist[j] = route[i].dist[k] + route[k].dist[j]
                        route[i].from_node[j] = k
                        flag = True

    for i in range(no):
        print(f"Router info for router: {i + 1}")
        print("Dest\tNext Hop\tDist")
        for j in range(no):
            print(f"{j + 1}\t{route[i].from_node[j] + 1}\t\t{route[i].dist[j]}")

if __name__ == "__main__":
    main()

