
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
#np.random.seed(10)
data = (38,38,39,39,40,40,41,42,45,47,48,49,49,50,51,51,53,53,61,61,63,63,65,65,70,72,73,74,75,76,76,78,78,80,80,83,85,92,98)
 
fig = plt.figure(figsize =(100, 10))
 
# Creating plot
plt.boxplot(data, vert = false, )
 
# show plot
plt.show()