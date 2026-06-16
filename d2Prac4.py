ask = "Y"
while ask == 'y'.lower():

    numba1 = int(input("Enter first number:"))
    numba2 = int(input("Enter second number:"))
    sum = numba1 + numba2

    if sum % 2 == 0:
        print(f"The sum of two integers is Even")
    else:
        print(f"The sum of two integers is Odd")





