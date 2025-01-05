class node:
  def __init__ (self,data=None,next=None):
    self.data=data
    self.next=next
class list:
    def __init__(self):
         self.head=None # the only one time the value assign of the node()
    def insertbegining(self,data):
         newnode=node(data,self.head)
         self.head=newnode
    def display(self):
         if(self.head==None):
            print("empty list it was")
            return
         else:
                                                        #  itr=self.head
            while self.head:                             # while itr:
               print("value " ,self.head.data," address is ",self.head.next)   #  print(itr.data,"  ",itr.next)
               self.head=self.head.next                    #itr=itr.next
if __name__ =='__main__':      
 n=list()
 n.insertbegining(6)
 n.insertbegining(9)
 n.insertbegining(11)
 n.display()