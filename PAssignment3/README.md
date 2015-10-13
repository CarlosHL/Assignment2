# Herrero_CSCI3202_Assignment3  ID: 106022019
Introduction to Artificial Intelligence, University of Colorado Boulder

This is an optimal implementation of the Assignment 3, Introduction to Artificial Intelligence.
Although the solution path stills the same, in this implementation, the algorithm has a new
an optimal way to calculate the heuristic. The code that creates the maze has also been update, and a new class to store
the nodes has been added to make more simple the debugging process. The number of visited nodes has also been updated, 
this algorithm only counts the nodes added to the open list (it excludes the walls). While the last implementation may be more 
accurate in terms of complexity, this one makes easier to understand the development of the heuristics (is implemented as we did
in classes). The output has also been modified to make easier to follow the path.

The program receives as a parameter the map and the heuristic (man for Manhattan, short for Diagonal Shortcut).
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
   -Terrain: 0 if the value of the location is 0, 10 for mountains, and 10000 for walls.
   As long as the penalization for walls is bigger than the number of squares*10, the code works.
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

➜  maze  python Assignment2.py World1.txt man

COST OF THE PATH:  156

LOCATIONS EVALUATED: 32

KEYS OF THE NODES OF THE SOLUTION PATH: [0, 11, 21, 31, 41, 52, 53, 64, 65, 76, 77, 78, 79]

SOLUTION PATH (POSITIONS IN MAP):

[7,0] 
[6,1] 
[5,1] 
[4,1] 
[3,1] 
[2,2] 
[2,3] 
[1,4] 
[1,5] 
[0,6] 
[0,7] 
[0,8] 
[0,9] 

----------DIAGONAL SHORTCUT----------

➜  maze  python Assignment2.py World1.txt short

COST OF THE PATH:  130

LOCATIONS EVALUATED: 61

KEYS OF THE NODES OF THE SOLUTION PATH: [0, 1, 2, 13, 23, 34, 45, 46, 47, 58, 69, 79]

SOLUTION PATH (POSITIONS IN MAP):

[7,0] 
[7,1] 
[7,2] 
[6,3] 
[5,3] 
[4,4] 
[3,5] 
[3,6] 
[3,7] 
[2,8] 
[1,9] 
[0,9] 


--------------------MAP2-------------------- 
 
----------MANHATTAN---------

➜  maze  python Assignment2.py World2.txt man 
 
COST OF THE PATH:  142

LOCATIONS EVALUATED: 36

KEYS OF THE NODES OF THE SOLUTION PATH: [0, 1, 2, 13, 23, 34, 44, 54, 64, 75, 76, 77, 78, 79]

SOLUTION PATH (POSITIONS IN MAP):

[7,0] 
[7,1] 
[7,2] 
[6,3] 
[5,3] 
[4,4] 
[3,4] 
[2,4] 
[1,4] 
[0,5] 
[0,6] 
[0,7]  
[0,8] 
[0,9] 

----------DIAGONAL SHORTCUT----------

➜  maze  python Assignment2.py World2.txt short

COST OF THE PATH:  142

LOCATIONS EVALUATED: 59

KEYS OF THE NODES OF THE SOLUTION PATH: [0, 1, 2, 13, 23, 33, 44, 54, 64, 75, 76, 77, 78, 79]

SOLUTION PATH (POSITIONS IN MAP):

[7,0] 
[7,1] 
[7,2] 
[6,3] 
[5,3]  
[4,3] 
[3,4] 
[2,4] 
[1,4] 
[0,5]  
[0,6] 
[0,7] 
[0,8] 
[0,9] 


As we can see, only the second heuristic finds the optimal path. This is because the Manhattan distance overestimates the 
distance if we can move in diagonals -> the Manhattan distance is not admisible for this kinds of maze, therefore it may not find 
the optimal path.

If we want to make if admissible we can divide if by two (as it has been done in the first submit).

It takes more evaluations for the diagonal shortcut heuristic. 
The diagonal shortcut heuristic is also a bit slower than the Manhattan heuristic.
The diagonal shortcut distance may work better with  small modifiers or influence map modifier. It works with diagonals.

