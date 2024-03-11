merc_val = float(input("Type in the goods value: "))
merc_disc = int(input("Type in the goods discount: "))

discount = merc_disc / 100

print(f"Discount: {discount}%")
print(f"Discount (Money): {(merc_val - merc_val*discount):.2f}")
print(f"The goods with the updated value is: {(merc_val*discount):.2f}")
