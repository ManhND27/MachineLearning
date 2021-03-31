import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('./data/admission.txt', delimiter=",")
X = data[:,0:2]
a = np.ones((X.shape[0],1))
X = np.concatenate((a, X),axis=1)
#print(X)

y = data[:,-1]

def sigmoid(theta, X):
    z = 1 / (1 + np.exp(-np.dot(X,theta)))
    return z

def loss(theta,X,y):
    J = np.dot(y.T,np.log(sigmoid(theta,X))) - np.dot((1-y).T,np.log(1-sigmoid(theta,X)))
    return -J/len(y)

def gradient(theta,X,y):
    denta = np.dot(X.T,(sigmoid(theta,X)-y))
    return denta/len(y)

 
 #print(N) 
def train(X,y,anpha = 0.01,T = 1000):
    N,D = np.shape(X)
    thetas = np.zeros((D,T))
    for i in range(1,T-1):
        denta = gradient(thetas[:,i],X,y)
        thetas[:,i+1]= thetas[:,i] - anpha*denta
    return thetas

N,D = np.shape(X)
print(N,D)
k = train(X,y)
print(k)
cost=[]
dem=[]

for i in range(100):
    t = loss(k[:,i],X,y)
    cost.append(t)
    dem.append(i)

plt.plot(dem,cost)
#a = k[:,0]
#print(a)
#t=loss(a,X,y)
#print(t)

#print(y)
#print(data)
#print(cost)
