st = 'Print only the words that start with s in this sentence'
st = st.split()
for word in st:
	if word[0] == 's':
		print(word)

nums = range(0,11,1)
for num in nums:
	if num%2 == 0:
		print(num)
nums = [num for num in range(1,51) if num%3==0]
print(nums)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
	if len(word)%2 == 0:
		print(word)
 
for num in range(1,101):
	if num%3 == 0 and num%5 == 0:
		print('FizzBuzz')
	elif num%3 == 0:
		print('Fizz')
	elif num%5 == 0:
		print('Buzz')
	else:
		print(num)
st = 'Create a list of the first letters of every word in this string'
st = [word[0] for word in st.split(' ')]
print(st)