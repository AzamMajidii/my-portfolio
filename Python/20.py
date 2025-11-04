def pick_evens(*args):
    num= []
    for i in args:
        if i % 2 == 0:
            num.append(i)
    return num

Nums = map(int, input().split())
print(pick_evens(*Nums))