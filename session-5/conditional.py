marks = 50
another_marks = 30

if another_marks >= 40:
   print("Student has passed")
else:
   print("Student has failed")





temprature = 30

if temprature >= 25:
 print("It is hot outside")
else: 
  print("It is cool outside")


age = 16

if age >= 18 :
  print("Adult")
else:
  print(" not adult")


score = 76
# score >= 90 Print A
# if score >= 75 Print B
# else print C
#else print D

if score >= 90: # score = 92 >= 90 : False
  print("Grade A")
elif score >= 75:
  print("Grade B")
elif score >= 45:
  print("Grade c")
else:
  print("Student failed")


# Self practice :

marks = 94
name = input("Enter your name :")
Enrollment_number = input("Enter your enrollment number :")
if marks >= 90:
  print(f"{name} with {Enrollment_number} is topper")
elif marks >= 55:
  print(f"{name} has conditionally passed")
else:
  print(f"{name} Failed in his exam.")



 #----------------------------------------------------------------------------------------

amount = 100
discount = 100
# amount > 1100, then apply a discount of 100 rs
# else don't apply discount

if amount > 1100:
 amount_to_be_paid = amount - discount
 print(amount_to_be_paid)
else :
  print(amount)
 







  