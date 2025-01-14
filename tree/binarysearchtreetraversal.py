from collections import deque
class binarysearch:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add(self,data):
        if(self.data==data):
            return
        if(data<self.data):
            if self.left:
                self.left.add(data)
            else:
                self.left=binarysearch(data)          
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right=binarysearch(data)
    def in_order(self):
        element=[]
        if self.left:
            element += self.left.in_order()
        element.append(self.data)
        if self.right:
            element += self.right.in_order()
        return element
    def pre_order(self):
        element=[]
        element.append(self.data)
        if self.left:
            element+=self.left.pre_order()
        if self.right:
            element+=self.right.pre_order()   

        return element
    
    def post_order(self):
        element=[]
        if self.left:
            element+=self.left.pre_order()
        if self.right:
            element+=self.right.pre_order()   
        element.append(self.data)
        return element
    def bfs(self):
        element = []
        queue = deque([self]) 
        while queue:
            node = queue.popleft()
            element.append(node.data) 
            if node.left:
                queue.append(node.left)  
            if node.right:
                queue.append(node.right) 
        return element
def build_tree(element):
    root=binarysearch(element[0])
    for i in range (1,len(element)):
        root.add(element[i])
    return root
if __name__=='__main__':
    numbers=[17,4,1,20,9,23,18,34,18,4]    
    tree=build_tree(numbers)
    print(tree.in_order())
    print(tree.pre_order())
    print(tree.post_order())
    print(tree.bfs())
