hoursSincePcr = int(input("How many hours passed since the last time you taken a PCR test? "))

if hoursSincePcr < 0:
    print("Invalid number of hours, please run the program and try again.")
elif hoursSincePcr > 48:
    print("You can only enter within 48 hours from a PCR test with a negative result.")
else:
    daysInAbuDhabi = int(input("How many days are you planning to stay in Abu Dhabi? "))
    if daysInAbuDhabi < 0:
        print("Invalid number of days, please run the program and try again.")
    elif daysInAbuDhabi > 3:
        print("Take a PCR test on ", end="day ")
        if daysInAbuDhabi >= 8:
            print(end="8")
        else:
            print(end="4")
        print(" of entry")
    else:
        print("No additional PCR test needed for staying 3 days or less.")
