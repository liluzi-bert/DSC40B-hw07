def cluster(graph, weights, level):
    """
    Return the clusters of an undirected, weighted graph at the given level.

    Parameters
    
    graph   : dsc40graph.UndirectedGraph
        The underlying (unweighted) graph. DO NOT modify this.
    weights : function
        A function weights(u, v) that returns the weight of edge (u, v).
    level   : number
        Threshold λ. Edges with weight < level are treated as removed.

    Returns

    frozenset of frozensets
        Each inner frozenset is the set of vertices in one cluster
        (a connected component after removing all edges whose
         weight is < level).
    """
    visited = set()
    clusters = []

    # Go through every vertex; start a BFS/DFS from each unvisited one.
    for start in graph.vertices():
        if start in visited:
            continue

        # Explore the component containing `start`,
        # but only following edges with weight >= level.
        stack = [start]       # can use stack or queue; doesn't matter
        visited.add(start)
        component = {start}

        while stack:
            u = stack.pop()
            for v in graph.neighbors(u):
                # Only traverse "strong-enough" edges
                if weights(u, v) >= level and v not in visited:
                    visited.add(v)
                    component.add(v)
                    stack.append(v)

        # One cluster finished
        clusters.append(frozenset(component))

    return frozenset(clusters)
