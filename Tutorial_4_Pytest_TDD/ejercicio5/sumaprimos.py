import primes

def sumaprimes(lista):
	contador=0
	for i in lista:
		if(primes.is_prime(i)):
			print(i)
			contador+=i
	return contador

print(sumaprimes([1,2,3,4,5,6,7,8,9,10]))


