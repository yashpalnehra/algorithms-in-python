import heapq


def dijkstra(adj, source):
    """Cheapest distance from source to every node. adj: node to [(neighbour, weight)]."""
    dist = {source: 0}
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        # stale entry, a shorter route was already found
        if d > dist.get(node, float("inf")):
            continue
        for nxt, w in adj.get(node, []):
            new = d + w
            if new < dist.get(nxt, float("inf")):
                dist[nxt] = new
                heapq.heappush(heap, (new, nxt))
    return dist


def topological_sort(adj):
    """Order the nodes of a DAG so every edge points forward (Kahn's algorithm)."""
    indegree = {node: 0 for node in adj}
    for targets in adj.values():
        for t in targets:
            indegree[t] = indegree.get(t, 0) + 1
    ready = sorted(n for n, d in indegree.items() if d == 0)
    order = []
    while ready:
        node = ready.pop(0)
        order.append(node)
        for t in adj.get(node, []):
            indegree[t] -= 1
            if indegree[t] == 0:
                ready.append(t)
    if len(order) != len(indegree):
        raise ValueError("graph has a cycle")
    return order


def has_cycle(adj):
    """Cycle check for a directed graph by DFS colouring."""
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {node: WHITE for node in adj}
    for targets in adj.values():
        for t in targets:
            colour.setdefault(t, WHITE)

    def visit(node):
        colour[node] = GREY
        for t in adj.get(node, []):
            if colour[t] == GREY or (colour[t] == WHITE and visit(t)):
                return True
        colour[node] = BLACK
        return False

    return any(colour[n] == WHITE and visit(n) for n in list(colour))
