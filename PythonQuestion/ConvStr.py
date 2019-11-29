def ConvertString(st):
    st = list(st)
    
    for i in range(0,len(st)):
        if st[i].isalpha():
            if st[i] == 'Z':
                st[i] = 'a'
            else:
                st[i] = (chr(ord(st[i]) + 1))
#     print(st)
    for i in range(0,len(st)):
        if st[i] in ['a','e','i','o','u']:
            st[i] = st[i].upper()
    print("".join(st))
ConvertString("hello*3")
