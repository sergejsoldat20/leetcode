import sys


class Graph():

    # definisi graf sa n cvorova, veze reprezentovane kao matrice
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for ccolumn in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # funkcija koja ce vratiit cvor sa mininalnom vrijednosti distance
    # iz seta cvorova koji nisu ukljuceni u stablo najkracih putanja
    def minDistance(self, dist, sptSet):

        # inicijalizujemo distancu za sledeci cvor kao beskonacnost
        min = sys.maxsize
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Dijkstra algoritam najkracih putanja
    def dijkstra(self, src):

        # za svaki cvor setujemo vrijednost na beskonacno
        dist = [sys.maxsize] * self.V
        # postavimo prvu vrijednost na 0 za prvi cvor
        dist[src] = 0
        # stablo najkracih putanja, shortest path tree set
        sptSet = [False] * self.V

        for cout in range(self.V):

            # uzmemo cvor sa najmanjom distancom
            # x je uvijek src u prvoj iteraciji
            x = self.minDistance(dist, sptSet)

            # dodaj cvor sa najmanjom distancom u stablo najkracih
            # putanja
            sptSet[x] = True

            #
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False \
                        and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)


# Driver's code
if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)

# This code is contributed by Divyanshu Mehta and Updated by Pranav Singh Sambyal
