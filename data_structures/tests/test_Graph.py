import pytest
from Graph import *

#####
# Create graph
#

@pytest.fixture()
def g0():
    g = Graph()
    return g

class Test_create_node(object):
    def test_type(self, g0):
        assert isinstance(g0, Graph)
        
    def test_graph(self, g0):
        assert g0._graph == {}

    def test_directed(self, g0):
        assert g0._directed == False

#####
# Basic undirected
#

@pytest.fixture()
def gu():
    gu = Graph()
    gu.add_edge('a', 'b')
    gu.add_edge('b', 'c')
    return gu

class Test_undirected_graph(object):
    def test_graph(self, gu):
        assert gu._graph == {'a': {'b'}, 'b': {'a', 'c'}, 'c': {'b'}}
        
    def test_delete_edge(self, gu):
        gu.delete_edge('a', 'b')
        assert gu._graph == {'b': {'c'}, 'c': {'b'}}
        
    def test_delete_all_edges(self, gu):
        gu.delete_edge('a', 'b')
        gu.delete_edge('b', 'c')
        assert gu._graph == {}
        
    def test_delete_nonexistent_edge(self, gu):
        gu.delete_edge('a', 'c')
        assert gu._graph == {'a': {'b'}, 'b': {'a', 'c'}, 'c': {'b'}}
        
    def test_delete_edge_with_nonexistent_node1(self, gu):
        gu.delete_edge('d', 'a')
        assert gu._graph == {'a': {'b'}, 'b': {'a', 'c'}, 'c': {'b'}}

    def test_delete_edge_with_nonexistent_node2(self, gu):
        gu.delete_edge('a', 'd')
        assert gu._graph == {'a': {'b'}, 'b': {'a', 'c'}, 'c': {'b'}}
        
    def test_are_connected_true(self, gu):
        assert gu.are_connected('a', 'b') == True
        
    def test_are_connected_true_symmetric(self, gu):
        assert gu.are_connected('b', 'a') == True
        
    def test_are_connected_false(self, gu):
        assert gu.are_connected('a', 'c') == False
        
    def test_are_connected_false_nonexistent_node1(self, gu):
        assert gu.are_connected('d', 'a') == False
        
    def test_are_connected_false_nonexistent_node2(self, gu):
        assert gu.are_connected('a', 'd') == False

#####
# Basic directed
#

@pytest.fixture()
def gd():
    gd = Graph(directed = True)
    gd.add_edge('a', 'b')
    gd.add_edge('b', 'c')
    return gd

class Test_directed_graph(object):
    def test_graph(self, gd):
        assert gd._graph == {'a': {'b'}, 'b': {'c'}}
        
    def test_delete_edge(self, gd):
        gd.delete_edge('a', 'b')
        assert gd._graph == {'b': {'c'}}
        
    def test_delete_all_edges(self, gd):
        gd.delete_edge('a', 'b')
        gd.delete_edge('b', 'c')
        assert gd._graph == {}
        
    def test_delete_nonexistent_edge(self, gd):
        gd.delete_edge('a', 'c')
        assert gd._graph == {'a': {'b'}, 'b': {'c'}}
        
    def test_delete_edge_with_nonexistent_node1(self, gd):
        gd.delete_edge('d', 'a')
        assert gd._graph == {'a': {'b'}, 'b': {'c'}}

    def test_delete_edge_with_nonexistent_node2(self, gd):
        gd.delete_edge('a', 'd')
        assert gd._graph == {'a': {'b'}, 'b': {'c'}}
        
    def test_are_connected_true(self, gd):
        assert gd.are_connected('a', 'b') == True
        
    def test_are_connected_false_symmetric(self, gd):
        assert gd.are_connected('b', 'a') == False
        
    def test_are_connected_false(self, gd):
        assert gd.are_connected('a', 'c') == False
        
    def test_are_connected_false_nonexistent_node1(self, gd):
        assert gd.are_connected('d', 'a') == False
        
    def test_are_connected_false_nonexistent_node2(self, gd):
        assert gd.are_connected('a', 'd') == False

#####
# find_path
#

@pytest.fixture()
def gfu():
    gfu = Graph()
    gfu.add_edge('a', 'b')
    gfu.add_edge('b', 'c')
    gfu.add_edge('c', 'd')
    return gfu

class Test_find_path_undirected(object):
    def test_graph(self, gfu):
        assert gfu._graph == {'a': {'b'}, 'b': {'a', 'c'}, 'c': {'b', 'd'}, 'd': {'c'}}
        
    def test_find_path_forward(self, gfu):
        assert gfu.find_path('a', 'b') == ['a', 'b']
        
    def test_find_path_backward(self, gfu):
        assert gfu.find_path('a', 'd') == ['a', 'b', 'c', 'd']
        
    def test_find_path_missing_node1(self, gfu):
        assert gfu.find_path('e', 'a') is None
        
    def test_find_path_missing_node2(self, gfu):
        assert gfu.find_path('a', 'e') is None

@pytest.fixture()
def gfd():
    gfd = Graph(directed = True)
    gfd.add_edge('a', 'b')
    gfd.add_edge('b', 'c')
    gfd.add_edge('c', 'd')
    return gfd

class Test_find_path_directed(object):
    def test_graph(self, gfd):
        assert gfd._graph == {'a': {'b'}, 'b': {'c'}, 'c': {'d'}}
        
    def test_find_path_forward(self, gfd):
        assert gfd.find_path('a', 'd') == ['a', 'b', 'c', 'd']        
        
    def test_find_path_backward(self, gfd):
        assert gfd.find_path('d', 'a') is None
        
    def test_find_path_missing_node1(self, gfd):
        assert gfd.find_path('e', 'a') is None
        
    def test_find_path_missing_node2(self, gfd):
        assert gfd.find_path('a', 'e') is None
        
#####
# find_all_paths
#

@pytest.fixture()
def gau():
    gau = Graph()
    gau.add_edge('a', 'b')
    gau.add_edge('b', 'c')
    gau.add_edge('c', 'd')
    gau.add_edge('d', 'a')
    return gau

class Test_find_all_paths_undirected(object):
    def test_graph(self, gau):
        assert gau._graph == {'a': {'b', 'd'}, 'b': {'a', 'c'}, 'c': {'b', 'd'}, 'd': {'c', 'a'}}
        
    def test_find_all_paths_forward(self, gau):
        assert gau.find_all_paths('a', 'd') == [['a', 'b', 'c', 'd'], ['a', 'd']]
        
    def test_find_all_paths_backward(self, gau):
        assert gau.find_all_paths('d', 'a') == [['d', 'a'], ['d', 'c', 'b', 'a']]
        
    def test_find_all_paths_missing_node1(self, gau):
        assert gau.find_all_paths('e', 'a') is None
        
    def test_find_all_paths_missing_node2(self, gau):
        assert gau.find_all_paths('a', 'e') is None

@pytest.fixture()
def gad():
    gad = Graph(directed = True)
    gad.add_edge('a', 'b')
    gad.add_edge('b', 'c')
    gad.add_edge('c', 'd')
    gad.add_edge('d', 'a')
    return gad

class Test_find_all_paths_directed(object):
    def test_graph(self, gad):
        assert gad._graph == {'a': {'b'}, 'b': {'c'}, 'c': {'d'}, 'd': {'a'}}
        
    def test_find_all_paths_forward(self, gad):
        assert gad.find_all_paths('a', 'd') == [['a', 'b', 'c', 'd']]
        
    def test_find_all_paths_backward(self, gad):
        assert gad.find_all_paths('d', 'a') == [['d', 'a']]
        
    def test_find_all_paths_missing_node1(self, gad):
        assert gad.find_all_paths('e', 'a') is None
        
    def test_find_all_paths_missing_node2(self, gad):
        assert gad.find_all_paths('a', 'e') is None
        
#####
# find_shortest_path
#

@pytest.fixture()
def gsu():
    gsu = Graph()
    gsd.add_edge('a', 'b')
    gsd.add_edge('b', 'c')
    gsd.add_edge('a', 'c')
    gsd.add_edge('c', 'd')
    return gsu

class Test_find_shortest_path_undirected(object):
    def test_graph(self, gsu):
        assert gsu._graph == {'a': {'b', 'c'}, 'b': {'a', 'c'}, 'c': {'a', 'b', 'd'}, 'd': {'c'}}
        
    def test_find_shortest_path_forward(self, gsu):
        assert gsu.find_shortest_path('a', 'd') == ['a', 'c', 'd']
        
    def test_find_shortest_path_backward(self, gsu):
        assert gsu.find_shortest_path('d', 'a') == ['d', 'c', 'a']
        
    def test_find_shortest_path_missing_node1(self, gsu):
        assert gsu.find_shortest_path('e', 'a') is None
        
    def test_find_shortest_path_missing_node2(self, gsu):
        assert gsu.find_shortest_path('a', 'e') is None

@pytest.fixture()
def gsd():
    gsd = Graph(directed = True)
    gsd.add_edge('a', 'b')
    gsd.add_edge('b', 'c')
    gsd.add_edge('a', 'c')
    gsd.add_edge('c', 'd')
    return gsd

class Test_find_shortest_path_directed(object):
    def test_graph(self, gsd):
        assert gsd._graph == {'a': {'b', 'c'}, 'b': {'c'}, 'c': {'d'}}
        
    def test_find_shortest_path_forward(self, gsd):
        assert gsd.find_shortest_path('a', 'd') == ['a', 'c', 'd']
        
    def test_find_shortest_path_backward(self, gsd):
        assert gsd.find_shortest_path('d', 'a') is None
        
    def test_find_shortest_path_missing_node1(self, gsd):
        assert gsd.find_shortest_path('e', 'a') is None
        
    def test_find_shortest_path_missing_node2(self, gsd):
        assert gsd.find_shortest_path('a', 'e') is None