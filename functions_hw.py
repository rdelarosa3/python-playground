# Write a function that computes the volume of a sphere given its radius.

def vsphere(r):
	print((4/3)*3.14*(r**3))

vsphere(2)

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def check(num,x,y):
	if num in range(x,y):
		print(True)
	else:
		print(False)

(check(6,5,10))

def check(num,x,y):
	return num in range(x,y)

print(check(6,5,10))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: .isupper() and .islower()

def up_low(s):
	up = []
	low = []
	for char in s:
		if char.islower():
			low.append(char)
		elif char.isupper():
			up.append(char)
	print(f'No. of Upper case: {len(up)}')
	print(f'No. of Lower case: {len(low)}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24


def mult(nums):
	total = 1
	for num in nums:
		total *= num
	print(total)

mult([1, 2, 3, -4])


# Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses 

def pali(s):
	if s == s[::-1]:
		print(True)
pali('lol')

def pali(s):
	return s == s[::-1]
print(pali('lol'))


# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
from string import ascii_lowercase

def ispan(s):
	count = 0
	for char in ascii_lowercase:
		if char in s:
			count += 1
	if len(ascii_lowercase) == count:
		print(True)
	else:
		print(False)

ispan(("The quick brown fox jumps over the lazy dog"))

def ispan(s):
	count = 0
	for char in ascii_lowercase:
		if char in s.lower():
			count += 1
	return len(ascii_lowercase) == count

print(ispan(("The quick brown fox jumps over the lazy dog")))
