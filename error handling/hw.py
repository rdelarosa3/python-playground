for i in ['a','b','c']:
    try:
    	print(i**2)
    except TypeError:
    	print("This is not an integer")
    finally:
    	print("Provide an Intger")

x = 5
y = 0
try:
	z = x/y
except ZeroDivisionError:
	print('Number is not divisible by 0')
finally:
	print('Provide a number greater than 0')


def ask():
	while True:
		try:
			num = int(input("Please provide number: "))
			result = num**2
		except:
			print("that is not a number")
			continue
		else:
			print(result)
			break
ask()