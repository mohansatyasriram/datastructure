class tree:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.children=[]
    def add(self,child):
        child.parent=self
        self.children.append(child)
    def display(self,level):
        if self.space()>level:
            return
        spaces=self.space()
        prefix=spaces*'     '+'-->'
        print(prefix,self.data)    
        if self.children:
            for child in self.children:
                child.display(level)
    def space(self):
        p=self.parent
        l=0
        while p:
            l+=1
            p=p.parent 
        return l               
if __name__=='__main__':
    root=tree('global')
    india=tree('india')
    usa=tree('usa')
    root.add(india)
    root.add(usa)    
    andhra=tree('andhra')
    ts=tree('telengana')
    alaska=tree('alska')
    newyork=tree('newyork')
    india.add(andhra)
    india.add(ts)
    usa.add(alaska)
    usa.add(newyork)
    newyork.add(tree('town1'))    
    newyork.add(tree('town2'))
    alaska.add(tree('snow 1'))    
    andhra.add(tree('vizag'))
    andhra.add(tree('amaravathi'))
    ts.add(tree('hyderbad'))  
    root.display(1) 