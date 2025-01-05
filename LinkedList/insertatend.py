class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class list:
    def __init__(self):
        self.head=None
    def insert(self,data):
        self.data=data
        if(self.head==None):
            self.head=node(self.data,self.head)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=node(data,None)
    def display(self):
           if self.head == None:
               print("empty list")
               return
           itr=self.head
           while itr:
                print(itr.data,itr.next)
                itr=itr.next            
if __name__ == '__main__':
    l= list()
    l.insert(20)
    l.insert(19)
    l.insert(99)
    l.display()