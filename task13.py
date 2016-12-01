### Graph creation with adjancency list
### with two classes (Vertex and Graph)
class Vertex():
    ''' class Vertex, with constructor
        and adjencency lists'''
    def __init__(self,value):   #contructor for class Vertex
        #print( "Created the", value, "vertex" )
        self.value = value
        self.adjlist = []

    def addedge(self,vertex):   #function for the vertex which adds the edge
        self.adjlist.append(vertex) # basically it appends the vertex to the adj list
        vertex.adjlist.append(self) 

class Graph():
    ''' class Grapgh, with constructor
       and node lists '''
    def __init__(self):     # contructor for the nodelist 
        self.nodelist = []
        
    def addnode(self,value): # append the node to the node list
        self.nodelist.append(  Vertex(value) )

        return self.nodelist[-1]    # returns the last element from the node list


### function which displays the graph
    def display(self):

        for element in  self.nodelist: # for loop which goes through the node list
            print(element.value,": ",end='')
            for i in element.adjlist:   # another for loop which goes thrugh the adjencency list
                print(str(i.value),end=' ')
            print()
if __name__ == '__main__':
### adding the nodes and then displaying them
    g = Graph()
    nodeA = g.addnode('A')
    nodeB = g.addnode('B')
    nodeD = g.addnode('D')
    nodeC = g.addnode('C')
    nodeP = g.addnode('P')
    nodeO = g.addnode('O')
    nodeA.addedge(nodeB)
    nodeB.addedge(nodeC)
    nodeC.addedge(nodeA)
    nodeC.addedge(nodeP)
    nodeD.addedge(nodeO)
    g.display()
