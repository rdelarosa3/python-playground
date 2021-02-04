mylist = [1,2,3]
mylist.append(4)
print(mylist)
mylist



def name_function():
	print('hello')

def say_hello(name):
	print('Hello ' + name)
say_hello('Robert')

def dog_check(s):
	return 'dog' in s.lower()

dog_check("My dog ran away")

def pig_latin(word):
	first_letter = word[0]

	#check if vowel
	if first_letter in 'aeiou':
		pig_word = word + 'ay'
	else:
		pig_word = word[1:]	+ first_letter + 'ay'
	return pig_word
print(pig_latin('apple'))