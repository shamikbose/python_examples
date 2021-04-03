#This is a tutorial about using decorators in Python
def f1(func):
	def wrapper(*args, **kwargs):
		print("Before function call")
		val=func(*args, **kwargs)
		print("After function call")
		return val

	return wrapper

@f1
def f(s: str):
	print(s)

@f1
def add(x,y):
	return x+y

print(add(3,9))