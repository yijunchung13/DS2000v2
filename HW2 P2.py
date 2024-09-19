
digits = [4, 5, 3, 2, 0, 1, 5, 1, 1, 2, 8, 3, 0, 3, 6, 6]


for i in range(len(digits)):
    if i % 2 == 0:  
        digits[i] *= 2


for i in range(len(digits)):
    if digits[i] > 9:
        digits[i] -= 9


total_sum = 0
for digit in digits:
    total_sum += digit


if total_sum % 10 == 0:
    print("This is a valid number.")
else:
    print("This is not a valid number.")


print("Modified list of digits:", digits)
print("Total sum:", total_sum)
