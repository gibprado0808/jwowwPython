hours = int(input("Enter number of hours: "))
rate = int(input("Enter rate per hour: "))
gsis = int(input("GSIS Premium: "))
philhealth = int(input("Enter Philhealth: "))
house_loan = int(input("Enter Housing Loan: "))
total_hours = hours * rate
tax_rate = .25 * total_hours
total_deductions = gsis + philhealth + house_loan + tax_rate

print(f"Your Gross Salary is ${total_hours: }.")
print(f"Your Total Deduction is ${total_deductions:.1f}.")
print(f"Your Net Salary is ${total_hours - total_deductions:.1f}.")
