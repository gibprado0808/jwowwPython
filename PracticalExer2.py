# greater than > | less than <

math = int(input("Enter Math grade: "))
science = int(input("Enter Science grade: "))
english = int(input("Enter English grade: "))

average = math + science + english
total_ave = average / 3

print(f"Your Average is {total_ave:.2f}.")

if total_ave >= 75:
    print("Congratulations!\nYou Passed the Semester")

else:
    print("You failed the Semester.")