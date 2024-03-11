how_many = int(input("How many numbers do you want to type in? "))

sum = 0

for n in range(how_many):
    number = int(input(f"Number #{n+1}: "))
    sum += number


average = sum / how_many
print(f"Your average is: {average:.2f}")
