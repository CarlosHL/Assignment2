    
    
class Node(object):
# Initializes the node object
    def __init__(self, key, char, listParent, listChildren, prev, next):
        #to link to the list
        self.prev = prev
        self.next = next
  
        self.key = key
        self.char = char
        self.parents = listParent
        self.children = listChildren
        # list with probabilities
        # for pollution and smoker, where High = T
        self.Prob = {}

        


#use this class to store open and closed nodes
class DoubleList(object):

    head = None
  
    def append(self, key, letter, listParent, listChildren):
        new_node = Node(key, letter, listParent, listChildren, None, None) 
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
    
    def searchNode(self, c):
        aux_node = self.head
    
        while aux_node is not None:
          if aux_node.char == c:
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
          print "key ", aux_node.key, " char", aux_node.char, " parents ", aux_node.parents, "children", aux_node.children 
          print aux_node.Prob
          aux_node = aux_node.next
    
        print "*" * 20