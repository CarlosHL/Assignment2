#import to read the txt
from sys import argv

import csv
import copy


# read data
script, filename, epsilon = argv
file = open(filename, 'rb')
data = csv.reader(file, delimiter=' ')
table = [row for row in data]

        
class Location(object):
  def __init__(self, row, col):
    self.row = row
    self.col= col
    
class Node(object):
# Initializes the node object
  def __init__(self, key, location, utility, reward, prev, next):
    #to link to the list
    self.prev = prev
    self.next = next
    self.old_utility = 0
    self.location = location
    self.key = key
    self.edges = []
    self.utility = utility
    self.reward = reward 
    self.parent = None


#use this class to store open and closed nodes
class DoubleList(object):

  head = None
  
  def append(self, key, location, utility, reward):
    new_node = Node(key, location, utility, reward, None, None) 
    if self.head is None:
      self.head = self.tail = new_node
    else:
      new_node.prev = self.tail
      new_node.next = None
      self.tail.next = new_node
      self.tail = new_node
  
  def search(self, key):
    aux_node = self.head
    
    while aux_node is not None:
      if aux_node.key == key:
        return True        
      aux_node = aux_node.next
      
    return False  
    
  def searchNode(self, key):
    aux_node = self.head
    
    while aux_node is not None:
      if aux_node.key == key:
        return aux_node        
      aux_node = aux_node.next
      
    return False 


  def remove(self, key):
    aux_node = self.head
    
    while aux_node is not None:
      if aux_node.key == key:
        #not first element
        if  aux_node.prev is not None:
          aux_node.prev.next = aux_node.next
          aux_node.next.prev = aux_node.prev
        # first element  
        else:
          self.head = aux_node.next
          aux_node.next.prev = None
          
      aux_node = aux_node.next
    

  def show(self):
    print "Nodes of the list"
    aux_node = self.head
    while aux_node is not None:
      print "key %d, reward %d, utility %d" % (aux_node.key, aux_node.reward, aux_node.utility)
      print "adjacent are", aux_node.edges
      aux_node = aux_node.next
    
    print "*" * 20
    

# first, we create a dlist with the nodes of the maze
maze = DoubleList()

key_node = 0
for val in range(0,8):
  row = 7- val
  for col in range (0, 10):
    loc = Location(row, col)
    utility = 0
    terrain_type = int(table[row][col])
    if terrain_type == 0:
      reward = 0 # no reward
    elif terrain_type == 1:
      reward = -1
    elif terrain_type == 3:
      reward = -2
    elif terrain_type == 4:
      reward = 1
    elif terrain_type == 50:
      reward = 50
    else:
      reward = -1000  
    maze.append(key_node, loc, utility, reward) 
        
    key_node = key_node +1

# setting adjacents of the nodes
node_maze = maze.head
while node_maze:
  k = node_maze.key
  if k < 10:
    if k == 0:
      node_maze.edges.append(k+1)
      node_maze.edges.append(k+10)
      node_maze.edges.append(k+11)
    elif k ==9: 
      node_maze.edges.append(k-1)
      node_maze.edges.append(k+10)
    else:
      node_maze.edges.append(k-1)
      node_maze.edges.append(k+1)
      node_maze.edges.append(k+10)
  elif k > 69:
    if k == 70:
      node_maze.edges.append(k-10)
      node_maze.edges.append(k+1)
    elif k == 79:
      node_maze.edges.append(k-10)
      node_maze.edges.append(k-1)
    else:
      node_maze.edges.append(k-10)
      node_maze.edges.append(k-1)
      node_maze.edges.append(k+1)      
  elif k % 10 == 0 and k != 0 and k !=70:
    node_maze.edges.append(k-10)
    node_maze.edges.append(k+1)
    node_maze.edges.append(k+10)
  elif k % 10 == 9 and k != 9 and k != 79:
    node_maze.edges.append(k-10)
    node_maze.edges.append(k-1)
    node_maze.edges.append(k+10)
  else:
    node_maze.edges.append(k-10)
    node_maze.edges.append(k-1)
    node_maze.edges.append(k+1)
    node_maze.edges.append(k+10)

  node_maze = node_maze.next
    
#maze.show()

# now the value iteration implementation
solution = False
epsilon = float(epsilon)
if epsilon<0 or epsilon > 1:
  print "Not valid epsilon, setting default value 0.5"
  epsilon = 0.5
gamma = 0.9
iteration = 0



while not solution:
  delta = 0
  aux_node = maze.head
  
  while aux_node: #set utilities
    aux_node.old_utility = aux_node.utility
    aux_node = aux_node.next  
      
  node_aux = maze.head
  while node_aux: #goes through maze
    up = node_aux.utility
    right = node_aux.utility
    down = node_aux.utility
    left = node_aux.utility
    if node_aux.reward != -1000:
      for m in node_aux.edges: #update utility of a single node
        if m == node_aux.key + 10:
          if maze.searchNode(m).reward != -1000:
            up = maze.searchNode(m).old_utility
          
        elif m == node_aux.key + 1:
          if maze.searchNode(m).reward != -1000:
            right = maze.searchNode(m).old_utility
        
        elif m == node_aux.key -10:
          if maze.searchNode(m).reward != -1000:
            down = maze.searchNode(m).old_utility

        elif  m == node_aux.key -1:
          if maze.searchNode(m).reward != -1000:
            left = maze.searchNode(m).old_utility
       
      max_value= max((0.8*up + 0.1*right + 0.1*left),(0.8*right + 0.1*up + 0.1*down),(0.8*down + 0.1*right + 0.1*left),
       (0.8*left + 0.1*up + 0.1*down))
      
         
      node_aux.utility = node_aux.reward + gamma * max_value
       # print "Setting max utility of ",   node_aux.key, " utility is ", node_aux.utility

      if abs(node_aux.old_utility-node_aux.utility)>0:
        delta = abs(node_aux.old_utility-node_aux.utility)
        
    node_aux=node_aux.next 
       
  if delta < float(epsilon*(1-gamma)/gamma):
    solution = True
        

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

