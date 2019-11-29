def AtomicDictionary():
	atoms={
		'H':'Hydrogen',

		'He':'Helium',

		'Li':'Lithium',

		'B':'Boron',

		'C':'Carbon',

  	'N':'Nitrogen'
	}

	print(atoms.items())
	print("Enter unique and duplicate element to the dictionary")
	print("Atomic Symbol:")
	x=input()
	print("Atomic Name:")
	y=input()
	atoms[x]=y
	print(atoms.items())
	print("Length of the dictionary is",len(atoms))
	print("Enter a key to search")
	z=input()
	print(atoms[z])
AtomicDictionary()
