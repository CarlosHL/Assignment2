import getopt, sys
import listNode

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)
    for o, a in opts:
		if o in ("-p"):
			print "flag", o
			print "args", a
			print a[0]
			print float(a[1:])
			setPrior(a[0], float(a[1:]))
			
		elif o in ("-m"):
			print "flag", o
			print "args", a
			print type(a)
			print calcMarginal(a)
			
		elif o in ("-g"):
			print "flag", o
			print "args", a
			print type(a)
			'''you may want to parse a here and pass the left of |
			and right of | as arguments to calcConditional
			'''
			p = a.find("|")
			print a[:p]
			print a[p+1:]
			if a[p+1:] == a[p+1]:
			    print calcConditional(a[:p], a[p+1:])
			else:
			    conditions = []
			    for x in a[p+1:]:
			        conditions.append(x)
			        
			    print calcMultiConditional(a[:p], conditions)

			
		elif o in ("-j"):
			print "flag", o
			print "args", a
			jointVar = []
			p = a.find("")
			for x in a[p:]:
			        jointVar.append(x)
			print calcJoint(jointVar)

			
			
			
			
		else:
			assert False, "unhandled option"
		
    # ...
def setPrior(a, b):
    bayes.searchNode(a).Prob = {'T' : b, 'F' : 1-b}
    
def calcMarginal(a):
    node = bayes.searchNode(a)
    marginal = 0
    if not node.parents:
        return node.Prob['T']
    elif len(node.parents) == 2: 
        for n in node.Prob:
            parent1 = bayes.searchNode(bayes.searchNode(a).parents[0])
            parent2 = bayes.searchNode(bayes.searchNode(a).parents[1])
            if n == "TT":
                marginal = marginal + node.Prob['TT'] * parent1.Prob['T'] * parent2.Prob['T']
            if n == "TF":
                marginal = marginal + node.Prob['TF'] * parent1.Prob['T'] * parent2.Prob['F']
            if n == "FT":
                marginal = marginal + node.Prob['FT'] * parent1.Prob['F'] * parent2.Prob['T']
            if n == "FF":
                marginal = marginal + node.Prob['FF'] * parent1.Prob['F'] * parent2.Prob['F']
        return marginal
    else:
        parent1 = bayes.searchNode(bayes.searchNode(a).parents[0])
        marginal = marginal + node.Prob['T'] * calcMarginal(parent1.char)
        marginal = marginal + node.Prob['F'] * (1 - calcMarginal(parent1.char))
        return marginal
        

def calcConditional(a, b): #if one argument
    node_ask = bayes.searchNode(a)
    node_con = bayes.searchNode(b)
    conditional = 0
    if node_con == node_ask:
        return 1
    if not node_con.parents and not node_ask.parents:
        return node_ask.Prob['T'] 
    elif a in node_con.children:
        
        for n in node_con.children:
            if n == a and node_ask.children:
                parent1 = bayes.searchNode(bayes.searchNode(a).parents[0])
                parent2 = bayes.searchNode(bayes.searchNode(a).parents[1])
                if (b=='S'):
                    conditional = (node_ask.Prob['TT'] * parent1.Prob['T'] * parent2.Prob['T'] 
                        + node_ask.Prob['FT'] * parent1.Prob['F'] * parent2.Prob['T'])/node_con.Prob['T']
                else:
                    print "not here"
                    conditional = (node_ask.Prob['TT'] * parent1.Prob['T'] * parent2.Prob['T'] 
                        + node_ask.Prob['TF'] * parent1.Prob['T'] * parent2.Prob['F'])/node_con.Prob['T']
                return conditional
                
    elif not node_ask.children and not node_con.parents:
        parent = bayes.searchNode(bayes.searchNode(a).parents[0])
        if (b =='P'):
            conditional = (conditional + node_ask.Prob['T'] * parent.Prob['TT'] * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                    node_ask.Prob['T'] * parent.Prob['TF'] * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['F'] +
                                    node_ask.Prob['F'] * (1-parent.Prob['TT']) * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                    node_ask.Prob['F'] * (1-parent.Prob['TF']) * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['F'])/(parent.Prob['TT'] * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                     parent.Prob['TF'] * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['F'] +
                                     (1-parent.Prob['TT']) * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                     (1-parent.Prob['TF']) * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['F'])
        else:
            conditional = (conditional + node_ask.Prob['T'] * parent.Prob['TT'] * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                    node_ask.Prob['T'] * parent.Prob['FT'] * bayes.searchNode(parent.parents[0]).Prob['F'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                    node_ask.Prob['F'] * (1-parent.Prob['TT']) * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                    node_ask.Prob['F'] * (1-parent.Prob['FT']) * bayes.searchNode(parent.parents[0]).Prob['F'] * bayes.searchNode(parent.parents[1]).Prob['T'])/(parent.Prob['TT'] * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                     parent.Prob['FT'] * bayes.searchNode(parent.parents[0]).Prob['F'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                     (1-parent.Prob['TT']) * bayes.searchNode(parent.parents[0]).Prob['T'] * bayes.searchNode(parent.parents[1]).Prob['T'] +
                                     (1-parent.Prob['FT']) * bayes.searchNode(parent.parents[0]).Prob['F'] * bayes.searchNode(parent.parents[1]).Prob['T'])
        return conditional
        
    elif b in node_ask.children and not node_con.children:
        conditional = node_con.Prob['T'] * calcMarginal(a) / node_con.Prob['F']
        return conditional
    
    elif not node_ask.children and not node_con.children:
        return node_ask.Prob['T'] * calcConditional('C', b) + node_ask.Prob['F'] *(1-calcConditional('C', b))
    
    elif not node_ask.parents and not node_con.children:
        return calcConditional(b, a) * node_ask.Prob['T'] /(calcMarginal(b))
        
#covered three first columns, starting with  C
    elif node_con.children and node_con.parents:
        if not node_ask.parents:
            return calcConditional(b, a) * node_ask.Prob['T'] /calcMarginal(b)   
        else:
            return  node_ask.Prob['T']
   
    
    return node_ask.Prob['T']


def calcMultiConditional(a, conList):
    if a in conList:
        return 1
    
    #two conditionals and one two know
    ask = bayes.searchNode(a) 
    firstCon = bayes.searchNode(conList[0]) 
    secondCon = bayes.searchNode(conList[1]) 
     
    #intercasual
    if firstCon.children and secondCon.children and (firstCon.parents or secondCon.parents):
        if not ask.children:
            return ask.Prob['T']
        else:
            if ask.children[0] in conList:
                return (bayes.searchNode('C').Prob['TT'] * ask.Prob['T'])/calcConditional(conList[1], conList[0])
    else:
        #combined
        if not ask.parents:
            if firstCon.parents:
                node_aux = firstCon
            else:
                node_aux = secondCon
            return calcConditional(a, node_aux.char)
            
        if ask.children:
            if not firstCon.children:
                node_aux = firstCon
                node_aux2 = secondCon
            else:
                node_aux = secondCon
                node_aux2 = firstCon
            return node_aux.Prob['T'] * calcConditional(a, node_aux2.char)/calcConditional(node_aux.char, node_aux2.char)
        
        else:
            return ask.Prob['T'] * calcMultiConditional(ask.parents[0], conList) + ask.Prob['F'] * (1-calcMultiConditional(ask.parents[0], conList))
               
        

#joint    
def calcJoint(jointVar):
    pos = -1
    result = 1
    iteration = 0
    print len(jointVar)
    for x in range(0, len(jointVar)):
        if jointVar[pos] == '~':
            pos = pos - 1 
        else:
            if not bayes.searchNode(jointVar[pos]).children:
                result = result * calcConditional(jointVar[pos], jointVar[pos+1])

            if bayes.searchNode(jointVar[pos]).children and bayes.searchNode(jointVar[pos]).parents:
                result = result * calcMarginal(jointVar[pos])
                
        
            pos = pos - 1 
            
        iteration = iteration + 1
        
    return result
        
def createNet():
    bayesNet = listNode.DoubleList()
    bayesNet.append(1, 'P', [], ['C'])
    bayesNet.searchNode('P').Prob = {'T' : 0.1, 'F' : 0.9}
    bayesNet.append(2, 'S', [], ['C'])
    bayesNet.searchNode('S').Prob = {'T' : 0.3, 'F' : 0.7}
    bayesNet.append(3, 'C', ['P', 'S'], ['X', 'D'])
    bayesNet.searchNode('C').Prob = { 'TT' : 0.05, 'TF' : 0.02, 'FT' : 0.03, 'FF' : 0.001} #first char referes to P
    bayesNet.append(4, 'X', ['C'], [])
    bayesNet.searchNode('X').Prob = {'T' : 0.9, 'F' : 0.2}
    bayesNet.append(5, 'D', ['C'], [])
    bayesNet.searchNode('D').Prob = {'T' : 0.65, 'F' : 0.3}
    return bayesNet
    
    
    
                    
if __name__ == "__main__":
    
    bayes = createNet()
    main()
    #bayes.show()