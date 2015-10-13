#import to read the txt
from sys import argv

import csv
import copy
import listNode


# read data
script, filename, heur = argv
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
        if heur == 'man':
          heuristic = (9 - col + row%10)*10 
        elif heur == 'short':
          xDist = abs(row - 9)
          yDist = abs(col -7)
          if xDist > yDist:
            heuristic = 14*yDist + 10*(xDist-yDist)
          else:
            heuristic = 14*xDist + 10*(yDist-xDist)
        else:
         print "Not valid heuristic" 
         heuristic = 0   
        penalization = int(table[row][col])
        if penalization == 0:
          terrain = 0
        elif penalization == 1:
          terrain = 10
        else:
          terrain = 10000 
        
        if k < 10:
          if k == 0:
            listEdges = [k + 1, k + 10, k + 11]
          elif k == 9:
             listEdges = [k - 1, k + 9, k + 10]
          else:
            listEdges = [k - 1, k + 1, k + 9, k + 10, k + 11]
        elif k > 69:
          if k == 70: 
            listEdges = [k - 10, k -9, k + 1]
          elif k == 79:
            listEdges = [k - 11, k - 10, k - 1]
          else:
            listEdges = [k - 11, k - 10, k - 9, k-1, k+1]
        elif k % 10 == 0 and k != 0 and k !=70:
          listEdges = [k - 10, k - 9, k + 1, k + 10, k + 11]
        elif k % 10 == 9 and k != 9 and k != 79:
          listEdges = [k - 10, k - 9, k - 1, k + 9, k + 10]
        else:
          listEdges = [k - 11, k - 10, k - 9, k - 1, k + 1, k + 9, k + 10, k + 11]

        maze.append(k, loc, heuristic, terrain, listEdges)     
        k = k +1
     
    return maze
    
    

maze = createMaze()   
  


# we create two list, one for the open nodes, the other for the close nodes

open = []
close = []
open.append(0)
maze.searchNode(open[0]).g = 0
maze.searchNode(open[0]).f = 0



solution = False
locations = 0 
it = 0
# A* algorithm 
while not solution:
# look for lowest in open list  
  value_f = 1000
  min_v = 0
  for n in open:
    if maze.searchNode(n).f < value_f :
      
      value_f = maze.searchNode(n).f
      min_v = n
      if n == 79:
        solution = True
  # switch from open to remove 
  open.remove(min_v)
  close.append(min_v)
  
  # calculate f of adjacents 
  for m in  maze.searchNode(min_v).edges:  
    # if is not in close
    if m not in close:
      # if is not in open
      if m not in open:
        if maze.searchNode(m).terrain!=10000:
          locations = locations + 1
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
        if maze.searchNode(m).g > maze.searchNode(close[it]).g + move + maze.searchNode(close[it]).terrain:
          maze.searchNode(m).g = maze.searchNode(close[it]).g + move + maze.searchNode(m).terrain
          maze.searchNode(m).f = maze.searchNode(m).heuristic + maze.searchNode(m).g 
          maze.searchNode(m).parent = maze.searchNode(close[it])
  it = it + 1
          
# print solution      
sol_node = maze.searchNode(79)
sol_list = []
print "COST OF THE PATH: ", sol_node.g
print "LOCATIONS EVALUATED:", locations

while sol_node:
  sol_list.insert(0, sol_node.key)
  sol_node = sol_node.parent

print "KEYS OF THE NODES OF THE SOLUTION PATH:", sol_list
print "SOLUTION PATH (POSITIONS IN MAP):"
for m in sol_list:
  print "[%d,%d]" % (maze.searchNode(m).location.row, maze.searchNode(m).location.col)
  
