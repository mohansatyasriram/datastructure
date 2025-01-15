class graph:
    def __init__(self,edge):
        self.edge=edge
        self.graphsheet={}
        for start ,end in self.edge:
            if start in self.graphsheet:
                self.graphsheet[start].append(end)
            else:
                self.graphsheet[start]=[end]
    def optimistic(self,start,end,path=[]):
        path =path+[start]
        if start==end:
            return path
        if start  not in self.graphsheet:
            return None
        shortestpath=None
        for node in self.graphsheet[start]:
           if node not in path:
                sp=self.optimistic(node,end,path)
                if sp:
                    if shortestpath is None or len(sp)< len(shortestpath):
                        shortestpath=sp
        return shortestpath                
if __name__=='__main__':
    root=[

        ('mumbai','dubai'),
        ('mumbai','paris'),
        ('dubai','paris'),
        ('paris','newyork'),
        ('newyork','canada')
    ]
    root=graph(root)
    start="mumbai"
    end="newyork"                
    print(f"the shortestpath of the {start} and the {end} :",root.optimistic(start,end))