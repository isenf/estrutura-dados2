"""
Author: Dante Fabro 
Nov, 2026.
"""
# %%

import pandas as pd
import igraph as ig

# %% [markdown]

# Os dados foram extraídos do Kaggle: 
# https://www.kaggle.com/datasets/weyoungopenlab/synthetic-green-supply-chain-carbon-pricing-data
#
# Nesse projeto, optou-se por limitar à região da Europa. Ele contém 203 nós e 587 arestas.

# %%

DATA_PATH = "data/"
OUTPUT_PATH = "output"

edges = pd.read_csv(f"{DATA_PATH}/raw/edges.csv")
edges.shape # 587 arestas
edges.head()
# %%
nodes = pd.read_csv(f"{DATA_PATH}/raw/nodes.csv")
nodes.shape # 203 vértices
nodes.head()
# %%

g = ig.Graph(directed=True)
g.add_vertices(nodes["node_id"].tolist())
g.vs["name"] = nodes["node_id"].tolist()
# %%

for col in ["node_type", "isic_code","latitude", "longitude", 
            "capacity_units", "employees", "founded_year", 
            "tech_level", "size_class"]:
    g.vs[col] = nodes[col].tolist()

# %%
g.add_edges(list(zip(edges["source_id"], edges["target_id"])))
for col in ["trade_share", "logistics_freq", "tenure"]:
    g.es[col] = edges[col].tolist()
g.es["weight"] = edges["wij"].tolist()
# %%
ig.plot(g)
