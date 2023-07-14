import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


import heapq


def dijkstra(aGraph, start, target):
    print
    start.set_distance(0)

    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print
                'updated : current = %s next = %s new_dist = %s' \
                % (current.get_id(), next.get_id(), next.get_distance())
            else:
                print
                'not updated : current = %s next = %s new_dist = %s' \
                % (current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')
    g.add_vertex('g')
    g.add_vertex('h')
    g.add_vertex('i')

    g.add_edge('a', 'd', 5)
    g.add_edge('a', 'c', 5)
    g.add_edge('b', 'e', 5)
    g.add_edge('b', 'c', 3)
    g.add_edge('b', 'f', 3)
    g.add_edge('b', 'g', 4)
    g.add_edge('b', 'i', 5)
    g.add_edge('c', 'd', 6)
    g.add_edge('c', 'h', 3)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 2)
    g.add_edge('f', 'g', 3)
    g.add_edge('g', 'i', 3)
    g.add_edge('h', 'i', 4)



    print
    'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print
            '( %s , %s, %3d)' % (vid, wid, v.get_weight(w))

    dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))

    target = g.get_vertex('e')
    path = [target.get_id()]
    shortest(target, path)
    print
    'The shortest path : %s' % (path[::-1])