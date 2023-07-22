length=int(input('enter length'))
count=1
for i in range(0,length+1):
    for j in range(0,i+1):
        print(count,end=" ")
        count+=1
    print('')
