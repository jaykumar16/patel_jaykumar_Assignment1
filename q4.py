import numpy as np
import matplotlib.pyplot as plt 
N = 200
x = np.linspace(-2,2,N)
y = np.linspace(-2,2,N)
#Z_st = np.zeros(N)
z_store = np.zeros((N,N))
for z in range(len(x)):
	x_tem = x[z]
	
	for k in range(len(y)):
		y_tem = y[k]
		
		c = x_tem + y_tem*1j
		Z = 0
		for i in range(N+1):
			Z = Z**2 + c
			Z_abs = np.absolute(Z) 
			
		if np.isnan(Z_abs):			
			z_store[k,z] = 1

		else:
			z_store[k,z] = 0
	


plt.imshow(z_store)
plt.colorbar()
plt.xlabel("Real number")
plt.ylabel("Imaginary number")
plt.title("Diverging vs convering of the complex number")
plt.savefig("Q4.plot_1.pdf")
plt.show()
