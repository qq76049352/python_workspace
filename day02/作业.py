
count = 1
while count<=10:
    print(count)
    count+=1

count = 1
sum = 0
while count<=100:
    sum +=count
    count+=1
else:
    print(sum)

count = 1
sum = 0
while count<=100:
    if count%2==0:
        sum -= count
    else:
        sum += count
    count+=1
else:
    print(sum)
