class bst:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def add(self,data):
        if self.data==data:
            return
        if self.data<data:
            if self.right:
               self.right.add(data)
            else:
               self.right=bst(data)
        else:
            if self.left:
                self.left.add(data)
            else:
                self.left=bst(data)    
    def min(self):
         while self.left:
              self=self.left
         return self.data    
    '''def max(self):
        while self.right:
            self=self.right
        return self.data '''
    def max(self):
        if self.right :
             return self.right.max()
        return self.data  
    def sum(self):
        total=self.data
        if self.left:
            total+=self.left.sum()
        if self.right:
            total+=self.right.sum()   

        return total        
if __name__=='__main__':
    element=[25,36,45,16,9,4,1]
    root=bst(element[0])
    for i in range(1,len(element)):
        root.add(element[i])
    print(root.min())   
    print(root.max()) 
    print(root.sum())
                