import numpy as np
import matplotlib.pyplot as plt 

def f(x):
	return x*(x-1)
funcation = f(1)
step_size = np.logspace(-14,-4,11)
der_save = np.zeros(len(step_size))

for i in range(len(step_size)):
	derivi = (f(1+ step_size[i]) + funcation)/ step_size[i]
	der_save[i] = derivi
	#print [step_size[i], der_save[i]]

plt.xlabel("Log scale number")
plt.ylabel("Derivitive value")
plt.title("Derivitive of x^2 + x at x= 1")
plt.ylim(0.9990,1.0002)
plt.plot(step_size,der_save)
plt.savefig("Q5.plot_1.pdf")
plt.show()
