
class Location(object):
    def __init__(self, row, col):
        self.row = row
        self.col= col
    
    
class Node(object):
# Initializes the node object
    def __init__(self, key, location, heuristic, terrain, listEdges, prev, next):
        #to link to the list
        self.prev = prev
        self.next = next
  
        self.location = location
        self.key = key
        self.edges = listEdges
        self.heuristic = heuristic
        self.terrain = terrain 
        self.parent = None
        self.f = None
        self.g = None


#use this class to store open and closed nodes
class DoubleList(object):

    head = None
  
    def append(self, key, location, heuristic, terrain, listEdges):
        new_node = Node(key, location, heuristic, terrain, listEdges, None, None) 
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
          print "key %d, terrain penalization %d, heuristic %d" % (aux_node.key, aux_node.terrain, aux_node.heuristic)
          print "adjacent are", aux_node.edges
          aux_node = aux_node.next
    
        print "*" * 20