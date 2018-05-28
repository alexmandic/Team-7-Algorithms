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
    
xLen = 100
yLen = 100
numNods = 15
minValue = 10
maxValue = 40

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
    weiVals.append(round((rng.random()*(maxValue-minValue))+minValue,2))
    
#randomly generated nodes assumed to be in decreasing value order
weiVals.sort()    
weiVals.reverse()
    
nodLocs = []
for j in range(numNods):
    nodLocs.append([nodLocsX[j],nodLocsY[j]])

gameOn = 1

plt.axis([0.0,xLen, 0.0,yLen])
ax = plt.gca()
ax.set_autoscale_on(False)
plt.plot(nodLocsX,nodLocsY,'ko',defLoc[0],defLoc[1],'bx',attLoc[0],attLoc[1],'rx')
plt.show()

while gameOn:
    defDis = []
    attDis = []

    for k in range(numNods):
        newDefDis = abs(defLoc[0]-nodLocsX[k])+abs(defLoc[1]-nodLocsY[k])
        newAttDis = abs(attLoc[0]-nodLocsX[k])+abs(attLoc[1]-nodLocsY[k])
        
        if newDefDis != 0:
            defDis.append(newDefDis)
        else:
            defDis.append(1)

        if newAttDis != 0:
            attDis.append(newAttDis)
        else:
            attDis.append(1)        
        
    attK = k_finder(attDis,weiVals) 
    defK = k_finder(defDis,weiVals)
    
    attP = attac_probs(attK,attDis,weiVals)
    attP = attP/np.sum(attP)
    attNew = np.random.choice(nodNames[0:attK], p=attP)

    if attLoc[0] > nodLocsX[attNew]:
        attLoc[0] -= 1
    elif attLoc[0] < nodLocsX[attNew]:
        attLoc[0] += 1
        
    if attLoc[1] > nodLocsY[attNew]:
        attLoc[1] -= 1
    elif attLoc[1] < nodLocsY[attNew]:
        attLoc[1] += 1        
    
    defP = defen_probs(defK,defDis,weiVals)
    defP = defP/np.sum(defP)
    defNew = np.random.choice(nodNames[0:defK], p=defP)
    
    if defLoc[0] > nodLocsX[defNew]:
        defLoc[0] -= 1
    elif defLoc[0] < nodLocsX[defNew]:
        defLoc[0] += 1
        
    if defLoc[1] > nodLocsY[defNew]:
        defLoc[1] -= 1
    elif defLoc[1] < nodLocsY[defNew]:
        defLoc[1] += 1        
        
    if attLoc[0] == defLoc[0] and attLoc[1] == defLoc[1]:
        gameOn = 0
    
    if attLoc[0] == nodLocsX[attNew] and attLoc[1] == nodLocsY[attNew] and gameOn == 1:
            numNods -= 1
            nodNames.pop()
            nodLocsX.pop(attNew)
            nodLocsY.pop(attNew)
            nodLocs.pop(attNew)  
    
    plt.axis([0.0,xLen, 0.0,yLen])
    ax = plt.gca()
    ax.set_autoscale_on(False)
    plt.plot(nodLocsX,nodLocsY,'ko',defLoc[0],defLoc[1],'bx',attLoc[0],attLoc[1],'rx')
    plt.show()