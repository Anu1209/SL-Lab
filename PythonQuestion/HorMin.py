def HourMinute(num):
    mn = num%60
    
    hr = int(num/60)
    print(hr,":",mn)
    
HourMinute(54)
