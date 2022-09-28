from distutils.command.build import build
import graphviz as gv
from helpers.checkpath import check_path 
from collections import deque
import json
import copy

CWD = check_path()
DATASET1 = CWD + r'\datasets\SimVerb-3500.txt'
DATASET2 = CWD + r'\datasets\wordsim_relatedness_goldstandard.txt'

def build_graph(G):
  words_dict = dict()
  for u in range(len(G)):
    word = G[u][0]
    related = G[u][1][0]
    if word in words_dict:
      existing = words_dict[word]
      existing.append(G[u][1])
      words_dict[word] = existing
    else:
      words_dict[word] = [G[u][1]]
    if related in words_dict:
      existing = words_dict[related]
      existing.append([G[u][0], G[u][1][1]])
      words_dict[related] = existing
    else:
      words_dict[related] = [[G[u][0], G[u][1][1]]]
  return words_dict


'''
graph = {
  'a': ['c','b'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': [],
  'g': ['h'],
  'h': ['g']

}


BFS(graph, source= 'a')
'''
def check_sub_graphs():

  return

def read_data():
  word_list = []
  relations = []
  with open(DATASET1) as file:
    lines = file.readlines()
    for line in lines:
      line = line.split('	')
      first_word = line[0]
      second_word = line[1]
      relatedness = line[3]
      word_list.append(first_word)
      word_list.append(second_word)
      relations.append([first_word,[second_word,relatedness]])

  with open(DATASET2) as file:
    lines = file.readlines()
    for line in lines:
      line = line.split('	')
      first_word = line[0]
      second_word = line[1]
      relatedness = line[2]
      word_list.append(first_word)
      word_list.append(second_word)
      w = [second_word,relatedness[:-2]]
      relations.append([first_word, w])
  return word_list, relations

def BFS(G, source = ''):
  newG = dict()
  explored = set()
  lengths = []
  if source == '':
    source = list(G.keys())[0]
  queue = deque([])
  queue.extend(G[source])

  while(len(queue) > 0):
    current = queue.popleft()
    newG[current[0]] = G[current[0]]
    for neighbor in G[current[0]]:
      if neighbor[0] not in explored:
        queue.append(neighbor)
        explored.add(neighbor[0])
  return newG

def convert(G):
  new_G = []
  keys = list(G.keys())
  for i in range(len(G)):
    for j in range(len(G[keys[i]])):
      new_G.append([keys[i], G[keys[i]][j]])
  return new_G

def show_graph(L, word_list, labels=None, path=[],layout="circo"):
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

'''
_, G = read_data()
#OPTIMIZE
graph = build_graph(G)
graph = convert(BFS(graph))
#f = open('write.json', 'a')
#f.write(json.dumps(graph, indent = 4))
print(graph[0])
show_graph(graph, _)
'''

