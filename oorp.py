class Dog():
	#class object attributes
	#same for any instance of a class
	species = "mammal"
	def __init__(self,breed,name):
		#expect to be string
		self.breed = breed
		self.name = name

	# Actions --- methods
	def bark(self):
		print('Woof! My name is {}'.format(self.name))
		print(f'Woof! My name is {self.name}')


my_dog = Dog('Lab','Spot')

my_dog.bark()


class Circle():

	#class attribute
	pi = 3.14

	def __init__(self, radius=1):

		self.radius = radius
		self.area = radius*radius*self.pi

	#method

	def get_circ(self):
		return self.radius * self.pi * 2


my_circle = Circle()

print(my_circle.get_circ())



####. inheritance
class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
    	#inherit from animal class
        Animal.__init__(self)
        print("Dog created")
     #overwrites Animal class method
    def whoAmI(self):
        print("Dog")
    #dog class original method
    def bark(self):
        print("Woof!")


#polymorphism
class Dog():

	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says Woof!"

class Cat():

	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says Meow!"



niko = Dog('Niko')
felix = Cat("Felix")

print(felix.speak())
print(niko.speak())


for pet in [niko,felix]:
	print(type(pet))
	print(type(pet.speak))


def pet_speak(pet):
	print(pet.speak())

pet_speak(felix)
pet_speak(niko)




#abstract

class Animal():

	def __init__(self,name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Sublclass must implement this abstract method")

myanimal = Animal('fred')

# myanimal.speak()


class Dog(Animal):

	def speak(self):
		return self.name+ " says woof!"

pet = Dog('odie')

pet.speak()




###### SPECIAL METHODS

mylist = [1,2,3]
len(mylist)

class Sample():
	pass

mysample = Sample()

print(mysample)



class Book():

	def __init__(self,title,author,pages):
		self.title = title
		self.author = author
		self.pages = pages

	#creates a string representation of self when called to print 
	def __str__(self):
		return f"{self.title} by {self.author}"

	def __len__(self):
		return self.pages

	def __del__(self):
		print("A book object has been deleted")


b = Book('python','jose',200)
print(len(b))
print(b)


