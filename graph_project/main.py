"""
Author: Dante Fabro 
Nov, 2026.
"""
# %%

import pandas as pd
import igraph as ig
import matplotlib.pyplot as plt
import networkx as nx
from typing import Literal

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
edges["type"].unique()
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

# %%

# P1: Quantos recursos realmente circulam?
def neighbors_by_edge(
    g: ig.Graph, 
    node_name: str,
    etype: str,
    direction: Literal["in", "out"] 
): 
    try:
        idx = g.vs.find(name=node_name).index
    except ValueError:
        return 0.0
    return sum(1.0 for e in g.incident(idx, mode=direction)
               if g.es[e]["etype"] == etype)

table = []
for v in g_res.vs:
    if v["category"] != "Resource": 
        continue
    produced = neighbors_by_edge(g_res, v["name"], "Production", "in")
    used = neighbors_by_edge(g_res, v["name"], "Use", "out")
    table.append((v["name"], produced, used))

# %%

# mudar esses nomes de variáveis depois
residuo = [t for t in table if t[1] > 0 and t[2] == 0]
virgem = [t for t in table if t[1] ==0 and t[2] > 0]
circulando = [t for t in table if t[1] >0 and t[2] > 0]
orfaos = [t for t in table if t[1] ==0 and t[2] ==0]

# %%

print("residuos:", len(residuo))
print("virgem:", len(virgem))
print("circulando:", len(circulando))
print("orfaos:", len(orfaos))

# %%

total = len(table)
print("taxa:", len(circulando)/ total)

# %% [markdown]

# P2: Quais recursos são gerados como resíduos (alguém produz) mas ninguém usa?

# %%
from collections import deque

def bfs(
    g: ig.Graph,
    resource_name: str,
    max_jumps: int=5
) -> dict:
    """
    BFS.
    """
    if resource_name not in g.vs["name"]:
        return {}

    start = g.vs.find(name=resource_name).index
    dist = {start: 0}
    queue = deque([start])

    def neighbors(
        idx: int
    ):
        cur_type = g.vs[idx]["category"]
        out = []
        for e in g.incident(idx, mode="out"):
            et = g.es[e]["etype"]
            target = g.es[e].target
            if cur_type == "Resource" and et=="Use":
                out.append((target, "Use"))
            elif cur_type != "Resource" and et=="Symbiosis":
                out.append((target, "Symbiosis"))
            elif cur_type!= "Resource" and et=="Production":
                out.append((target, "Production")) 

        if cur_type != "Resource":
            for e in g.incident(idx, mode="out"):
                if g.es[e]["etype"] == "Communication":
                    out.append((g.es[e].target, "Communication"))
        return out

    while queue:
        cur = queue.popleft()
        d = dist[cur]
        if d >= max_jumps:
            continue
        for n, _et in neighbors(cur):
            if n not in dist:
                dist[n] = d+1
                queue.append(n)

    return {g.vs[k]["name"]: v for k, v in dist.items()}

# %%

from collections import Counter 
prod = Counter()
use = Counter()

for e in g_res.es:
    if e["etype"] == "Production":
        prod[e.target] += 1
    elif e["etype"] == "Use":
        use[e.source] += 1

rows = []
for v in g_res.vs:
    if v["category"] != "Resource":
        continue

    p = prod.get(v.index, 0)
    u = use.get(v.index, 0)
    reach = bfs(g_res, v["name"], max_jumps=5)
    comp_reach = {
        k: d for k, d in reach.items()
        if k != v["name"] and g_res.vs.find(name=k)["category"] != "Resource"
    }
    rows.append({
        "resource": v["name"],
        "produced_by": p,
        "used_by": u,
        "reached_companies": len(comp_reach),
        "jumps_to_closest": min(comp_reach.values()) if comp_reach else None
    })

df_p2 = pd.DataFrame(rows)
df_p2

# %%
import numpy as np
df_p2["status"] = np.select(
    [
        (df_p2["produced_by"]> 0) & (df_p2["used_by"] == 0) & (df_p2["reached_companies"]==0),
        (df_p2["produced_by"] == 0) & (df_p2["used_by"] > 0),
        (df_p2["used_by"] > 0) | (df_p2["reached_companies"] > 0)
    ],
    ["resíduo acumulado", "material virgem", "circula"],
    default="isolado"
)

df_p2
# %%

(
    df_p2.groupby("status").agg(
        resource=("resource", "count"),
        mean_reached_companies=("reached_companies", "mean"),
        mean_jumps=("jumps_to_closest", "mean"),
    ).round(4)
)

# %% [markdown]

# P3: Qual hub pratica mais cirularidade?

# %%
rows = []
for h in sorted(set(g_res.vs["hub"])):
    if not h or pd.isna(h): 
        continue

    comps = [v for v in g_res.vs if v["hub"] == h and v["category"] != "Resource"]
    materials = sum(1 for e in g_res.es
                    if g_res.vs[e.source]["hub"] == h and e["etype"] in ("Use", "Production", "Symbiosis"))
    interns = sum(1 for e in g_res.es
                  if g_res.vs[e.source]["hub"] == h and g_res.vs[e.target]["hub"] == h)
    rho = materials/len(comps) if comps else 0.0
    rows.append({
        "hub": h,
        "companies": len(comps),
        "materials": materials,
        "materials_by_comp": rho,
        "interns": interns,
        "interns_by_comp": round(interns / len(comps), 3) if comps else 0.0,
    })

df_p3 = pd.DataFrame(rows).sort_values("materials_by_comp", ascending=False).reset_index(drop=True)
df_p3

# %% [markdown]

# P4: Existem múltiplas rotas de reaproveitamento para cada resíduo?
# multiplas -> mais que 2

# %%

def count_rotes(
    g: ig.Graph,
    v1: int,
    v2: int,
    max_len: int=6
):
    if v1 == v2:
        return 0
    try:
        rotes = g.get_all_simple_paths(v=v1, to=v2, maxlen=max_len)
    except Exception:
        return 0
    return len(rotes)

# %%

rows = []
for v in g_res.vs:
    if v["category"] != "Resource":
        continue
    prod = [g_res.vs[g_res.es[e].source]["name"]
            for e in g_res.incident(v.index, mode="in")
            if g_res.es[e]["etype"] == "Production"]
    cons = [g_res.vs[g_res.es[e].source]["name"]
            for e in g_res.incident(v.index, mode="out")
            if g_res.es[e]["etype"] == "Use"]
    if not prod or not cons:
        continue

    rotes_total = sum(
        count_rotes(g_res, p, c)
        for p in prod for c in cons if p!=c
    )
    rows.append({
        "resource": v["name"],
        "prod": len(prod),
        "cons": len(cons),
        "rotes": rotes_total
    })

# %%

df_p4 = pd.DataFrame(rows)
df_p4.set_index(keys="resource")

# %%

df_p4[df_p4.select_dtypes("number").columns.tolist()].mean()

# %% [markdown]

# P5: Quem fala é quem faz?

# %%

df = nodes[nodes["cat_full"] != "Resource"][["id_code", "cat_full", "hub"]].copy()
df["deg_comm"] = df["id_code"].map(dict(zip(g_comm.vs["name"], g_comm.degree())))
df["deg_res"]  = df["id_code"].map(dict(zip(g_res.vs["name"],  g_res.degree(mode="all"))))
df =df.fillna({"deg_comm": 0, "deg_res": 0})

# %%

mc, mr = df["deg_comm"].median(), df["deg_res"].median()
df["quadrante"] = np.select(
    [(df.deg_comm > mc) & (df.deg_res > mr),
     (df.deg_comm > mc) & (df.deg_res <= mr),
     (df.deg_comm <= mc) & (df.deg_res > mr)],
    ["líder", "fachada", "invisível"],
    default="periférico",
)

# %%
df.groupby("quadrante")[["deg_comm","deg_res"]].agg(["count","mean"]).round(2)

# %% [markdown]
# P6: A circularidade é local ou global?

# %%

intern = sum(1 for e in g_res.es
               if g_res.vs[e.source]["hub"] == g_res.vs[e.target]["hub"]
               and e["etype"] in ("Use","Production","Symbiosis"))
extern = sum(1 for e in g_res.es
               if g_res.vs[e.source]["hub"] != g_res.vs[e.target]["hub"]
               and e["etype"] in ("Use","Production","Symbiosis"))

# %%

print(f"fluxos internos: {intern} ({100*intern/(intern+extern):.2f}%)")
print(f"fluxos externos: {extern} ({100*extern/(intern+extern):.2f}%)")

# %% [markdown]
# P7: O material é reusado ou apenas acumulado?

# %%

hierarchy = Counter(g_res.es["etype"])
total = sum(hierarchy.values())

for stage in ["Use", "Symbiosis", "Production"]:
    val = hierarchy.get(stage, 0)
    print(f"{stage}: {val} ({100*val/total:.2f})")

reuse_rate = (hierarchy.get("Use",0) + hierarchy.get("Symbiosis",0))/hierarchy.get("Production",1)
print(f"razão reuso/produção: {reuse_rate:.2f}")
