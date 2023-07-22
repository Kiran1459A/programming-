num=int(input('enter a number:'))
first,sec,nxtnum=0,1,0
print(first)
print(sec)
for i in range(2,num+1):
    nxtnum=first+sec
    print(nxtnum)
    first=sec
    sec=nxtnum
    
