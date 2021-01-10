import min

def test_get_min():
	values = [1,2,3,4,5]
	assert min.get_min(values) == 1
def test_get_min2():
	values = [2,3,4,5]
	assert min.get_min(values)==2

