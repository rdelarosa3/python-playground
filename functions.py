 # Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of(x,y):
	if x%2 == 0 and y%2 == 0:
		return min(x,y)
		# if x < y:
		# 	return x
		# else:
		# 	return y
	else:
		return max(x,y)
		# if x > y:
		# 	return x
		# else:
		# 	return y

print(lesser_of(2,4))
print(lesser_of(2,5))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(string):
	string = string.split()
	if len(string) == 2:
		return string[0][0] == string[1][0]
		# x = string[0]
		# y = string[1]

		# return x[0] == y[0] simplified

		# if x[0] == y[0]:
		# 	return True
		# else:
		# 	return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(x,y):
	if (x+y) == 20 or (x == 20 or y == 20):
		return True
	else:
		return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3)) 

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
	new_name = ''
	for index, value in enumerate(name):
		if index == 0 or index == 3:
			new_name += value.upper()
		else:
			new_name += value
	return new_name

print(old_macdonald('macdonald'))

def old_macdonald(name):
	new = list(name)
	new[0] = new[0].upper()
	new[3] = new[3].upper()
	return ''.join(new)

print(old_macdonald('macdonald'))

def old_macdonald(name):
	first = name[:3]
	second = name[3:]

	return first.capitalize() + second.capitalize()

print(old_macdonald('macdonald'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed¶
def master_yoda(string):
	return ' '.join(string.split()[::-1])


print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(num):
	return (num > 89 and num < 111) or ( num > 189 and num < 211)


	# return (abs(100-n)<=10) or (abs(200-n) <= 10

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(string):
	triple = ''
	for char in list(string):
		triple += char*3
	return triple

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(x,y,z):
	nums = [x,y,z]
	for num in nums:
		if num <= 11:
			if sum(nums) <= 21:
				return sum(nums)
			elif sum(nums) > 21 and (11 in nums):
				return sum(nums)-10 
			else:
				return 'BUST'
print(blackjack(5,6,7)) 
print(blackjack(9,9,9)) 
print(blackjack(9,9,11))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶
def summer_69(array):
	added = []
	for num in array:
		if num >= 6:
			if num > 9:
				added.append(num)
			else:
				continue
		else:
			added.append(num)
	return sum(added)

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(array):
	spy = []
	for num in array:
		if num == 0 or num == 7:
			spy.append(num)
	spy = ''.join(map(str,spy))
	return spy == '007'

	# spy [0,0,7,'x']
	# for num in array:
	# 	if num == code[0]:
	# 		code.pop(0)
	# return len(code) == 1



print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]) )

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number¶
def count_primes(number):
	nums = []
	for num in range(0,number+1):
		if num > 1:
			for i in range(2,num):
				if num%i == 0:
					break
			else:
				nums.append(num)
	return len(nums)

print(count_primes(100))