#Temperature conversion
def fhr(Fahr):
	
		Celsius = (Fahr - 32) * 5.0/9.0
		print "Temperature:", Fahr, "Fahrenheit = ", Celsius, " C"

def cls(Cel):
		Fahrenite = (Cel*9/5) + 32		
		print "Temperature:", Cel, "Fahrenheit = ", Fahrenite, " F"

print('Enter 1 for F->C \nEnter 2 for C->F \n Enter 3 for exit')
n=int(input())
while(1):
	if(n==1):
		Fahr = int(raw_input("Enter a temperature in Fahrenheit:"))
		print fhr(Fahr)
	elif(n==2):
		Cel=int(raw_input("Enter the temperature in Celsius"))
		print cls(Cel)
	else:
		sys.exit()

