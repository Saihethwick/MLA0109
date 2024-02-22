class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: set() for v in vertices}
        self.colors = {}

    def add_edge(self, u, v):
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)

    def greedy_coloring(self):
        colors = {}
        for vertex in self.vertices:
            used_colors = {colors[self.colors[neighbor]] for neighbor in self.adj_list[vertex] if neighbor in self.colors}
            for color in range(len(self.vertices)):
                if color not in used_colors:
                    colors[vertex] = color
                    break
        self.colors = colors

# Example usage:
regions = ['A', 'B', 'C', 'D', 'E']
graph = Graph(regions)

# Add adjacency between regions
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')

# Perform greedy coloring
graph.greedy_coloring()

# Print the coloring
for region, color in graph.colors.items():
    print(f"Region {region} is colored with color {color}")
