def myfunc(*args):
	evens = []
	for item in args:
		if item%2 == 0:
			evens.append(item)
	return evens

nums = myfunc(1,2,3,4,5,6)

print(nums)


def myfunc(string):
	s = ''
	counter = 1
	for letter in string:
		if counter%2 != 0:
			s += letter.lower()
		else:
			s += letter.upper()
		counter += 1
	print(s)

word = myfunc('Robert')
print(word)