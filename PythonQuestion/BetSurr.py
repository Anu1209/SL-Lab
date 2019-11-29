def betterSurround(st):
    st = list(st)
    
    if st[0]!= '+' and st[len(st)-1]!= '=':
        return False
    else:
        for i in range(0,len(st)):
            if st[i].isalpha():
                if not (st[i-1]=='+' or st[i-1]=='=') and (st[i+1] == '+' or st[i+1] == '='):
                    return false
            else:
                if i!=0 and i!= len(st)-1:
                    if st[i-1].isalpha() and st[i+1].isalpha():
                        return False
    return True

new = betterSurround("+f=+d+")
if new:
    print("y")
else:
    print("N")
