temps=[28,30,27,29,31,26,32]
print("list: ",temps)
import numpy as np
temp =np.array(temps)
print("np array: ",temp)
print("Temperature data:", temp)
print("Number of dimensions:", temp.ndim)
print("Maximum temperature:", np.max(temp))
print("Minimum temperature:", np.min(temp))
print("Mean temperature:", np.mean(temp))
print("Variance:", np.var(temp))
print("Standard Deviation:", np.std(temp))
