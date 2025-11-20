def biggest_descendent(graph, root, value):
    """
    graph  : a dsc40graph.DirectedGraph representing a rooted tree
    root   : label of the root node
    value  : dict mapping each node to its value

    Returns:
        dict mapping each node u to the largest value of any
        node in the subtree rooted at u (including u itself).
    """
    biggest = {}

    def dfs(u):
        # Start with this node's own value
        current_max = value[u]

        # Recurse on all children (outgoing neighbors)
        for v in graph.neighbors(u):
            child_max = dfs(v)
            if child_max > current_max:
                current_max = child_max

        # Store result for this node and return it
        biggest[u] = current_max
        return current_max

    dfs(root)
    return biggest
