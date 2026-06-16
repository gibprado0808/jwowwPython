

math = int(input("Enter Math grade: "))
science = int(input("Enter Science grade: "))
english = int(input("Enter English grade: "))

grade = math < 75, science < 75, english < 75

average = math + science + english
total_ave = average / 3



print(f"Your Average is {total_ave:.2f}.")

if total_ave >= 75:
    print("Congratulations!\nYou Passed the Semester")

if grade < 75:
    print(f"You have to retake {grade}")

else:
     print("You failed the Semester.")