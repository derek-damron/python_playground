class Graph:
    def __init__(self, directed=False):
        self._graph = {}
        self._directed = directed
        
    def add_edge(self, node1, node2):
        # node1 -> node2
        if node1 not in self._graph.keys():
            self._graph[node1] = set()
        self._graph[node1].add(node2)
        
        # node2 -> node1 if not directed
        if not self._directed:
            if node2 not in self._graph.keys():
                self._graph[node2] = set()
            self._graph[node2].add(node1)
        
    def delete_edge(self, node1, node2):
        # node1 -> node2
        try:
            self._graph[node1].remove(node2)
        except:
            pass
        if node1 in self._graph.keys() and self._graph[node1] == set():
            del self._graph[node1]
        
        # node2 -> node1 if not directed
        if not self._directed:
            try:
                self._graph[node2].remove(node1)
            except:
                pass
            if node2 in self._graph.keys() and self._graph[node2] == set():
                del self._graph[node2]
                
    def are_connected(self, node1, node2):
        if node1 not in self._graph.keys():
            return False
        elif node2 in self._graph[node1]:
            return True
        else:
            return False
        
    def adj_list(self):
        return self._graph
        
    def find_path(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph.keys():
            return None
        for new_node in self._graph[node1]:
            if new_node not in path:
                new_path = self.find_path(new_node, node2, path)
                if new_path:
                    return new_path
        return None
        
    def find_all_paths(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph.keys():
            return None
        all_paths = []
        for new_node in self._graph[node1]:
            if new_node not in path:
                new_paths = self.find_all_paths(new_node, node2, path)
                if new_paths:
                    if isinstance(new_paths[0], list):
                        all_paths = all_paths + new_paths
                    else:
                        all_paths = all_paths + [new_paths]
        if all_paths == []:
            return None
        return all_paths
        
    def find_shortest_path(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph.keys():
            return None
        shortest_path = None
        for new_node in self._graph[node1]:
            if new_node not in path:
                new_path = self.find_shortest_path(new_node, node2, path)
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path
        return shortest_path
        
