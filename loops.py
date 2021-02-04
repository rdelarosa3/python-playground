from random import shuffle
###### for loops #####

#lists
mylist = [1,2,3,4,5,6,7,8,9,10]

for jelly in mylist:
	if jelly%2 == 0:
		print(f'Even Number: {jelly}')
	else:
		print(f'Odd Number: {jelly}')
list_sum = 0 

for num in mylist:
	list_sum = list_sum + num 

print(list_sum)

#string iteration

mystring = "hello world"

for char in mystring:
	print(char)

#tuple unpacking

mylist = [(1,2),(3,4),(5,6),(7,8)]

print(len(mylist))

for a,b in mylist:
	print(a)
	print(b)


#dictionaries

d = {'k1':1, 'k2':2, 'k3':3}

#keys
for item in d:
	print(item)

#items

#tuple pairs
for item in d.items():
	print(item)

#tuple values
for key,value in d.items():
	print(value)
#only values
for value in d.values():
	print(value)


####### while loops #########

x = 0

while x < 5:
	print(f'The current value of x is {x}')
	x += 1
else:
	print("X is not less than 5")


## BREAK CONTINUE PASS ###
x = [1,2,3]
for item in x:
	pass #can use as place holder to build out functions later

mystring = "sammy"
for char in mystring:
	if char == 'a': 
		continue #go back to loop kind of like ignore
	print(char)

x = 5

while x > 0:
	if x == 2:
		break #exits loop when condition is true
	print(x)
	x -= 1

### loop operators generators #######


## range()
mylist = [1,2,3]

for num in range(10):
	print(num)

for num in range(3,10):
	print(num)

for num in range(0,10,2):#steps 
	print(num)


##enumerate
index_count = 0
word = 'abcde'
for char in word:
	#print("at index {} the letter is {}".format(index_count,char))
	print(word[index_count])
	index_count += 1

for item in enumerate(word):
	print(item)

for index,char in enumerate(word):
	print(index)
	print(char)


## ZIP

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1,mylist2):
	print(item)
print(list(zip(mylist1,mylist2)))


## IN

print('x' in ['x','y','z'])

d = {'mykeys':345}

print('mykeys' in d.keys())
print(345 in d.values())

mylist = [1,2,3,4,5]
randomlist = shuffle(mylist)
print(randomlist)

#input("what is your name:")



###### list comprehension
mystring = "hello"
mylist = []

for letter in mystring:
	mylist.append(letter)

mylist = [letter for letter in mystring]

print(mylist)

newlist = [num for num in range(0,11)]
print(newlist)
newlist = [num**2 for num in range(0,11)]
print(newlist)

newlist = [x for x in range(0,11) if x%2==0]
print(newlist)

celcius = [0,10,20,34.5]

fahrenheit = [( (9/5)*temp +32) for temp in celcius]
print(fahrenheit)

fahrenheit = []
for temp in celcius:
	fahrenheit.append((9/5*temp +32))
print(fahrenheit)


# nested loop
mylist = []

for x in [2,4,6]:
	for y in [1,10,1000]:
		mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)
