marks=int(input("Enter your marks: "))

if marks > 100:
    print("Grade: invalid marks")
elif 100 >= marks >= 80:
    print("Grade: A")
elif 80 > marks >= 60:
    print("Grade: B")
elif 60 > marks >= 34:
    print("Grade: C")
else:
    print("fail")
