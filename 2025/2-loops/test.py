####################

count = []

for i in range(0,100001):
    if i % 2 == 0:
        pass
    else:
        count.append(i)
        
print(sum(count))

####################

count = []
num = range(3,5000)

for i in num:
    if i % 35 == 0:
        pass
    elif i % 5 == 0:
        count.append(i)
    elif i % 7 == 0:
        count.append(i)

print(sum(count))

####################

li = [1,2,3,4,5]

for num in enumerate(li):
    print(num)

####################

num = list(range(1,30,3))

for i in num:
    print(i, end=' ')

####################

count = 3968
to_subtract = []

for i in range(1,16):
    if i % 3 != 0:
        to_subtract.append(i)
        
count = count - sum(to_subtract)
print(count)
    
####################