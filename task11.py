class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
### Double linked list delete node function below ###              
      def remove(self,n):         
            if n.prev!=None:              #if previois element is different than None
                  n.prev.next = n.next    # if its true: we set the pointer to the next value
            else:
                  self.head=n.next        #otherwise we set the head to point to the next element
            if n.next!=None:              # if the next element is different than None
                  n.next.prev=n.prev      # we set the pointer from 
            else:
                  self.tail=n.prev        #otherwise 
                  
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
         
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(7))
      l.insert(l.head,Node(8))
      l.insert(l.head,Node(9))
      l.insert(l.head,Node(10))
      l.insert(l.head,Node(11))
      l.display()
### while loop to delete an element which is anywhere apart from the head or tail ###      
      step=l.head
      while step!=l.tail:
            if step.value==9:
                  l.remove(step)
                  print("Middle value deleted!")
                  l.display()
                  print()
                  break
            else:
                  step=step.next
      l.display()
      l.remove(l.head)
      print("Head deleted!")
      print()
      l.display()
      l.remove(l.tail)
      print("Tail deleted!")
      print()
      l.display()
    
