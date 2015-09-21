# Herrero_CSCI3202_Assignment2  ID: 106022019
Introduction to Artificial Intelligence, University of Colorado Boulder


The program receives as a parameter the map and the heuristic (mas for Manhattan, short for Diagonal Shortcut).
To run the program: 
    Manhattan: python Assignment2.py World1.txt man
    Diagonal Shortcut: python Assignment2.py World1.txt short
    
    
This python file creates a double linked list of nodes with the locations of the map. It gives 
the key 0 to the start node, and goes on until node 79, the goal.

Each node has:
  -Previous and next node 
  -Location of the node (row, column)
  -Key
  -List of adjacent nodes (edges) 
  -Value of h (heuristic)
  -Value of f
  -Value of g
  -Terrain
  -Parent: for visited nodes used to know the solution path    
  
After creating the list (maze), the program sets the adjacents of each node. It creates two python lists: close[]
and open[], to store the keys of the nodes. Then it executes the A* algorithm and creates a list with the key of the nodes 
of the solution. It prints the solution, number of different nodes evaluated, and cost of the path.


SECOND HEURISTIC
Diagonal Shortcut

This method balances H with G. I used this method because it is balanced, it is able to fully consider small modifiers like a turning penalty or influence map modifier, and is one of the most popular methods. 

    xDistance = abs(currentX-targetX)
    yDistance = abs(currentY-targetY)
    if xDistance > yDistance
         H = 7*yDistance + 5*(xDistance-yDistance)
    else
         H = 7*xDistance + 5*(yDistance-xDistance)
    end if

Comparing heuristics:

--------------------MAP1--------------------
----------MANHATTAN---------
COST OF THE PATH:  130
LOCATIONS EVALUATED: 76
KEYS OF THE NODES OF THE SOLUTION PATH: [0, 1, 2, 13, 24, 34, 45, 46, 57, 58, 69, 79]
SOLUTION PATH (POSITIONS IN MAP):
[7] , [0]
[7] , [1]
[7] , [2]
[6] , [3]
[5] , [4]
[4] , [4]
[3] , [5]
[3] , [6]
[2] , [7]
[2] , [8]
[1] , [9]
[0] , [9]

----------DIAGONAL SHORTCUT----------
COST OF THE PATH:  130
LOCATIONS EVALUATED: 79
KEYS OF THE NODES OF THE SOLUTION PATH: [0, 1, 2, 13, 23, 34, 45, 46, 47, 58, 69, 79]
SOLUTION PATH (POSITIONS IN MAP):
[7] , [0]
[7] , [1]
[7] , [2]
[6] , [3]
[5] , [3]
[4] , [4]
[3] , [5]
[3] , [6]
[3] , [7]
[2] , [8]
[1] , [9]
[0] , [9]


--------------------MAP2--------------------
----------MANHATTAN---------
COST OF THE PATH:  142
LOCATIONS EVALUATED: 77
KEYS OF THE NODES OF THE SOLUTION PATH: [0, 1, 2, 13, 23, 34, 44, 54, 64, 75, 76, 77, 78, 79]
SOLUTION PATH (POSITIONS IN MAP):
[7] , [0]
[7] , [1]
[7] , [2]
[6] , [3]
[5] , [3]
[4] , [4]
[3] , [4]
[2] , [4]
[1] , [4]
[0] , [5]
[0] , [6]
[0] , [7]
[0] , [8]
[0] , [9]


----------DIAGONAL SHORTCUT----------
COST OF THE PATH:  142
LOCATIONS EVALUATED: 79
KEYS OF THE NODES OF THE SOLUTION PATH: [0, 1, 2, 13, 23, 33, 44, 54, 64, 75, 76, 77, 78, 79]
SOLUTION PATH (POSITIONS IN MAP):
[7] , [0]
[7] , [1]
[7] , [2]
[6] , [3]
[5] , [3]
[4] , [3]
[3] , [4]
[2] , [4]
[1] , [4]
[0] , [5]
[0] , [6]
[0] , [7]
[0] , [8]
[0] , [9]


As we can see, both heuristic find the optimal path. It takes more evaluations for the diagonal shortcut heuristic. 
The diagonal shortcut heuristic is also a bit slower than the Manhattan heuristic.
The diagonal shortcut distance may work better with  small modifiers or influence map modifier.