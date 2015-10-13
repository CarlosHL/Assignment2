# Herrero_CSCI3202_Assignment5  ID: 106022019
Introduction to Artificial Intelligence, University of Colorado Boulder

This is an optimal implementation of the Assignment 5, Introduction to Artificial Intelligence.
Although the solution path stills the same, in this implementation, the algorithm does not update 
the utility of the goal. The code that creates the maze has also been update, and a new class to store
the nodes has been added to make more simple the debugging process. The utilities do not show decimals although
they store it (store a float, print an int).

The program receives as a parameter the map and the value of epsilon.

To run the program: 
python Assignment5.py <map.txt> <epsilon>

Example:
python Assignment5.py World1MDP.txt 0.5 

Running the program with epsilon = 5:

➜  maze2  python Assignment5.py World1MDP.txt 0.5
[0] , [7], utility 5, key 0
[1] , [7], utility 6, key 1
[2] , [7], utility 7, key 2
[3] , [7], utility 8, key 3
[4] , [7], utility 9, key 4
[5] , [7], utility 11, key 5
[6] , [7], utility 12, key 6
[6] , [6], utility 14, key 16
[6] , [5], utility 16, key 26
[6] , [4], utility 19, key 36
[6] , [3], utility 22, key 46
[7] , [3], utility 26, key 47
[7] , [2], utility 29, key 57
[8] , [2], utility 33, key 58
[9] , [2], utility 38, key 59
[9] , [1], utility 43, key 69
[9] , [0], utility 50, key 79


Running the program with epsilon = 0.00001:

➜  maze2  python Assignment5.py World1MDP.txt 0.00001
[0] , [7], utility 5, key 0
[1] , [7], utility 6, key 1
[2] , [7], utility 7, key 2
[3] , [7], utility 8, key 3
[4] , [7], utility 9, key 4
[5] , [7], utility 11, key 5
[6] , [7], utility 12, key 6
[6] , [6], utility 14, key 16
[6] , [5], utility 16, key 26
[6] , [4], utility 19, key 36
[6] , [3], utility 22, key 46
[7] , [3], utility 26, key 47
[7] , [2], utility 29, key 57
[8] , [2], utility 33, key 58
[9] , [2], utility 38, key 59
[9] , [1], utility 43, key 69
[9] , [0], utility 50, key 79

Running the program with epsilon = 0.99999:

➜  maze2  python Assignment5.py World1MDP.txt 0.99999                      
[0] , [7], utility 5, key 0
[1] , [7], utility 6, key 1
[2] , [7], utility 7, key 2
[3] , [7], utility 8, key 3
[4] , [7], utility 9, key 4
[5] , [7], utility 11, key 5
[6] , [7], utility 12, key 6
[6] , [6], utility 14, key 16
[6] , [5], utility 16, key 26
[6] , [4], utility 19, key 36
[6] , [3], utility 22, key 46
[7] , [3], utility 26, key 47
[7] , [2], utility 29, key 57
[8] , [2], utility 33, key 58
[9] , [2], utility 38, key 59
[9] , [1], utility 43, key 69
[9] , [0], utility 50, key 79

Changing the value of epsilon, the error of the model changer, therefore the algorithm may stop in a different iteration. 
This may cause eventually a change in the utilities of the nodes and a different path solution, but for the map given, the solution 
remain the same (not the utilities). We can conclude that a change on the precision of epsilon may change the expected utility of the map but 
non the optimal path.