def skyline(*args):
    height= 0
    for i in args:
        height = max(height,i)
    return height

Nums = map(int, input().split())
print(skyline(*Nums))