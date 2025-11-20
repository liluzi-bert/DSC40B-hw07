def cluster(graph, weights, level):
    """
    Return the clusters of an undirected, weighted graph at the given level.

    Parameters
    ----------
    graph   : dsc40graph.UndirectedGraph
        The underlying (unweighted) graph. DO NOT modify this.
    weights : function
        A function weights(u, v) that returns the weight of edge (u, v).
    level   : number
        Threshold λ. Edges with weight < level are treated as removed.

    Returns
    -------
    frozenset of frozensets
        Each inner frozenset is the set of vertices in one cluster
        (a connected component after removing all edges whose
         weight is < level).
    """
    visited = set()
    clusters = []

    # graph.nodes is a *view* of all node labels in the graph
    for start in graph.nodes:
        if start in visited:
            continue

        # Explore the component containing `start`,
        # but only along edges with weight >= level.
        stack = [start]          # DFS with an explicit stack
        visited.add(start)
        component = {start}

        while stack:
            u = stack.pop()
            for v in graph.neighbors(u):
                if weights(u, v) >= level and v not in visited:
                    visited.add(v)
                    component.add(v)
                    stack.append(v)

        clusters.append(frozenset(component))

    return frozenset(clusters)
