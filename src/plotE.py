# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import math

b = 1000000 #
N = math.pow(10,-12) # W
p = 0.5 # W
mu = 0.0001
E = 0.15 # J

d = np.array(range(100))
L = E*b/p*np.log2(1+p*mu/((np.power(d, 2))*N*b))

# Create the plot
plt.plot(L,d,label='d')

# Add a title
plt.title('Relationship between d and L')

# Add X and y Label
plt.xlabel('L')
plt.ylabel('d')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()


###########################################################################


