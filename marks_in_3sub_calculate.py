maths= ("Enter Your maths marks: " )   
chemistry= ("Enter Your chemistry marks: ")
physics= ("Enter Your physics marks: ")
english= ("Enter Your english marks: ")
computer= ("Enter Your computer marks: ")
total_marks = int(input(maths)) + int(input(chemistry)) + int(input(physics)) + int(input(english)) + int(input(computer))
percentage = (total_marks / 500) * 100

print("The total marks obtained in all subjects is:", total_marks)
print("The percentage obtained is:", percentage)
