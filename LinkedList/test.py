class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class list:
    def __init__(self):
        self.head=None
    def insertbegining(self,data):
        self.data=data
        self.head=node(self.data,self.head)
    def display(self):
        itr=self.head
        while itr:
            print(itr.data)
            itr=itr.next 
    def insertend(self,data):
        self.data=data
        if(self.head==None):
            self.head=node(self.data,None)
            return
        itr=self.head
        while itr.next:
          itr=itr.next
        itr.next=node(self.data,None) 
    def insertmiddle(self,data,index):
        self.data=data
        self.index=index
        itr=self.head
        c=1
        while itr:
            if(c==self.index):
                itr.next=node(data,itr.next)
            itr=itr.next
            c+=1
    def remove(self,index):
        self.index=index
        c=1
        itr=self.head
        while itr:
            if(c==self.index):
                itr.next=itr.next.next
                return 
            itr=itr.next
            c+=1        

if __name__ =='__main__':
   l=list()
   l.insertbegining(2)
   l.insertbegining(1)
   l.insertend(4)
   l.insertmiddle(3,2)
   l.remove(2)
   l.display()