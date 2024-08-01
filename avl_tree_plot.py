import networkx as nx
import matplotlib.pyplot as plt


def build_graph(root, g):
    
    if root:
        g.add_node(root.key)
        if root.left:
            g.add_edge(root.key, root.left.key)
            build_graph(root.left, g)
        if root.right:
            g.add_edge(root.key, root.right.key)
            build_graph(root.right, g)


def calculate_positions(node, level, position, x_spacing, group_spacing, g):
    pos = {}
    if node is not None:
        x = position * x_spacing
        y = -level
        pos[node.key] = (x, y)

        left_width = get_subtree_width(node.left, g)
        right_width = get_subtree_width(node.right, g)

        left_pos = calculate_positions(node.left, level + 1, position - left_width - group_spacing / 2, x_spacing,
                                       group_spacing, g)
        right_pos = calculate_positions(node.right, level + 1, position + right_width + group_spacing / 2, x_spacing,
                                        group_spacing, g)
        pos.update(left_pos)
        pos.update(right_pos)

    return pos


def get_subtree_width(root, g):
    if root is None:
        return 0
    return get_subtree_width(root.left, g) + 1 + get_subtree_width(root.right, g)


def plot_tree(root, x_spacing=0.5, group_spacing=0.3, title=None):
    g = nx.Graph()
    build_graph(root, g)
    pos = calculate_positions(root, 0, 0, x_spacing, group_spacing, g)

    plt.figure(figsize=(8, 6))

    if title:
        plt.title(title)

    nx.draw(g, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black")
    plt.show()
