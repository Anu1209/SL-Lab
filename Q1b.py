#x is interrator
S=[x**2 for x in range(10)]
M=[x for x in S if x%2==0]
print(M)
M.reverse()
print(S)
print(M)
