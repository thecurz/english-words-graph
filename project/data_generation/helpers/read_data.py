from distutils.command.build import build
from checkpath import check_path 
from collections import deque
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
      words_dict[word] = G[u][1]
    if related in words_dict:
      existing = words_dict[related]
      existing.append([G[u][0], G[u][1][1]])
      words_dict[related] = existing
    else:
      words_dict[related] = [G[u][0], G[u][1][1]]
  return words_dict

def BFS(G, explored = set(), source = ''):
  if source == '':
    source = list(G.keys())[0]
    #print(source)
  queue = deque([source])
  while(len(queue) > 0):
    current = queue.popleft()
    #print(current)
    for neighbor in G[current]:
      queue.append(neighbor)
  return
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
      #print(first_word)
      #print(w)
      relations.append([first_word, w])
  #print(relations)
  #return list(set(word_list)), relations
  return relations

G = read_data()
#OPTIMIZE
graphing =  copy.deepcopy(G)
graph = build_graph(graphing)
print(G[0][1])
#print(G[0][1][2])
#BFS(graph)