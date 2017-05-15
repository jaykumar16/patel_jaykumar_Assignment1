import matplotlib.pyplot as plt 
import numpy as np

def factorial(n):
	y =1
	while n > 0:
		y = y * n
		n= n-1
	return y

n=2
k= 1
n_fac = factorial(n)
n_minus_k_fac = factorial(n-k)
k_fac = factorial(k)

binomial_the = n_fac / (n_minus_k_fac*k_fac)
print(binomial_the)

def binomial_coeff(n):
		result= []
	
		for k in range(n+1):
			n_fac = factorial(n)
			x = n-k
			n_minus_k_fac = factorial(x)
			k_fac = factorial(k)
			binomial_the = n_fac / (n_minus_k_fac*k_fac)
			result.append(binomial_the)
		return (result)

for n in range(20):
	print binomial_coeff(n)

def proba(n,k,p):

	n_fac = factorial(n)
	n_minus_k_fac = factorial(n-k)
	k_fac = factorial(k)
	binomial_the = n_fac / (n_minus_k_fac*k_fac)
	probability = binomial_the * (p**k) * (1-p)**(n-k)

	return probability
print proba(4,2,0.25)

# The number of 15/20 heads
# The probability is 0.75 
step = np.linspace(10,1000)
print len(step)
number_of_sum = []
num = []
for i in range(len(step)):
	count_in = []
	print i
	for n in range(i+1):
		#rand = np.random.rand(low=0, high=1, size=(10,))
		rand = np.random.rand(20)		
		count =  []
		print rand
		for k in range(len(rand)):
			if rand[k] >= 0.60:
				count.append(1)
				
			else:
				count.append(0)
		print len(count)
		#print np.sum(count)
		#print np.average(count)
		if np.average(count) >= 0.60:
			count_in.append(1)
		else: count_in.append(0)
	
	number_of_sum.append(np.sum(count_in)/step[i])	
	
		
	#num.append(np.average(number_of_sum[i]))

print len(step)
print len(number_of_sum)
plt.plot(step,number_of_sum,'o')
plt.show()
#cv = input("The Probability")
#for n in step:
#	pro = []
#	for N in range(n):
#		probabi=proba(n,N,cv)
#		pro.append(probabi)

#	print len(pro)
#	print len(range(n))
#	plt.plot(range(n),pro)
#	plt.ylabel('some numbers')
#	plt.show()


