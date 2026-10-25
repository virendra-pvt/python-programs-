age=int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

    if age >= 65:
        print("You are eligible for senior citizen benefits.")
    elif age >= 16:
        print("You are eligible for a learner's permit.")
    else:
        print("You are not eligible to drive")
         