"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex Does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex)

        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push a starting vertex
        s = Stack()
        s.push(starting_vertex)

        # create a set to store the visited vertices
        visited = set()

        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()

            # if vertex has not been visited:
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of its neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            last = path[-1]

            if last not in visited:
                visited.add(last)
                neighbors = self.get_neighbors(last)

                for neighbor in neighbors:
                    next_path = path.copy()
                    next_path.append(neighbor)

                    if neighbor == destination_vertex:
                        return next_path
                    q.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()

        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()
            last = path[-1]

            if last in visited:
                continue
            else:
                visited.add(last)
                neighbors = self.get_neighbors(last)

                for neighbor in neighbors:
                    next_path = path.copy()
                    next_path.append(neighbor)

                    if neighbor == destination_vertex:
                        return next_path
                    s.push(next_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()

        def dft(path):
            last = path[-1]

            if last in visited:
                return None
            else:
                visited.add(last)

            if last == destination_vertex:
                return path

            neighbors = self.get_neighbors(last)
            for neighbor in neighbors:
                next_path = path.copy()
                next_path.append(neighbor)

                target = dft(next_path)
                if target:
                    return target
            
            return None
        
        return dft([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
