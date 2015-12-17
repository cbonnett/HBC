# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sat Nov  7 16:38:37 2015

@author: felipemateosmartin
"""

import numpy as np
from node import node
from itertools import permutations
import distributions as dist

class tree():
    
    
    def __init__(self,rawData,diffFunction):
        self.rawData = rawData
        self.diffFunction = diffFunction
        self.iterNodes={}
        self.nodes=[]
        self.activeNodes=[]
        self.node1=[node() for i,d in enumerate(rawData)]
        self.alpha =0.1
        print self.node1
        
    def initTree(self):
        [self.node1[i].populateNode(i,[],self.diffFunction)  for i,d  in enumerate(self.rawData)]
        [self.node1[i].initData(d)  for i,d  in enumerate(self.rawData)]
        self.activeNodes = [node.id for node in self.node1]
        print self.activeNodes
        
    def createPerm(self,nodesToMerge):
        return permutations(nodesToMerge,2)
    
        
    def probUnderH1(self,datos):
        #d = posibleNodesMerge[0].data     .extend(posibleNodesMerge[1].data)
        
        aux = dist.likelihood(datos)
        return aux.calculate([2.0],[1.0])
        
    #def mergedNodes(self):
        #nodes = list(self.createPerm(self.activeNodes))
  
    def fact(self,n):
        if(n==1):
            return 1
        else:
            return n*self.fact(n-1)
   
    def mergedNodes(self,node):
        nodes = list(self.createPerm(self.activeNodes))
        print "- 1 - Number of Nodes that could be merge : {0} ".format(len(self.activeNodes))

        rkList=[]
        allOtherVals=[]
        
        for duple in nodes:
             
            #print self.node1[duple[0]].data 
           
            #mergeCandidate=[self.node1[duple[0]],self.node1[duple[1]]]
            left =  self.node1[duple[0]]
            right = self.node1[duple[1]]
            datos = left.data + right.data 
            #print  mergeCandidate[0].data  , mergeCandidate[1].data           
            
            p1 = np.exp(self.probUnderH1(datos)) 
            alphaGamma = self.alpha*self.fact(len(datos)-1)
           
            
            dK = alphaGamma + left.dk*right.dk
            piK = alphaGamma/dK
           
            marginal = p1*piK + left.pTi*right.pTi*(left.dk*right.dk)/dK
           
            #rk = np.random.rand() #to be transformed.
                        
            rk = piK*p1/marginal
            
            print "------------------"
            print "rk:{6},p1:{0},alphaGamma:{1},dK:{2},marginal:{3},idleft:{4},idright:{5}".format(p1,alphaGamma,dK,marginal,left.id,right.id,rk)
            print "left.pTi:{0},right.pTi:{1},rest:{2},piK:{3}".format(left.pTi,right.pTi,(left.dk*right.dk)/dK,piK)
           
            allOtherVals.append((dK,piK,p1,marginal))
                 
            rkList.append(rk)

        maxIndex = rkList.index(np.max(rkList))       
        cadidateIndex = list(nodes[maxIndex]) 
        
        print "- 2 - Nodes to merge {0}".format(cadidateIndex)
        mergeCandidate=[self.node1[cadidateIndex[0]],self.node1[cadidateIndex[1]]]
        
        nodeMerge = node()
        nodeMergeId=max([i.id for i in self.node1])+1
        print "- 3 - New Node Crated with id {0}".format(nodeMergeId)
        nodeMerge.populateNode(nodeMergeId,mergeCandidate,self.diffFunction)
        nodeMerge.repopulateVals(allOtherVals[maxIndex])
        
        [self.activeNodes.remove(elem.id) for elem in nodeMerge.children]
        self.activeNodes.append(nodeMerge.id)        
        self.node1.append(nodeMerge.merge())
        print "Node Created :"
        self.node1[-1].toString()
        

    def fit(self):
        count=0
        while ( len(self.activeNodes)!=1):
                count +=1
                print "Loop number {0} : ___________________________________".format(count)                
                self.mergedNodes(node)
                

        
if __name__ == "__main__":

    arbol = tree(np.arange(10),"")
    arbol.initTree()
    arbol.fit()

        
