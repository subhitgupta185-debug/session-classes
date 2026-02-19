# Easy level :



#Take an integer input from the user.
#Check whether the number is positive, negative, or zero.

number = int(input("ENTER NUMBER : "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negetive")
else:
    print("Zero")

# Take a float number from the user.
#Print its square and cube.

float = float(input("Enter your float number : "))

square = float ** 2
cube = float ** 3

print(square)
print(cube)




#User se apna first name aur last name lo (string).
#Unko combine karke full name print karo

text_1 = input("Enter first name :")
text_2 = input("Enter 2nd name :")

print(text_1,"and", text_2)



#Create a boolean variable:
#is_student = True
#If it is True, print "You get a student discount" Otherwise, print "No discount available"

is_student = True
if is_student:
    print("Gets an discount")
else:
    print("Discount allowed failed")






#Take an integer input from the user.
#Check whether the number is divisible by 5.


number = int(input("Enter ;"))
if number % 5 == 0:
    print("successfull")
else:
    print("failed")