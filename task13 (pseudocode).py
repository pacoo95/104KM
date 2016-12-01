CLASS VERTEX()
        value <- 0
        adjlist <- []
        
    ADDEDGE(VERTEX)
        append vertex to adjlist

    
CLASS GRAPH()
    nodelist <- []
    
    ADDNODE(VERTEX)
        append Vertex(value) to nodelist
        return last element of nodelist

    DISPLAY()
        for element in nodelist
            print value of element

            for edge in adjlist of element
                print edge

g <- new Graph 

nodeA <- g.ADDNODE('A')
nodeB <- g.ADDNODE('B')
nodeC <- g.ADDNODE('C')

nodeA.ADDEDGE(nodeB)
nodeB.ADDEDGE(nodeC)
nodeC.ADDEDGE(nodeA)
g.DISPLAY()

        



