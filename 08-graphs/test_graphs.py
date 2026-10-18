import pytest

from graph import Graph
from weighted import dijkstra, has_cycle, topological_sort


@pytest.fixture
def g():
    g = Graph()
    for a, b in [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (6, 7)]:
        g.add_edge(a, b)
    return g


def test_bfs_order(g):
    assert g.bfs(1) == [1, 2, 3, 4, 5]


def test_dfs_order(g):
    assert g.dfs(1) == [1, 2, 4, 3, 5]


def test_shortest_path(g):
    assert g.shortest_path(1, 5) in ([1, 2, 4, 5], [1, 3, 4, 5])
    assert g.shortest_path(1, 1) == [1]
    assert g.shortest_path(1, 7) is None


def test_connected_components(g):
    g.add_node(8)
    assert g.connected_components() == [[1, 2, 3, 4, 5], [6, 7], [8]]


def test_directed_edges_go_one_way():
    g = Graph(directed=True)
    g.add_edge("a", "b")
    assert g.bfs("a") == ["a", "b"]
    assert g.bfs("b") == ["b"]


def test_dijkstra():
    adj = {
        "a": [("b", 7), ("c", 9), ("f", 14)],
        "b": [("c", 10), ("d", 15)],
        "c": [("d", 11), ("f", 2)],
        "d": [("e", 6)],
        "f": [("e", 9)],
    }
    assert dijkstra(adj, "a") == {"a": 0, "b": 7, "c": 9, "f": 11, "d": 20, "e": 20}
    assert dijkstra(adj, "e") == {"e": 0}


def test_topological_sort():
    adj = {
        "shirt": ["tie", "belt"],
        "tie": ["jacket"],
        "trousers": ["belt"],
        "belt": ["jacket"],
    }
    order = topological_sort(adj)
    assert set(order) == {"shirt", "tie", "belt", "jacket", "trousers"}
    for src, targets in adj.items():
        for t in targets:
            assert order.index(src) < order.index(t)


def test_topological_sort_rejects_cycle():
    with pytest.raises(ValueError):
        topological_sort({"a": ["b"], "b": ["a"]})


def test_has_cycle():
    assert not has_cycle({"a": ["b"], "b": ["c"], "c": []})
    assert has_cycle({"a": ["b"], "b": ["c"], "c": ["a"]})
    assert has_cycle({"a": ["a"]})
    assert not has_cycle({})
