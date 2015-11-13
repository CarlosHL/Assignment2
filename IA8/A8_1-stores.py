from __future__ import division
   
class Node(object):
# Initializes the node object
    def __init__(self, char, prev, next):
        self.prev = prev
        self.next = next
        
        self.char = char
        self.initial = 0
        self.emission = {}
        self.transition = {}
        
class DoubleList(object):

    head = None
  
    def append(self, char):
        new_node = Node(char, None, None) 
        if self.head is None:
          self.head = self.tail = new_node
        else:
          new_node.prev = self.tail
          new_node.next = None
          self.tail.next = new_node
          self.tail = new_node 
    
    def searchNode(self, c):
        aux_node = self.head
    
        while aux_node is not None:
          if aux_node.char == c:
            return aux_node        
          aux_node = aux_node.next
      
        return False 


    def remove(self, char):
        aux_node = self.head
    
        while aux_node is not None:
          if aux_node.char == key:
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
          print  " char", aux_node.char
          print  "emission", aux_node.emission
          print "transition", aux_node.transition
          
          aux_node = aux_node.next
    
        print "*" * 20
        
 
        
##Calculus####

        
def getInitial(x):
    xTimes = 0
    for i in range(0, len(list)): #check number of times x is in list
        if list[i][0] == x: 
            xTimes = xTimes + 1
    return xTimes / len(list)

def getEmission(e, x):
    denominator = 27
    numerator = 1
    for i in range(0, len(list)): 
        if list[i][0] == x: #check number of times x (state) is in list
            denominator = denominator + 1
            if list[i][2] == e: #check number of times e (evidence) is in list, given the state
                numerator = numerator + 1
    return numerator / denominator
    
def getTransition(x1, x0):
    denominator = 27
    numerator = 1
    for i in range(0, len(list)):
        if list[i][0] == x0: #check number on times the state x0 is in list
            denominator = denominator + 1
            if i+1<len(list) and list[i+1][0] == x1 : #check number on times the state x1 is in list given x0 at state t-1
                numerator = numerator + 1
    return numerator / denominator           

f = open('results','w') #open file where the results are going to be printed
      
file_object = open('typos20.data', 'r')

list = file_object.readlines() #store lines

listAlphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']


##List to store values##
data_values = DoubleList()

for x in listAlphabet:
    data_values.append(x)

f.write("----------------------------Initial-------------------------\n") 
for x in listAlphabet:
        node_aux=data_values.searchNode(x)
        node_aux.initial = getInitial(x)
        string_result =  'P ( X[t] = ' + str(x) + ' ) =' + str(getInitial(x)) + '\n'
        f.write(string_result)

f.write("----------------------------Emission-------------------------\n") 
for x in listAlphabet: 
    node_aux=data_values.searchNode(x)
    for y in listAlphabet:
        node_aux.emission[y] = getEmission(y, x)
        string_result= 'P ( E[t] = ' +str(y) + ' | X[t]= ' + str(x) + ' ) = ' +  str(getEmission(y, x)) + '\n'
        f.write(string_result)
    f.write('\n')

f.write("----------------------------Transition-------------------------\n") 
for x in listAlphabet: 
    node_aux=data_values.searchNode(x)
    for y in listAlphabet:
        node_aux.transition[y] = getTransition(y, x)
        string_result = 'P ( X[t+1] = '+ str(y)+' | X[t] = '+str(x)+' ) = '+str(getTransition(y, x))+'\n'
        f.write(string_result)
    f.write('\n')
    
data_values.show()
        