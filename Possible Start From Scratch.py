import random as rng
import matplotlib.pyplot as plt
import numpy as np

###############################################################################

#Determines the value of k (and the number of points with non-zero probability)
def k_finder(distances, values):
    k = len(distances)

    for i in range(k):
        test = 0
        for j in range(i):
            test += (values[j]-values[i])/(distances[j]*values[j])
        if(test >= 1):
            return i
    
    return k

#Returns the probabilities for the defender
def defen_probs(k, distances, values):
    nes_sum = 0
    for j in range(k):
        nes_sum += (1/(distances[j]*values[j]))
    
    probabilities = []    
    for l in range(k):
        nes_sum2 = 0
        for m in range(k):
            nes_sum2 += (values[m]-values[l])/distances[m]/values[m]
        probabilities.append(round((((1/(distances[l]*values[l]))/nes_sum)*(1-nes_sum2)),6))
    
    return probabilities

#Returns the probabilities for the attacker
def attac_probs(k, distances, values):    
    nes_sum = 0
    for j in range(k):
        nes_sum += (1/(distances[j]*values[j]))
        
    probabilities = []
    for l in range(k):
        probabilities.append(round((1/nes_sum/(distances[l]*values[l])),6))

    return probabilities

###############################################################################
    
xLen = 10
yLen = 10
numNods = 4

defLoc = [rng.randint(0,xLen),rng.randint(0,yLen)]
attLoc = [rng.randint(0,xLen),rng.randint(0,yLen)]
nodNames = []
nodLocsX = []
nodLocsY = []
weiVals = []

for i in range(numNods):
    nodLocsX.append(rng.randint(0,xLen))
    nodLocsY.append(rng.randint(0,yLen))
    nodNames.append(i)
    weiVals.append(round((rng.random()*80)+20,2))
    
#randomly generated nodes assumed to be in decreasing value order
weiVals.sort()    
weiVals.reverse()
    
nodLocs = []
for j in range(numNods):
    nodLocs.append([nodLocsX[j],nodLocsY[j]])

while 1:
    plt.plot(defLoc[0],defLoc[1],'bo',attLoc[0],attLoc[1],'ro',nodLocsX,nodLocsY,'ko')

    defDis = []
    attDis = []

    for k in range(numNods):
        defDis.append(abs(defLoc[0]-nodLocsX[k])+abs(defLoc[1]-nodLocsY[k]))
        attDis.append(abs(attLoc[0]-nodLocsX[k])+abs(attLoc[1]-nodLocsY[k]))
        
    attK = k_finder(defDis,weiVals) 
    defK = k_finder(defDis,weiVals)
    
    attP = attac_probs(attK,attDis,weiVals)
    attP = attP/np.sum(attP)
    attNew = np.random.choice(nodNames[0:attK], p=attP)
    attLoc[0] = nodLocsX[attNew]
    attLoc[1] = nodLocsY[attNew]
    #CURRENT PROBLEM IS THAT ONCE YOU'RE IN THE SAME PLACE AS A NODE, YOU ARE DIVIDING BY A DISTANCE OF 0
    #NEED TO ADD IN SIMILAR LINES FOR DEF ONCE ATT IS WORKING