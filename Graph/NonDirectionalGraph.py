class Graph:
    def __init__(self) -> None:
        self.edge = {}

    # 정점 추가
    def addVertex(self, vertex):
        self.edge[vertex] = []

    # v1 -> v2
    def addEdge(self, v1, v2):
        if v1 not in self.edge:
            self.addVertex(v1)
        if v2 not in self.edge:
            self.addVertex(v2)

        self.edge[v1].append(v2)
        self.edge[v2].append(v1)

    def removeEdge(self, v1, v2):
        # v1에서 v2삭제
        idx = self.edge[v1].index(v2)
        self.edge[v1] = self.edge[v1][:idx] + self.edge[v1][idx + 1 :]

        if len(self.edge[v1]) == 0:
            del self.edge[v1]

        # v2에서 v1 삭제
        idx = self.edge[v2].index(v1)
        self.edge[v2] = self.edge[v2][:idx] + self.edge[v2][idx + 1 :]

        if len(self.edge[v2]) == 0:
            del self.edge[v2]

    def removeVertex(self, vertex):
        # 삭제할 간선을 모두 구한다
        if self.edge[vertex] is None:
            raise Exception("해당 엣지 없음 !")

        edges = self.edge[vertex][:]

        for edge in edges:
            self.removeEdge(vertex, edge)

    def sizeVertex(self):
        return len(self.edge)

    def sizeEdge(self, vertex):
        return 0 if self.edge[vertex] is None else len(self.edge[vertex])

    def print(self):
        for vertex, edges in self.edge.items():
            if len(edges) == 0:
                continue

            print(f"{vertex} -> {''.join(edges)}")


graph = Graph()
vertices = ["A", "B", "C", "D", "E"]

for vertex in vertices:
    graph.addVertex(vertex)


graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("A", "D")
graph.addEdge("B", "F")
graph.addEdge("B", "E")
graph.addEdge("C", "G")
graph.addEdge("D", "H")
graph.addEdge("D", "G")
graph.addEdge("E", "I")
print(graph.edge)
graph.removeEdge("A", "B")
# graph.removeVertex("E")
print(graph.sizeVertex())
print(graph.sizeEdge("A"))


graph.print()
