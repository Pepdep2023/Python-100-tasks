day = input("Enter day of the week: ")
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday":
    print("Weekday")
elif day == "Friday":
    print("TGIF")
elif day == "Saturday" or day == "Sunday":
    print("Weekends")
else:
    print("invalid input")
    