#counting the occcurence of each word in test
from collections import Counter #collection is a library and Counter is being called
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
		

print("Number of words in a file:",word_count("test.txt"))

