def add(n1,n2):
	print(n1+n2)

add(10,20)

num1 = 10
# num2 = input("Enter number: ")
num2 = 10

try:
	#attempt code
	#may have error
	result = add(num1,num2)
except:
	print("Hey it looks like you arent adding correctly")
else:
	print('Add went well')
	print(result)


try:
	f = open('testfile','w')
	f.write('Write a test line')
except TypeError:
	print("There was a type error")
except OSError:
	print('You have an IO error')
finally:
	print('I always run')



def ask_int():

	while True:
		try:
			result = int(input("Please provide number: "))
		except:
			print("that is not a number")
			continue
		else:
			print("thank you")
			break
		finally:
			print("Try again")

ask_int()