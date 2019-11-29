class person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		person.x+=1

p1=person("Suppandi",20)
p2=person("Raju",15)

print ("Name of first person is :", p1.name)
print ("Age of first person is :", p1.age)

print ("Name of secondt person is :", p2.name)
print ("Age of second person is :", p2.age)

p2.age=10
print("Changed age for second person is :",p2.age)
print("no of persons :",person.x)
