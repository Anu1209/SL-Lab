students = {'1MS17IS020':'Ahana','1MS17IS021':'Zain'}
list = ["value1","value2","value3"]

j = 0

for i in students:
    print("Key is ",i," and value is ",students[i])
    list[j] = students[i]
    j = j+1

print(list)
print(students.keys)
print(students.values())
