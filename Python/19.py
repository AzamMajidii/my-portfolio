def sum_numbers(*args):
    sum_num= 0
    for i in args:
        sum_num += i
    return sum_num

Total = map(int, input().split())
print(sum_numbers(*Total))