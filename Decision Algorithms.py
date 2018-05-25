import numpy as np

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

def attac_probs(k, distances, values):    
    nes_sum = 0
    for j in range(k):
        nes_sum += (1/(distances[j]*values[j]))
        
    probabilities = []
    for l in range(k):
        probabilities.append(round((1/nes_sum/(distances[l]*values[l])),6))

    return probabilities

def k_finder(distances, values):
    k = len(distances)

    for i in range(k):
        test = 0
        for j in range(i):
            test += (values[j]-values[i])/(distances[j]*values[j])
        if(test >= 1):
            return i
    
    return k

###############################################################################
    
max_length = 10

node_order_D = [9,10,11]

vals_temp_D = [1250,1400,1300]
dif_D = [3,3,2]
vals_D = []
for l in range(len(vals_temp_D)):
    vals_D.append(vals_temp_D[l]/dif_D[l]) 

dist_temp_D = [2,1,4.123]
dist_D = []
for h in range(len(dist_temp_D)):
    dist_D.append(dist_temp_D[h]/max_length)    
    
vals_D, dist_D, node_order_D = (list(t) for t in zip(*sorted(zip(vals_D, dist_D, node_order_D))))
vals_D.reverse()
dist_D.reverse()
node_order_D.reverse()

k_val_D = k_finder(dist_D,vals_D)
    
print(defen_probs(k_val_D,dist_D,vals_D))
print(node_order_D[0:k_val_D])
p = defen_probs(k_val_D,dist_D,vals_D)
p = p/np.sum(p)
print(np.random.choice(node_order_D[0:k_val_D], p=p))

###############################################################################

node_order_A = [1,2,3,4,5]

vals_temp_A = [2000,3500,6000,10000,8000]
dif_A = [5,7,10,16,14]
vals_A = []
for l in range(len(vals_temp_A)):
    vals_A.append(vals_temp_A[l]/dif_A[l]) 

dist_temp_A = [5.472,5,2.414,3,1]
dist_A = []
for h in range(len(dist_temp_A)):
    dist_A.append(dist_temp_A[h]/max_length)  
    
vals_A, dist_A, node_order_A = (list(t) for t in zip(*sorted(zip(vals_A, dist_A, node_order_A))))
vals_A.reverse()
dist_A.reverse()
node_order_A.reverse()

k_val_A = k_finder(dist_A,vals_A)

print(attac_probs(k_val_A,dist_A,vals_A))
print(node_order_A[0:k_val_A])
p = attac_probs(k_val_A,dist_A,vals_A)
p = p/np.sum(p)
print(np.random.choice(node_order_A[0:k_val_A], p=p))