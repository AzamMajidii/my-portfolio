def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You cann't divide by zero.")
        return None


while True:
    try:
        num1 = float(input())
        num2 = float(input())
        r = divide(num1, num2)
        
        if  r is not None:
            print(r)
            break
        
    except ValueError:
        print("You can’t divide a string.")

    finally:
        print("برنامه با موفقیت اجرا شد!")
        
        

        
