import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#999999"
        self.id = str(uuid.uuid4())

def build_heap_tree(heap):
    if not heap:
        return None
    nodes = [Node(v) for v in heap]
    for i in range(len(nodes)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(nodes):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(nodes):
            nodes[i].right = nodes[right_idx]
    return nodes[0]

def add_edges(G, node, pos, x=0, y=0, layer=1):
    if node:
        G.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            G.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(G, node.left, pos, l, y - 1, layer + 1)
        if node.right:
            G.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(G, node.right, pos, r, y - 1, layer + 1)
    return G

def draw_colored_tree(root, title=""):
    G = nx.DiGraph()
    pos = {root.id: (0, 0)}
    G = add_edges(G, root, pos)
    node_colors = [G.nodes[n]['color'] for n in G.nodes]
    labels = {n: G.nodes[n]['label'] for n in G.nodes}
    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(G, pos, labels=labels, arrows=False, node_color=node_colors, node_size=2500)
    plt.show()

def hex_blue_gradient(n):
    return [to_hex((i/n, i/n, 1.0)) for i in range(n)]

def bfs_coloring(root):
    queue = [root]
    visited = []
    color_list = hex_blue_gradient(100)
    idx = 0
    while queue:
        current = queue.pop(0)
        current.color = color_list[idx]
        idx += 1
        visited.append(current)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

def dfs_coloring(root):
    stack = [root]
    visited = []
    color_list = hex_blue_gradient(100)
    idx = 0
    while stack:
        current = stack.pop()
        if current not in visited:
            current.color = color_list[idx]
            idx += 1
            visited.append(current)
            if current.right: stack.append(current.right)
            if current.left: stack.append(current.left)

heap_array = [1, 3, 5, 7, 9, 8, 10]

# BFS
root_bfs = build_heap_tree(heap_array)
bfs_coloring(root_bfs)
draw_colored_tree(root_bfs, "Обхід у ширину (BFS)")

# DFS
root_dfs = build_heap_tree(heap_array)
dfs_coloring(root_dfs)
draw_colored_tree(root_dfs, "Обхід у глибину (DFS)")
