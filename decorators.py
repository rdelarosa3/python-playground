def func():
	return 1

print(func())
print(func)

greet = func()

print(greet)




def hello(name="jose"):
	print('hellow excuted')

	def greet():
		return '\t This is the greet() inside hello'

	def welcom():
		return '\t this iniside hello()'

	if name == 'jose':
		return greet
	else:
		return welcom

new_func = hello()


print(new_func)
print(new_func())


def cool():

	def super_cool():
		return "I am very cool"

	return super_cool

some_func = cool()

print(some_func())



def hello():
	return 'Hi Jose'



# pass func as argument
def other(something):
	print('othe code runs')
	print(something())

other(hello)




#### DECORATORS ####

def new_dec(original):

	def wrap_func():

		print('Some Extra code before')
		original()
		print('Some extra code after ')

	return wrap_func

def original():
	print("Decorate me")

decorator = new_dec(original)
print(decorator())


#### simplified decorator
@new_dec
def original():
	print("Decorate me")

print(original())


