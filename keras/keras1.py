#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt

n_pts=500
np.random.seed(0)
Xa=np.array([np.random.normal(13,2,n_pts),
             np.random.normal(12,2,n_pts)]).T
Xb=np.array([np.random.normal(8,2,n_pts),
             np.random.normal(8,2,n_pts)]).T 
X=np.vstack((Xa,Xb))
y=np.matrix(np.append(np.zeros(n_pts),np.ones(n_pts))).T
print(X)
print(y)
plt.scatter(X[:n_pts,0],X[:n_pts,1])
plt.scatter(X[n_pts:,0],X[n_pts:,1])
