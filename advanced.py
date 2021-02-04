#ADVANCED NUMBERS

print(hex(12))

print(bin(1234))

# to the power
2**4
print(pow(2,4))

# modulo of power
print(pow(2,4,3))


# absolute
print(abs(-3))

#rountding

print(round(2))

print(round(2.7))

print(round(3.141592,2))

#ADVANCED STRINGS
s= "hello"
s.capitalize()

print(s.upper())

print(s.lower())

print(s.count('l'))

print(s.find('l'))

print(s.center(20,'z'))

print('hello\thi')

'hello\t'.expandtabs()

s.isalnum()

s.isalpha()

s.istitle()

s.isupper()

s.endswith('o')

print(s.split('l'))

#### ADVANCED SETS ##########

s = set()

s.add(1)
s.add(2)
print(s)

s.clear()

print(s)
s.add(1)
s.add(2)

sc = s.copy()
sc.add(3)
print(sc)

#### ADVANCED LISTS ########
l = [1,2,3]
l.append(4)
print(l.count(10))
print(l.count(1))

l.append([4,5])
print(l)

l.extend([4,5])
print(l)
print(l.index(3))
print(l.index(5))

l.insert(2, "insert")

print(l)

l.remove('insert')
print(l)

l.remove([4,5])
l.sort()
print(l)


##### ADVANCED DICTIONARIES


d = {'k1':1, 'k2':2}
print(d['k1'])

d = {x:x**2 for x in range(10)}
print(d)

d = {k:v**2 for k,v in zip(['a','b'], range(10))}

# d.viewvalues()
# d.viewkeys()
print(d)