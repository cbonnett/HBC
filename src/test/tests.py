# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:34:57 2015

@author: felipemateosmartin
"""
#adding module to the pythonpath for testing
import sys,os
lev1 =  os.getcwd()[0:os.getcwd().rfind("/")]
lev2 =  lev1[0:lev1.rfind("/")]
topDir=lev2 
if not topDir in sys.path:
    sys.path.append(topDir)
from  src.main import distributions,node,tree
import numpy as np
import unittest

class Tests(unittest.TestCase):

    def test_NormalInverseWhisart(self):
        rv = distributions.NormalInverseWishartDistribution(np.array([0,0]),1.,3.,np.eye(2))
        result = rv.sample()
        self.assertEqual(len(result[0]),2)
        self.assertTrue(np.linalg.det(result[1])>=0)
        
    def test_likelihood(self):
        result = distributions.likelihood([[0,0],[0,0]]).calculate([0.0,0.0],np.eye(2))
        self.assertTrue(result<0)
        self.assertTrue(np.exp(result)<=1)
        
    def test_Nodes_Botton_Node(self):
        #Creating a botton node.
        bottonLeave = node.node()
        bottonLeave.populateNode(1,[],"")
        bottonLeave.initData([1])
        #Data Stored correctly
        data =np.array([a==b for a,b in zip(bottonLeave.data,[1])]).all() 
        self.assertEquals(data,True,msg="Data inputed correctly")
        self.assertEquals(bottonLeave.id,1,msg="Id Assign Correctly")
        self.assertEquals(len(bottonLeave.children),0,msg="It has no children")
        
    def test_Merge_Nodes(self):
        #Leave node 
        leftNode = node.node()
        leftNode.populateNode(1,[],"")
        leftNode.initData([1,2,3])
        #Not Leave Node
        rightNode = node.node()
        rightNode.populateNode(1,[2,3],"")
        rightNode.initData([2,3])
        #Merging
        mergeNode = node.node()
        mergeNode.populateNode(3,[leftNode,rightNode],"")
        mergeNode.merge()
        #Test
        data = np.array([a==b for a,b in zip(mergeNode.data,[1,2,3])]).all()
        self.assertEquals(data,True,msg="Data from children incorrectly merge.")
        self.assertEquals(mergeNode.id,3,msg="Id assingment wrong")
        children = np.array([a==b for a,b in zip(mergeNode.children,[leftNode,rightNode])]).all()
        self.assertEquals(children,True,msg="Children list not properly built")
        
suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
unittest.TextTestRunner(verbosity=2).run(suite)        

