PA = int(input())
if PA > 50000:
    discount = 0.20
elif PA >= 20000 <= PA <=50000:
    discount = 0.10
elif PA < 20000:
    discount = 0.0

Final_amount= PA - (PA * discount)

print(f"{Final_amount:.0f}")