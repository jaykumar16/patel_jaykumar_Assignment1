import scipy.special as special
import scipy.integrate as integrate 
#import scipy.special.cython_special as csc
import numpy as np
import matplotlib.pyplot as plt 
import PIL as image

x = np.linspace(0, np.pi*4, 500)
for n in range(0,6):
	plt.plot(x, special.jv(n, x), label = '$Bessal: %i$' % n)
	

results = integrate.quad(lambda x: special.jv(0,x),0,np.pi)
print(results)
plt.legend()
plt.xlabel("Number X")
plt.ylabel("B(x) Values")
plt.title("Bessel funcation")
plt.savefig("Q3.plot_1.pdf")
plt.show()

#def Id(R,a,q,lamda, I_0):
z = np.linspace(-5,5,1000)
y = np.linspace(-5,5,1000)
xv, yv = np.meshgrid(z,y)
q = np.sqrt(xv**2 + yv**2)
print q[0:,0:]
print len(xv)
print np.shape(q)
def Id(q,a,R,lamda):
	return ((np.pi *2 *a*q)/(lamda*R))
I_0 = 100
I  = I_0 * ((2* special.jv(1,Id(q,1,1,650)))/(Id(q,1,1,650)))**2
#np.shape(I)
plt.imshow(I)
plt.title("function values")
plt.colorbar()
#plt.legend("B:1","B:2","B:3","B:4","B:5","B:6""
plt.xlabel("Appature")
plt.ylabel("Intensity")
plt.title("Intensity graph")
plt.savefig("Q3.plot_2.pdf")
plt.show()



