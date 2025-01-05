class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class list:
    def __init__(self):
        self.head=None
    def insertbegining(self,data):
        self.data=data
        newnode=node(self.data,self.head)
        self.head=newnode

    def insertl(self,data):
        self.data=data
        if(self.head==None):
            self.head=node(self.data,self.head)
            return
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=node(self.data,None)      
    def display(self):  
        itr=self.head
        while itr:
            print(itr.data,end='-->\n')
            itr=itr.next
    def positioninsert(self,data,index):
        c=1
        itr=self.head
        self.data=data
        self.index=index
        if(self.index==0):
            self.insertbegining(self.data)
            return
        while itr:
            if c==self.index:
                itr.next=node(self.data,itr.next)
                break
            itr=itr.next
            c+=1

        

if __name__ =='__main__':
 n=list()
 n.insertl(20)
 n.insertl(30)
 n.insertl(40)
 n.insertbegining(10)
 n.positioninsert(15,1)
 n.display()            