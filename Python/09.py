n= int(input())
x= int(input())
for a in range(n):
    if x % 2 ==0:
        x = x // 2
    else:
        x= (x * 2) -1
print (x)