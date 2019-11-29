def OddRange(num1,num2):
    odd = []
    for i in range(num1+1,num2):
        if i%2 != 0:
            odd.append(i)
    return odd

# taking the input and converting it to integer 
# input() takes the input
# int() converts it to integer

num1 = int(input())
num2 = int(input())
print(OddRange(num1,num2))
