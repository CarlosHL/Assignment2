#import to read the txt
from sys import argv

import csv
import copy
import listNode, math 

# read data
script, filename, epsilon = argv
file = open(filename, 'rb')
data = csv.reader(file, delimiter=' ')
table = [row for row in data]

    

# first, we create a dlist with the nodes of the maze

def createMaze():
    maze = listNode.DoubleList()
    k = 0
    for val in range(0,8):
      row = 7- val
      for col in range (0, 10):
        loc = listNode.Location(row, col)
        utility = 0

        terrain_type = int(table[row][col])
        if terrain_type == 0:
          reward = 0 # no reward
        elif terrain_type == 1: #mountain
          reward = -1
        elif terrain_type == 3: #snake
          reward = -2
        elif terrain_type == 4: #barn
          reward = 1
        elif terrain_type == 50:
          reward = 50
        else:
          reward = -1000 
        
        if k < 10:
          if k == 0:
            listEdges = [k + 1, k + 10]
          elif k == 9:
             listEdges = [k - 1, k + 10]
          else:
            listEdges = [k - 1, k + 1, k + 10]
        elif k > 69:
          if k == 70: 
            listEdges = [k - 10, k + 1]
          elif k == 79:
            listEdges = [k - 10, k - 1]
          else:
            listEdges = [ k - 10, k-1, k+1]
        elif k % 10 == 0 and k != 0 and k !=70:
          listEdges = [k - 10,  k + 1, k + 10]
        elif k % 10 == 9 and k != 9 and k != 79:
          listEdges = [k - 10,  k - 1,  k + 10]
        else:
          listEdges = [k - 10, k - 1, k + 1,  k + 10]

        maze.append(k, loc, utility, terrain_type, listEdges, reward)     
        k = k +1
     
    return maze

maze = createMaze()

iteration = 0
# now the value iteration implementation
solution = False
epsilon = float(epsilon)
if epsilon<0 or epsilon > 1:
  print "Not valid epsilon, setting default value 0.5"
  epsilon = 0.5
gamma = 0.9
#iteration = 0

#initialize delta and the utility of the goal to start Bellman's equation
maze.searchNode(79).utility = 50.0
delta = 1000


while delta > epsilon*((1-gamma)/gamma):
  
  #set utilities, set delta
  node = maze.head
  while node:
    node.old_utility = node.utility
    node = node.next

  
  delta = 0
  
  node = maze.head
  while node:
    if node.terrain != 2 and node.utility != 50:
      up = node.utility
      right = node.utility
      down = node.utility
      left = node.utility  
      for n in node.edges:
        if n == node.key + 10 and maze.searchNode(n).terrain!=2:
          up =  maze.searchNode(n).old_utility
        if n == node.key + 1 and maze.searchNode(n).terrain!=2:
          right = maze.searchNode(n).old_utility
        if n == node.key - 10 and maze.searchNode(n).terrain!=2:
          down = maze.searchNode(n).old_utility 
        if n == node.key - 1 and maze.searchNode(n).terrain!=2:
          left = maze.searchNode(n).old_utility 
          
      up_dir = float((0.8*up + 0.1*right + 0.1*left))
      right_dir = float((0.8*right + 0.1*up + 0.1*down))
      down_dir = float((0.8*down + 0.1*right + 0.1*left))  
      lef_dir = float((0.8*left + 0.1*up + 0.1*down)) 
      
      max_dir = max(up_dir, right_dir, down_dir, lef_dir)
      node.utility = node.reward  + gamma * max_dir
      
      
      if abs(node.old_utility-node.utility)>delta:
        delta = abs(node.old_utility-node.utility) 
      

        
    node = node.next  

  #iteration = iteration + 1


open = []
open.append(0)
max = 0
solution_path = False

while not solution_path: 
  value = open [-1]
  max = 0
  for m in maze.searchNode(value).edges:
    if maze.searchNode(m).utility > max:
        max = maze.searchNode(m).utility
        key_path = m
  
  open.append(key_path)
  if key_path == 79:
    solution_path = True
  
#print open

for n in open:
  print "[%d] , [%d], utility %d, key %d" % (maze.searchNode(n).location.col,
   maze.searchNode(n).location.row, maze.searchNode(n).utility, n)


