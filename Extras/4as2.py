def AgeConverter(a):
        b=int(a[:2])
        c=int(a[3])
        e=int(a[5:9])
        age=2019-e
        print(age)
a=input('enter the birthdate\n')
AgeConverter(a)        
