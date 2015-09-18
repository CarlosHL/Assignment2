#import to read the txt
from sys import argv

import csv
import copy


# read data
script, filename = argv
file = open(filename, 'rb')
data = csv.reader(file, delimiter=' ')
table = [row for row in data]

        
class Location(object):
  def __init__(self, row, col):
    self.row = row
    self.col= col
    
class Node(object):
# Initializes the node object
  def __init__(self, key, location, heuristic, terrain, prev, next):
    #to link to the list
    self.prev = prev
    self.next = next
  
    self.location = location
    self.key = key
    self.edges = []
    self.next = None
    self.heuristic = heuristic
    self.terrain = terrain 
    self.parent = None
    self.f = None
    self.g = None

#use this class to store open and closed nodes
class DoubleList(object):

  head = None
  tail = None
  
  def append(self, key, location, heuristic, terrain):
    new_node = Node(key, location, heuristic, terrain, None, None) #check this out!
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
      print "key %d, terrain penalization %d, heuristic %d" % (aux_node.key, aux_node.terrain, aux_node.f)
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
    xDist = abs(row - 9)
    yDist = abs(col -7)
    if xDist > yDist:
     heuristic = 14*yDist + (xDist-yDist)
    else:
     heuristic = 14*xDist + (yDist-xDist)    
    penalization = int(table[row][col])
    if penalization == 0:
      terrain = 0
    elif penalization == 1:
      terrain = 10
    else:
      terrain = 10000 
    maze.append(key_node, loc, heuristic, terrain) 
        
    key_node = key_node +1

# maze.show()

# setting adjacents
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
      node_maze.edges.append(k+9)
      node_maze.edges.append(k+10)
    else:
      node_maze.edges.append(k-1)
      node_maze.edges.append(k+1)
      node_maze.edges.append(k+9)
      node_maze.edges.append(k+10)
      node_maze.edges.append(k+11)
  elif k > 69:
    if k == 70:
      node_maze.edges.append(k-10)
      node_maze.edges.append(k-9)
      node_maze.edges.append(k+1)
    elif k == 79:
      node_maze.edges.append(k-11)
      node_maze.edges.append(k-10)
      node_maze.edges.append(k-1)
    else:
      node_maze.edges.append(k-11)
      node_maze.edges.append(k-10)
      node_maze.edges.append(k-9)
      node_maze.edges.append(k-1)
      node_maze.edges.append(k+1)      
  elif k % 10 == 0 and k != 0 and k !=70:
    node_maze.edges.append(k-10)
    node_maze.edges.append(k-9)
    node_maze.edges.append(k+1)
    node_maze.edges.append(k+10)
    node_maze.edges.append(k+11)
  elif k % 10 == 9 and k != 9 and k != 79:
    node_maze.edges.append(k-10)
    node_maze.edges.append(k-9)
    node_maze.edges.append(k-1)
    node_maze.edges.append(k+9)
    node_maze.edges.append(k+10)
  else:
    node_maze.edges.append(k-11)
    node_maze.edges.append(k-10)
    node_maze.edges.append(k-9)
    node_maze.edges.append(k-1)
    node_maze.edges.append(k+1)
    node_maze.edges.append(k+9)
    node_maze.edges.append(k+10)
    node_maze.edges.append(k+11)

  node_maze = node_maze.next
 
# maze.show()


#---------------WORKS-----------------------#


open = []
close = []
open.append(0)
maze.searchNode(open[0]).g = 0
maze.searchNode(open[0]).f = 0



#boolean = False
it = 0
solution = False
locations = 1 

while not solution:

  min_v = 0
  # look for lowest in open list  
  value_f = 1000
  
  for n in open:
    if maze.searchNode(n).f < value_f :
      value_f = maze.searchNode(n).f
      min_v = n
      if n == 79:
        solution = True
 
  print close
  # switch from open to remove 
  open.remove(min_v)
  close.append(min_v)
  
  # calculate f of adjacents
  m = 0 
  
  for m in  maze.searchNode(min_v).edges:  
    locations = locations + 1
    # if is not in close
    if m not in close:
      # if is not in open
      if m not in open:
        if (m == min_v - 1 or m == min_v + 1 or m == min_v - 10 or m == min_v + 10):
          move = 10
        else:
          move = 14
        open.append(m)
        maze.searchNode(m).g = maze.searchNode(close[it]).g + move + maze.searchNode(m).terrain
        maze.searchNode(m).f = maze.searchNode(m).heuristic + maze.searchNode(m).g 
        maze.searchNode(m).parent = maze.searchNode(close[it])
      # if is in open
      if m in open: #add move
        if (m == min_v - 1 or m == min_v + 1 or m == min_v - 10 or m == min_v + 10):
          move = 10
        else:
          move = 14
        if maze.searchNode(m).g > maze.searchNode(close[it]).g + move:
          maze.searchNode(m).g = maze.searchNode(close[it]).g + move + maze.searchNode(m).terrain
          maze.searchNode(m).f = maze.searchNode(m).heuristic + maze.searchNode(m).g 
          maze.searchNode(m).parent = maze.searchNode(close[it])
          open.append(m)
          
   

     
  it = it + 1      
      
      

sol_node = maze.searchNode(79)
sol_list = []
print "COST OF THE PATH: ", sol_node.g
print "LOCATIONS EVALUATED:", locations

while sol_node:
  sol_list.insert(0, sol_node.key)
  sol_node = sol_node.parent

print "SOLUTION PATH:", sol_list


