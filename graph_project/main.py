"""
Author: Dante Fabro 
Nov, 2026.
"""
# %%

import pandas as pd
import igraph as ig
import matplotlib.pyplot as plt
import networkx as nx

# %% [markdown]

# https://zenodo.org/records/17375854 \
# Tleuken, A., Rogetzer, P., Fraccascia, L. et al. From atoms to allies: a social network analysis of information and resource exchange in hubs for circularity. J. Ind. Ecol. 30, 505–520 (2026). https://doi.org/10.1007/s44498-026-00034-y

# %%

DATA_PATH = "data/"
OUTPUT_PATH = "output"
COLORS = {
    "Industry": "#ff6a49",
    "Research": "#40cdc4",
    "Community": "#fcbb00",
    "Regulatory": "#fff4d6",
    "Resource": "#0066a8"
}

# %%

edges = pd.read_csv(f"{DATA_PATH}/raw/edgedata.csv")
edges.shape # 396 arestas
edges.head()
edges["type"].unique()
# %%
nodes = pd.read_csv(f"{DATA_PATH}/raw/nodes.csv")
nodes.shape # 97 vértices
nodes.head()
# %%

# way to treat NaN values in category (resources does not have 'category')
nodes["cat_full"] = nodes.apply(
    lambda r: r["category"] if pd.notna(r["category"]) else r["type"], axis=1
)

# %%

# communication net -> undirected
comm_edges = edges[edges["type"]=="Communication"]
g_comm = ig.Graph(directed=False)
g_comm.add_vertices(nodes["id_code"].tolist())
g_comm.add_edges(list(zip(comm_edges["source"], comm_edges["target"])))
g_comm.vs["category"] = nodes["cat_full"].tolist()
g_comm.vs["hub"] = nodes["hub"].tolist()

g_comm.delete_vertices([v.index for v in g_comm.vs if g_comm.degree(v.index) == 0])
ig.plot(g_comm)

# %%

# resources net -> directed
res_e = edges[edges["type"].isin(["Symbiosis", "Use", "Production"])]
g_res =ig.Graph(directed=True)
g_res.add_vertices(nodes["id_code"].tolist())
g_res.add_edges(list(zip(res_e["source"], res_e["target"])))
g_res.es["etype"] = res_e["type"].tolist()
g_res.vs["category"] = nodes["cat_full"].tolist()
g_res.vs["hub"] = nodes["hub"].tolist()

g_res.delete_vertices([v.index for v in g_res.vs if g_res.degree(v.index, mode="all") == 0])
ig.plot(g_res)

# %%

def draw_graph(
    g: ig.Graph,
    title: str,
    directed: bool=False,
    figsize: tuple[float, float]=(14, 10)
):
    arrow_size = 0.6 if directed else 0
    fig, ax = plt.subplots(figsize=figsize)
    layout = g.layout_fruchterman_reingold(niter=500)
    vcolor = [COLORS.get(c, "'#999999") for c in g.vs["category"]]
    ig.plot(g, target=ax, layout=layout,
            vertex_color=vcolor,
            vertex_label=None,
            vertex_frame_color="black", 
            edge_color="#888888", 
            edge_width=1.0,
            edge_arrow_width=.45,
            edge_arrow_size=arrow_size,
            margin=40,
            edge_curved=0.0
            )
    handles = [plt.Line2D([0],[0], marker="o", color="w", markerfacecolor=c,
                          markersize=12, label=k) for k, c in COLORS.items()]
    ax.legend(handles=handles, loc="upper left", title="Category", frameon=True)
    ax.set_title(title)
    fig.tight_layout()
    return fig
# %%
draw_graph(g_res, title="AAAAA", directed=True)

# %%
# g_res_nx = g_res.to_networkx()
# nx.draw(g_res_nx)
