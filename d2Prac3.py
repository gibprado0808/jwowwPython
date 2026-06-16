years = int(input("Enter number of years: "))

office = (input("Enter office: "))

if office == 'IT'.lower() and years >= 10:
    print("Amount given: 10,000")
elif office == 'IT'.lower() and years <= 10:
    print("Amount given: 5000")

if office == 'ÁCCT'.lower() and years >= 10:
    print("Amount given: 12,000")
elif office == 'ÁCCT'.lower() and years <= 10:
    print("Amount given: 6000")

if office == 'HR'.lower() and years >= 10:
    print("Amount given: 15,000")
elif office == 'HR'.lower() and years <= 10:
    print("Amount given: 7500")

