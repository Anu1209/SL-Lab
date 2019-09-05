class Person:

	def __init__(self,name,age): #dis is the constructor of the class Person

		self.name = name;

		self.age = age;

p1 = Person("Suppandi",14)

p2 = Person("Ramu",12)

	
print("\n Name of person #1 is ",p1.name)

print("\n Age of the person #1 is ",p1.age)



print("\n Name of person #2 is ",p2.name)

print("\n Age of person #2 is ",p2.age)



p2.age = 10

print("Modified age of person #2 is ",p2.age)

