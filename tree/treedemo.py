class treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def display(self):
        print(self.data)      
        for child in self.children:
             print(child.data)
    def total_display(self):
         space=self.space()
         prefix=space*'  '+'|-->'
         print(prefix,self.data)
         if self.children:  #or len(self.children)>0
          for child in self.children:
              child.total_display()         
    def space(self):
        p=self.parent
        level=0
        while p:    #its go up33
          level+=1
          p=p.parent
        return level  
    
if __name__ =='__main__':
        root=treenode('device')
        #laptop
        laptop=treenode('laptop')
        root.add_child(laptop)
        laptop.add_child(treenode('asus'))
        laptop.add_child(treenode('dell'))
        laptop.add_child(treenode('hp'))
        #
        mobile=treenode('mobile')
        root.add_child(mobile)
        mobile.add_child(treenode('motrola'))
        mobile.add_child(treenode('apple'))
        mobile.add_child(treenode('galaxy'))  
        root.display()
        root.total_display()
        

        
        

