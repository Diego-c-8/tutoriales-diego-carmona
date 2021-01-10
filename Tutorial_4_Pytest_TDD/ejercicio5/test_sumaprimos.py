import primes
import sumaprimos
def test_suma_prime():
	value = [1,2,3,4,5,6,7,8,9,10]

	assert sumaprimos.sumaprimes(value) == 12

def test_suma_prime2():
	value = [1,2,3,4,5,6,7,8,9,10]

	assert sumaprimos.sumaprimes(value) == 17