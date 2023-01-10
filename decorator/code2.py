# code for testing decorator chaining
def decor1(func1):
	def inner():
		x = func1()
		return x * x
	return inner

def decor(func2):
	def inner():
		x = func2()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 5

print(num())

#decor1(decor(num)) calling is similar to this