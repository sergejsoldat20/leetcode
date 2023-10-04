class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):

    def __init__(self):
        clones_dict = dict()

    def cloneGraph(self, node):

        if not node:
            return node

        if node in self.clones_dict:
            return self.clones_dict[node]

        # create clone for node
        new_node = Node(node.val, [])
        self.clones_dict[node] = new_node

        new_node.neighbors = [self.cloneGraph(
            next_node) for next_node in node.neighbors]

        return new_node


sol = Solution()

# generate me five nodes and connect them by some random order in connected undirected graph
# (so that I can test my solution)
nodes = [Node(i) for i in range(5)]
nodes[0].neighbors = [nodes[1], nodes[2]]
nodes[1].neighbors = [nodes[0], nodes[3]]
nodes[2].neighbors = [nodes[0], nodes[3]]
nodes[3].neighbors = [nodes[1], nodes[2], nodes[4]]
nodes[4].neighbors = [nodes[3]]


sol.cloneGraph(nodes[0], [])
