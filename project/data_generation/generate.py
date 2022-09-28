import graphviz as gv
from helpers.read_data import read_data

word_list, relations = read_data()

def show_graph(L, labels=None, path=[],
             layout="circo"):
  g = gv.Graph("G")
  g.graph_attr["layout"] = layout
  g.edge_attr["color"] = "gray"
  g.node_attr["color"] = "orangered"
  g.node_attr["width"] = "0.1"
  g.node_attr["height"] = "0.1"
  g.node_attr["fontsize"] = "8"
  g.node_attr["fontcolor"] = "mediumslateblue"
  g.node_attr["fontname"] = "monospace"
  g.edge_attr["fontsize"] = "8"
  g.edge_attr["fontname"] = "monospace"
 
  for u in range(len(word_list)):
    g.node(word_list[u])
  added = set()

  #REFACTOR
  #REFACTOR
  #REFACTOR
  for v, u in enumerate(path):
    if u != None:
      #?????
      for vi, w in L[u]:
        if vi == v:
          break
        g.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="orange")

  for u in range(len(L)):
      tail = L[u][0]
      head = L[u][1][0]
      if not f"{tail},{head}" in added:
        added.add(f"{tail},{head}")
        added.add(f"{head},{tail}")
        g.edge(tail, head, L[u][1][1])
  return g
show_graph(relations[:1200])