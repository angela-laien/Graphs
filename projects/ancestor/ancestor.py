class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_parent(self, v1, v2):
        self.vertices[v1].add(v2)
    def get_parents(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return -1
    def bfs(self, starting_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        paths = []
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            last = path[-1]
            if self.get_parents(last) == -1:
                paths.append(path)
            if last not in visited:
                if self.get_parents(last) != -1:
                    parents = self.get_parents(last)
                    for p in parents:
                        next_path = path + [p]
                        q.enqueue(next_path)
        return paths

def earliest_ancestor(ancestors, starting_node):
    parents = Graph()
    for a in ancestors:
        parents.add_vertex(a[1])
    for a in ancestors:
        parents.add_parent(a[1], a[0])
    if parents.get_parents(starting_node) == -1:
        return -1
    paths = parents.bfs(starting_node)
    longest = paths[0]
    for path in paths:
        if len(path) == len(longest):
            if path[-1] < longest[-1]:
                longest = path
        if len(path) > len(longest):
            longest = path
    return (longest[-1])

# from graph import Graph

# def earliest_ancestor(ancestors, starting_node):
#     graph = Graph()
#     for i in ancestors:
#         graph.add_vertex(i[0])
#         graph.add_vertex(i[1])
#     for i in ancestors:
#         graph.add_edge(i[1], i[0])
#     answer = graph.bfs(starting_node)
#     if answer == starting_node:
#         return -1
#     else:
#         return answer