"""
Author: Dante Fabro 
Nov, 2026.
"""
# %%

import pandas as pd
import igraph as ig

# %% [markdown]

# https://zenodo.org/records/17375854 \
# Tleuken, A., Rogetzer, P., Fraccascia, L. et al. From atoms to allies: a social network analysis of information and resource exchange in hubs for circularity. J. Ind. Ecol. 30, 505–520 (2026). https://doi.org/10.1007/s44498-026-00034-y

# %%

DATA_PATH = "data/"
OUTPUT_PATH = "output"

edges = pd.read_csv(f"{DATA_PATH}/raw/edgedata.csv")
edges.shape # 396 arestas
edges.head()
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

