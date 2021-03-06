class Node:
    def __init__(self,data,next_node):
        self.data=data
        self.next_node=next_node

class LinkedList:

    head=None
    def insertAtStart(self,value:int):
            node = Node(value,self.head)
            self.head=node

    def printList(self):
        if(self.head==None):
            return print("list  empty")
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next_node        
    
    def reverseLinkedList(self):

       
        current= self.head
        prev = None
        
        

        while current:

            temp = current.next_node
            current.next_node=prev
            prev=current
            current=temp
         
        self.head=prev

            
        


    

    def insertAtEnd(self,value:int):
        if(self.head==None):
            self.head=Node(value,None)
            return
        temp=self.head
        last=None
        while temp:
            last=temp
            temp = temp.next_node
          
        node= Node(value,None)
        last.next_node=node
    
    def deleteNode(self,position):
        return
    def updateNode(self,position,value):
        return
 

    

    



     
        
             
      
             







          
list=LinkedList()
list.insertAtStart(5)
list.insertAtStart(3)
list.insertAtStart(4)
list.insertAtEnd(1)
list.printList()
print("inversed")
list.reverseLinkedList()
list.printList()
