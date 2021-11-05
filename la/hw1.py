# Import libraries
import matplotlib.pyplot as plt
import numpy as np
plt.grid('true','major','both',alpha=0.8)
plt.figure(figsize=(5, 5))
plt.xlim(-5,+5)
plt.ylim(-5,+5)
#fig, ax = plt.subplots()
plt.quiver(0, 0, 10, 20)
plt.show()