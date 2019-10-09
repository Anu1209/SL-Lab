def oddrange(a,b):
        list=[]             
        while(a<=b):
                if(a%2==0):
                        a=a+1
                        list.append(a)
                else:
                        list.append(a)
                        a=a+2
        print(list)                
a=int(input())    
b=int(input()) 
oddrange(a,b)
