class node:
    def __init__(self,data=None,pre=None,next=None):
        self.data=data
        self.pre=pre
        self.next=next
class dlist:
    def __init__(self):
        self.head=None
    def insertbegining(self,data):
        self.data=data
        if(self.head==None):
            self.head=node(self.data,None,None)
            return
        newnode=node(self.data,None,self.head)
        self.head.pre=newnode        #self.head=node(self.data,None,self.head)
                                      # self.head.next.pre=self.head                                                                 
        self.head=newnode
    def insertend(self,data):
        self.data=data
        itr=self.head
        while itr.next:
            itr=itr.next
        newnode=node(self.data,itr,None)
        itr.next=newnode
    def remove(self,index):
        self.index=index
        c=1
        itr=self.head
        while itr:
            if(c==self.index):
                itr.next=itr.next.next
                itr.next.pre=itr
            itr=itr.next
            c+=1        
    def display(self):
        itr=self.head
        while itr:
            print(itr.data)
            itr=itr.next 
    def insertmiddle(self,index,data):
        self.index=index
        self.data=data
        c=1
        itr=self.head
        while itr:
            if(c==self.index):
                newnode=node(self.data,itr,itr.next)
                itr.next.pre=newnode
                itr.next=newnode
            itr=itr.next
            c+=1

        
if __name__=='__main__':
    n=dlist()
    n.insertbegining(2)   
    n.insertbegining(1)
    n.insertbegining(0)
    n.insertend(3)
    n.remove(2)
    n.insertmiddle(2,2)
    n.display()      