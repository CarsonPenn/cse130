




# leapYearTest = userYear // 4


def lYear():
    userYear = input("What is the year?: ")
    while userYear != "":
        try:
            year = int(userYear)
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"{year} is a leap year.")
                lYear()
            else:
                print(f"{year} is not a leap year.")
                lYear()
        except ValueError:
            print("Please enter a valid year.")
            lYear()