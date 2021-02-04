x = 25

def printer():
	x=50
	return x

printer()

name = "Global"

def greet():
	# name = 'Sammy'

	def hello():
		name = 'Local'
		print('Hello ' + name)

	hello()

greet()

x = 50

def func():
	global x # will allow manipulation of global variable
	print(f"{x}")



func()