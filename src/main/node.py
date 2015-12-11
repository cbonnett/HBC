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
import distributions as dist
import numpy as np

class node():
    
    def populateNode(self,id,children,diffFunction):
        '''
        args : id : int , unique identifier for the node
               children : a list of nodes that are the children.
               diffFunction : The function  used to decide which 2 nodes to merge.
        '''
        self.alpha = 0.1
        self.data=[]
        self.id=id
        self.left=0
        self.right=0
        self.children=children
        
        self.dk=self.alpha #Stores the value of the object dk  as the probability of the data.
        self.pik=1
        self.pH1=0
        self.pTi=0
    
    def __init__(self):
        pass

    def merge(self):
        '''
        function that merge the data ( o points ) in the childrens .
        '''
        self.left=self.children[0]
        self.right=self.children[1]
        self.data=self.left.data + self.right.data
        
        return self
    
  

    '''    
    def calcDiff(self,left,righ):
        self.diff = funct(left.id,righ.id)
    '''
    
    def initData(self,dataInit):
        '''
        fills the data variables of the object node.
        '''
        #print type(dataInit)
        #if(len(self.data)==0):
        #    self.data=list(dataInit)
        #else:

        self.data.extend([dataInit])
        self.pTi = np.exp(dist.likelihood(self.data).calculate([0.0],[1.0]))
        self.pH1 = self.pTi 
     
    
    def toString(self):
        '''
        Personalize the printing of the object node.
        '''
        print "-- Node With id {0} , and children {1}".format(self.id,[i.id for i in self.children])
        print "-- With data {0})".format(self.data) 
        
        #for e in self.data:
           #print e
        
    def repopulateVals(self,valsToRepopulate):
        self.dk=valsToRepopulate[0] #Stores the value of the object dk  as the probability of the data.
        self.pik=valsToRepopulate[1]
        self.pH1=valsToRepopulate[2]
        self.pTi=valsToRepopulate[3]
    
        
if __name__ == "__main__":
    t = node()
    t.populateNode(1,[],"")
    t.initData(1)
    
    r = node()
    r.populateNode(2,[0,2],"")
    r.initData(2)
    
    y=node()
    y.populateNode(3,[t,r],"")
    y.merge()
    print y.data


