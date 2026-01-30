import networkx as nx
import matplotlib.pyplot as plt
import itertools


def load_graph(f):
    g = nx.drawing.nx_agraph.read_dot(f)
    mapping = {
        n: data["label"]
        for n, data in g.nodes(data=True)
    }

    g=nx.relabel_nodes(g, mapping, copy=False)
    return g


def n_hop_subgraph(G, source, N):
    nodes = nx.single_source_shortest_path_length(G.to_undirected(), source, cutoff=N)
    return G.subgraph(nodes.keys())
def ancestors_and_n_hops(G, source, Nhops):
    return G.subgraph(set(nx.single_source_shortest_path_length(G.to_undirected(), source, cutoff=Nhops).keys()).union(nx.descendants(G, source)))
def ancestors_up_to(G, source, N):
    return G.subgraph(nx.single_source_shortest_path_length(G, source, cutoff=N).keys())

def plot(Gp, figsize=(10, 8), pos=None):
    if pos is None:
        pos = nx.nx_agraph.pygraphviz_layout(Gp, prog="dot")

    fig=plt.figure(figsize=figsize)
    nx.draw(
        Gp,
        pos,
        with_labels=True,
        labels={key: node_data["label"]+"\n"+node_data["tooltip"] for key, node_data in Gp.nodes(data=True)},
        node_size=2000,
        node_color="lightgreen",
        arrows=True,
        node_shape="s"
    )
    return fig