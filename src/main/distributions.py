# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:45:07 2015

@author: felipemateosmartin
"""

#Hyperparameters:
import numpy as np
from scipy.stats import chi2 , multivariate_normal

class likelihood():
    def __init__(self,data):
        self.data=data
        
    def calculate(self,m,S):
        dataLikelyHood=0
        for i in self.data:
            #Many of the prob calculated here will be redundant when used upper levels of the tree.
            print "multivaritate normal {0}".format(np.log(multivariate_normal.pdf(i, mean=m, cov=S)))
            dataLikelyHood += np.log(multivariate_normal.pdf(i, mean=m, cov=S))
        return dataLikelyHood           

class NormalInverseWishartDistribution(object):
    def __init__(self, mu, lmbda, nu, psi):
        self.mu = mu
        self.lmbda = float(lmbda)
        self.nu = nu
        self.psi = psi
        self.inv_psi = np.linalg.inv(psi)
        self.cholesky = np.linalg.cholesky(self.inv_psi)

    def sample(self):
        sigma = np.linalg.inv(self.wishartrand())
        
        return (np.random.multivariate_normal(self.mu, sigma / float(self.lmbda)), sigma)

    def wishartrand(self):
        dim = self.inv_psi.shape[0]
        foo = np.zeros((dim,dim))

        for i in range(dim):
            for j in range(i+1):
                if i == j:
                    foo[i,j] = np.sqrt(chi2.rvs(self.nu-(i+1)+1))
                else:
                    foo[i,j]  = np.random.normal(0,1)
        return np.dot(self.cholesky, np.dot(foo, np.dot(foo.T, self.cholesky.T)))

if __name__ == "__main__":
    
    x = NormalInverseWishartDistribution(np.array([0,0]),1.,3.,np.eye(2))
    samples = [x.sample() for _ in range(1000)]
    var_ = np.array([variance for mean,variance in samples])
    mean_ = np.array([mean for mean,variance in samples])
    
    var_mean = np.mean(var_,axis=0)
    mean_mean =np.mean(mean_,axis=0)
    l=likelihood([[0,0],[0,0]]).calculate(mean_mean,var_mean)
    print mean_mean,var_mean 
    #print  mean_samples #var_samples
    #print 'mean: {0}'.format(np.mean(mean_, axis=0))
    # Should be close to the identity matrix, but usually is close to I*5
