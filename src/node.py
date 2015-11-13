# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sat Nov  7 16:36:35 2015

@author: felipemateosmartin
=======
Created on Sat Nov  7 20:55:16 2015

@author: felipemateosmartin


Class node

>>>>>>> felipe
"""

class node():
    
    def populateNode(self,id,children,diffFunction):
        self.data=[]
        self.id=id
        self.left=0
        self.right=0
        self.children=children
    
    def __init__(self):
        pass

    def merge(self):
        self.left=self.children[0]
        self.right=self.children[1]
        self.data=self.left.data + self.right.data
        return self

        
    def calcDiff(self,left,righ):
        self.diff = funct(left.id,righ.id)
        
    def initData(self,dataInit):
        self.data=dataInit
        self.data.extend([dataInit])
        
    def toString(self):
        print "-- Node With id {0} , and children {1}".format(self.id,[i.id for i in self.children])
        print "-- With data {0})".format(self.data)        

if __name__ == "__main__":
    t = node()
    t.populateNode(1,[3,2],"")
    t.initData([1,2,3])
    
    r = node()
    r.populateNode(2,[0,2],"")
    r.initData([1,1,1])
    
    y=node()
    y.populateNode(3,[t,r],"")
    y.merge()
    print y.data


