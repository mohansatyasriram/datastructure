class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class list:
    def __init__(self):
        self.head=None
    def insertll(self,data):
        self.data=data
        if(self.head==None):
            self.head=node(self.data,self.head)
            return
        else:
            itr=self.head
            while itr.next:#why use itr.next means in insertl we have to assign the value at itr.next when we print(itr.next) it show the Nonetype error
                itr=itr.next
            itr.next=node(self.data,None)      
    def display(self):   #print
        itr=self.head
        while itr:
            print(itr.data,end='-->\n')
            itr=itr.next
    def length(self): #length
        itr=self.head
        c=0
        while itr:
            c+=1
            itr=itr.next 
        print("the length is :",c)
        return c  
    def insertl_values(self,data):# multiple values
        for datai in data:
            self.insertl(datai)  
    def remove(self,index):
        self.index=index
        c=0
        if(self.index<0 or self.index >self.length()-2):
            raise Exception ("index out bound erorr")
        else:
            itr=self.head
            while itr:
                if (self.index==c):
                    itr.next=itr.next.next
                    break
                c+=1
                itr=itr.next 

if __name__ =='__main__':
    n=list()
    n.insertl(20)
    n.insertl(30)
    n.insertl(40)
    n.insertl_values([50,60,70])
    n.remove(4)
    n.display()
    n.length()