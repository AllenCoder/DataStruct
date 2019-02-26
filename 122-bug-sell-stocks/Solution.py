class Solution:

    def __init__(self):
        self.visited = []

    def BFS(self, graph, start, end):
        queue = []

        queue.append([start])
        self.visited.add(start)

        while queue:
            node = queue.pop()
            self.visited.add(node)
            process(node)

            nodes = generate_related_nodes(node)
            queue.push(nodes)
