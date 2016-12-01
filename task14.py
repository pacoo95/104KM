### Graph creation with adjancency list
### with two classes (Vertex and Graph)
### and also stack and queue(for bfs and dfs functions)

class Vertex():
    def __init__(self,value): #contructor for class Vertex
        #print( "Created the", value, "vertex" )
        self.value = value
        self.adjlist = []

    def addedge(self,vertex):
        self.adjlist.append(vertex) #function for the vertex which adds the edge
        vertex.adjlist.append(self) # basically it appends the vertex to the adj list

class Queue():
    ''' Queue class for BFS'''
    
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        elem=self.queue[0]
        self.queue=self.queue[1:]
        return elem
    def isEmpty(self):
        return len(self.queue) == 0
    
class Stack():
    ''' Stack class for DFS'''
    
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0
    
class Graph():
    ''' class Grapgh, with constructor
       and node lists '''
    
    def __init__(self): # contructor for the nodelist
        self.nodelist = []
        
    def addnode(self,value): # append the node to the node list
        self.nodelist.append(  Vertex(value) )

        return self.nodelist[-1] # returns the last element from the node list
    
### Breadth First Search function
    def Breadth_first_search(self,v):
        ''' Breadth first search function
            implemented with Queue'''
        ## opening and writing the results into file
        f = open('Breadth_first_search.txt','w')
        q = Queue()
        visited = []    #an empty list where the visited nodes are stored
        q.enqueue(v)
        while not q.isEmpty():
            u = q.dequeue()
            if u not in visited:
                visited.append(u)
                for edge in u.adjlist:
                    q.enqueue(edge)
        s=''
        for i in visited:
            s+=str(i.value)+" "
        f.write(s)
        f.close()
        return None
### Depth First Search Function    
    def Depth_First_Search(self,v):
        '''Depth first search function
            implemented with stack '''
        ## opening and writing the results into file
        f = open('Depth_First_Search.txt','w')
        s = Stack()
        visited = [] #an empty list where the visited nodes are stored
        s.push(v)
        while not s.isEmpty():
            u = s.pop()
            if u not in visited:
                visited.append(u)
                for edge in u.adjlist:
                    s.push(edge)
                    

        s = ''
        for i in visited:
            s+=str(i.value)+" "
        f.write(s)
        f.close()
        return visited

    def display(self):
        '''Function which displays the graph'''
    
        for element in  self.nodelist: # for loop which goes through the node list
            print(element.value,": ",end='')
            for i in element.adjlist: # another for loop which goes through the adjencency list
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
    nodeP.addedge(nodeA)
    nodeA.addedge(nodeO)
    
    g.display()
# calling functions bfs and dfs for the graph above
    g.Breadth_first_search(nodeA)
    g.Depth_First_Search(nodeA)
