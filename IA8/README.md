# Herrero_CSCI3202_Assignment8  ID: 106022019
Introduction to Artificial Intelligence, University of Colorado Boulder

Files included:

A8_1.py : contains the main functionality, using a list with all the alphabet and "_" calculates the emission, transition and initial probabilities. 
          Code is clear and comented.

A8_1-store.py : same as A8_1.py, but creates a double list with all the characters and stores the result in dictionaries inside the nodes. Prints the stored values.

result : file where the out is written.

typos20.data : data used to calculate the probabilities.

typos20test.data : data included for the second part.



To run the code:

python A8_1,py



Formulas used: 

X[t] E[t] -> where X[t] is the current state of the data and E[t] the evidence

Initial probabilities:

  P ( X [0] = x) =  times X[t]=x  / number of characters in state data
  
Emission probabilities:
 
  P( E[t] = y | X[t] = x ) = (1 + number of times E[t]=y given X[t]=x) / (27 + times X[t]=x )

Transition probabilities:

 P( X[t+1] = y | X[t] = x ) = (1 + number of times X[t+1]=y given X[t]=x) / (27 + times X[t]=x )