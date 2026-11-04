amount=900
tax=amount * 0.08

total_amount=amount + tax

print(total_amount)

if total_amount > 1000:
    discount=amount * 0.02
    total_amount -= discount
    print(f"Total amount with discount: {total_amount}")
else:
    print(f"Total amount: {total_amount}")