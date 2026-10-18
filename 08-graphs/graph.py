from collections import deque


class Graph:
    """Unweighted graph as an adjacency dict. Undirected unless told otherwise."""

    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def add_node(self, node):
        self.adj.setdefault(node, [])

    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)
        self.adj[a].append(b)
        if not self.directed:
            self.adj[b].append(a)

    def bfs(self, start):
        """Nodes in the order a breadth-first search visits them."""
        seen = {start}
        order = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in self.adj[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return order

    def dfs(self, start):
        seen = set()
        order = []

        def visit(node):
            seen.add(node)
            order.append(node)
            for nxt in self.adj[node]:
                if nxt not in seen:
                    visit(nxt)

        visit(start)
        return order

    def shortest_path(self, start, goal):
        """Fewest edges from start to goal, as a list of nodes. None if unreachable."""
        parents = {start: None}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node == goal:
                break
            for nxt in self.adj[node]:
                if nxt not in parents:
                    parents[nxt] = node
                    queue.append(nxt)
        if goal not in parents:
            return None
        path = []
        while goal is not None:
            path.append(goal)
            goal = parents[goal]
        return path[::-1]

    def connected_components(self):
        seen = set()
        components = []
        for node in self.adj:
            if node not in seen:
                part = self.bfs(node)
                seen.update(part)
                components.append(sorted(part))
        return components
