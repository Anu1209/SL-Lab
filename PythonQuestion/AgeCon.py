def AgeCover(num):
    num = num.split("-")
#     print(num)
    age = 2019 - int(num[2])
    if int(num[1])>10:
        age = age - 1
    print(age)
AgeCover("16-12-1998")
