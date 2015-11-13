# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:56:41 2015

@author: felipemateosmartin
"""

from tree import tree
import numpy as np


arbol = tree(np.arange(4),"")
arbol.initTree()
arbol.fit()

        
 