class graph:
    def __init__(self,edge):
        self.edge=edge
        self.graphsheet={}
        for start ,end in self.edge:  
            if start in self.graphsheet:
                self.graphsheet[start].append(end)
            else:
                self.graphsheet[start]=[end]    
        print(self.graphsheet)
    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graphsheet:
            return []
        paths=[]
        for node in self.graphsheet[start]:
            if node not in path:
                newpath=self.get_path(node,end,path)
                for p in newpath:
                    paths.append(p)
        return paths
   
        

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
    print(f"paths between {start} and {end}:",root.get_path(start,end))