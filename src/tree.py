# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sat Nov  7 16:38:37 2015

@author: felipemateosmartin
"""

import numpy as np
from node import node
from itertools import permutations

class tree():
    
    
    def __init__(self,rawData,diffFunction):
        self.rawData = rawData
        self.diffFunction = diffFunction
        self.iterNodes={}
        self.nodes=[]
        self.activeNodes=[]
        self.node1=[node() for i,d in enumerate(rawData)]
        print self.node1
        
    def initTree(self):
        [self.node1[i].populateNode(i,[],self.diffFunction)  for i,d  in enumerate(self.rawData)]
        [self.node1[i].initData(d)  for i,d  in enumerate(self.rawData)]
        self.activeNodes = [node.id for node in self.node1]
        print self.activeNodes
        
    def createPerm(self,nodesToMerge):
        return permutations(nodesToMerge,2)
    

    #def mergedNodes(self):
        #nodes = list(self.createPerm(self.activeNodes))

    def mergedNodes(self,node):
        nodes = list(self.createPerm(self.activeNodes))
        print "- 1 - Number of Nodes that could be merge : {0} ".format(len(self.activeNodes))

        rkList=[]
        for duple in nodes:

            rk = np.random.rand() #to be transformed.
            
            rkList.append(rk)

        cadidateIndex = list(nodes[rkList.index(np.max(rkList))]) 
        print "- 2 - Nodes to merge {0}".format(cadidateIndex)
        mergeCandidate=[self.node1[cadidateIndex[0]],self.node1[cadidateIndex[1]]]
        
        nodeMerge = node()
        nodeMergeId=max([i.id for i in self.node1])+1
        print "- 3 - New Node Crated with id {0}".format(nodeMergeId)
        nodeMerge.populateNode(nodeMergeId,mergeCandidate,self.diffFunction)
        
        
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

        
