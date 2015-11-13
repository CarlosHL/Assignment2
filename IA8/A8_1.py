from __future__ import division
        
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


f.write("----------------------------Initial-------------------------\n") 
for x in listAlphabet:
        string_result =  'P ( X[0] = ' + str(x) + ' ) =' + str(getInitial(x)) + '\n'
        f.write(string_result)

f.write("----------------------------Emission-------------------------\n") 
for x in listAlphabet: 
    for y in listAlphabet:
        string_result= 'P ( E[t] = ' +str(y) + ' | X[t]= ' + str(x) + ' ) = ' +  str(getEmission(y, x)) + '\n'
        f.write(string_result)
    f.write('\n')

f.write("----------------------------Transition-------------------------\n") 
for x in listAlphabet: 
    for y in listAlphabet:
        string_result = 'P ( X[t+1] = '+ str(y)+' | X[t] = '+str(x)+' ) = '+str(getTransition(y, x))+'\n'
        f.write(string_result)
    f.write('\n')