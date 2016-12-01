class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
### Stack is needed (or just is easier)
### to store the values in it and then just print them out
class Stack():
    def __init__(self):     #constructor
        self.stack = []
        
    def isEmpty(self):      #function which returns true when the lenght of the stack is 0
        return len(self.stack) == 0

    def push(self,item):    # function which appends an element into the stack
        self.stack.append(item)

    def pop(self):          #function which which pops out an element (and deletes it afterwards)
        return self.stack.pop()
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
    
### function to print out values in order from the Tree (iteratively) ### 
def in_order(tree):
    stack = Stack()     #create the stack
    t = tree            #assign the Tree to a variable
    res = True
    while res:          #while loop which iterates until "res" becomes False
        if t != None:   # checks if there is a Tree ?
            stack.push(t)   #if there is, appends the first value to the stack
            t = t.left      # and then continues to the left (thats how it is supposed to be - left then right)
            continue        #goes back to the beginning
        t=stack.pop()       # otherwise (when the iterator goes through the entire left side)
        ## we start popping out elements and printing them
        print(t.value)
        t = t.right #directs the iterator so that it goes to the right side of the Tree
        
        if stack.isEmpty() and t==None: ## if the stack AND the Tree are empty
            res=False       # break the iterator AND WE ARE DONEEEEE
        


## Calling the function (first inserting values, then printing them in order ###
if __name__ == '__main__':
   
  t=tree_insert(None,11);
  tree_insert(t,9)
  tree_insert(t,5)
  tree_insert(t,8)
  tree_insert(t,12)
  tree_insert(t,20)
  tree_insert(t,15)
  tree_insert(t,21)
  in_order(t)
