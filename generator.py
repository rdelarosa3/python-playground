### stores in memory
def create_cubes(n):
	result = []
	for x in range(n):
		result.append(x**3)

	return result

for x in create_cubes(10):
	print(x)


### generate values as you need them
def create_cubes(n):
	for x in range(n):
		yield (x**3)


for x in create_cubes(10):
	print(x)




### stores in memory
def gen_fib(n):

	a = 1
	b = 1
	output = []
	for i in range(n):
		output.append(a)
		a,b = b,a+b
	return output

for num in gen_fib(10):
	print(num)

### generate values as you need them
def gen_fib(n):

	a = 1
	b = 1

	for i in range(n):
		yield a
		a,b = b,a+b

for num in gen_fib(10):
	print(num)




def simple():
	for x in range(3):
		yield x

g = simple()

print(next(g))
print(next(g))
print(next(g))
# print(next(g))



####### itererators ####

s = 'hello'

for letter in s:
	print(letter)

s_iter = iter(s)
print(s_iter)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))