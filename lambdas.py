##### MAP FUNCTION EXAMPLES
# iterates funtion through each.
def square(num):
	return num**2

my_nums = [1,2,3,4,5]

# iterate through and print 
for item in map(square,my_nums):
	print(item)


# print out a list of numers
list(map(square,my_nums))	


def splicer(mystring):
	if len(mystring)%2 == 0:
		return "EVEN"
	else:
		return mystring[0]


names = ['Andy','Eve','Sally']

list(map(splicer,names))

###### FILTER FUNCTION EXAMPLES
# * filter only puts conditions that are true into an array
def check_even(num):
	return num%2 == 0

mynums = [1,2,3,4,5,6]

list(filter(check_even, mynums))

for n in filter(check_even,mynums):
	print(n)


# what are lambdas

def square(num):
	result = num**2
	return result

# turned to lambdas

# simiplified
def square(num):
	return num ** 2

# named lambda
square = lambda num: num ** 2

# true lambda
list(map(lambda num:num**2,my_nums))




