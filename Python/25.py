import time

def time_of_fun(f):
    def wrapper(*args, **kwargs):
        s_time = time.time()
        r = f(*args,**kwargs)
        e_time = time.time()
        print(f"Time: {e_time - s_time:.6f}")
        return r
    return wrapper

@time_of_fun
def my_list(n):
    ls = [i for i in range(1, n+1)]
    return ls
    
n = int(input())
result = my_list(n)
print(result)


        