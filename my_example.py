import math

def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		if a < b:
			result = a
		else:
			result = b
	else:
		if a > b:
			result = a
		else:
			result = b
	return result

addition = 3 + 1.5 + 4

print(addition)


num = math.sqrt(25)

print(num)

s = 'hello'

print(s[1])
print(s[-1])

list1 = [0,0,0]

list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)

list4 = [5,3,4,6,1]

list4.sort()

print(list4)

d = {'simple_key':'hello'}

print(d['simple_key'])

d = {'k1':{'k2':'hello'}}

print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])

list5 = [1,2,2,33,4,4,11,22,3,3,2]

list5 = set(list5)

print(list5)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])