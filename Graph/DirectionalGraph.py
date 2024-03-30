import copy
from collections import deque


class Graph:
    def __init__(self) -> None:
        self.edge = {}
        self.visited = {}

    # 정점 추가
    def addVertex(self, vertex):
        self.edge[vertex] = []
        self.visited[vertex] = False

    # v1 -> v2
    def addEdge(self, v1, v2):
        self.edge[v1].append(v2)
        self.visited[v1] = False

    def removeEdge(self, target, edge):
        # 삭제하고자 하는 엣지의 인덱스를 찾는다
        idx = self.edge[target].index(edge)
        # 해당 인덱스의 값의 엣지를 삭제
        self.edge[target] = self.edge[target][:idx] + self.edge[target][idx + 1 :]

        if len(self.edge[target]) == 0:
            del self.edge[target]

    def removeVertex(self, vertex):
        # 삭제할 간선을 모두 구한다
        if self.edge[vertex] == None:
            raise Exception("해당 엣지 없음 !")

        edges = self.edge[vertex][:]

        for edge in edges:
            self.removeEdge(vertex, edge)

    def sizeVertex(self):
        return len(self.edge)

    def sizeEdge(self, vertex):
        return 0 if self.edge[vertex] == None else len(self.edge[vertex])

    def print(self):
        for vertex, edges in self.edge.items():
            if len(edges) == 0:
                continue

            print(f"{vertex} -> {''.join(edges)}")

    def dfs_recursion(self, startVertex, visited):
        def _recursion_dfs(startVertex, visited):
            if visited[startVertex]:
                return

            # 명령절차 : 방문했을때 무엇을 할래
            # 종료조건을 만들었으니 그에 대응되도록
            visited[startVertex] = True
            print(startVertex)

            for vertex in self.edge[startVertex]:
                _recursion_dfs(vertex, visited)

        _recursion_dfs(startVertex, copy.copy(self.visited))

    def dfs_stack(self, startVertex, visited):
        stack = []
        stack.append(startVertex)

        while len(stack) != 0:
            vertex = stack.pop()
            if visited[vertex]:
                continue
            # 방문했을때 무엇을 해야하는가 ?
            # 1. 방문처리
            # 2. 로직수행
            visited[vertex] = True
            print(vertex)

            for vertex in reversed(self.edge[vertex]):
                stack.append(vertex)

    def bfs(self, startVertex, visited):
        dq = deque()
        dq.append(startVertex)

        while len(dq) != 0:
            vertex = dq.popleft()

            if visited[vertex]:
                continue
            visited[vertex] = True
            print(vertex)

            for vertex in self.edge[vertex]:
                dq.append(vertex)

    def bfs_path_info(self, startVertex, visited):
        # 기준 : {**startVertex**}  부터 인접노드들의 거리
        dq = deque()
        distance = {}
        pre_visit = {}

        for vertex in self.edge.keys():
            distance[vertex] = 0
            pre_visit[vertex] = None

        dq.append(startVertex)
        while len(dq) != 0:
            prev = dq.popleft()
            if visited[prev]:
                continue

            visited[prev] = True

            for adj_vertex in self.edge[prev]:
                distance[adj_vertex] = distance[prev] + 1
                pre_visit[adj_vertex] = prev
                dq.append(adj_vertex)

        return distance, pre_visit

    # from vertext에서 to vertex로까지 최단경로 출력
    def _from_to_path(self, pre_visit, from_, to):
        stack = []

        vertex = to
        while vertex != from_:
            stack.append(vertex)
            vertex = pre_visit[vertex]

        # vertex가 from이 됐을때 안들어감
        stack.append(from_)

        while len(stack) != 0:
            vetext = stack.pop()
            print(f"{vetext} ->", end="")

        print("end")

    def shortest_path(self, startVertex):
        distance, pre_visit = self.bfs_path_info(startVertex, copy.copy(self.visited))

        print("distance : ", distance)
        print("pre_visit : ", pre_visit)

        for vertex in self.edge.keys():
            if vertex == startVertex:
                continue

            self._from_to_path(pre_visit, startVertex, vertex)


graph = Graph()
vertices = ["A", "B", "C", "D", "E", "F", "H", "G", "I"]

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
# graph.removeEdge("E", "I")
# graph.removeVertex("E")
# print(graph.sizeVertex())
# print(graph.sizeEdge("A"))
# graph.print()

# print(graph.edge)
# graph.dfs_recursion("A", copy.copy(graph.visited))
# graph.dfs_stack("A", copy.copy(graph.visited))
graph.shortest_path("A")
# graph.bfs("A", copy.copy(graph.visited))
