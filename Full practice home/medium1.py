#Take the user's age as input (remember input returns a string).Convert it into an integer.
#If age is 18 or above, print "Eligible to vote"
#Otherwise, print "Not eligible"..

age = int(input('Enter your age : :'))
if age >= 18:
    print("Eligible")
else:
    print("not eligible")

#Take a product price (float) and quantity (integer) from the user.
#Calculate the total cost.
#If total cost is more than 1000, give a 10% discount.
#Print the final amount.

product_price = float(input("Enter product price: "))
quantity = int(input("Enter your quantity: "))

total_cost = product_price * quantity

if total_cost > 1000:
    discount = total_cost * 0.10
    final_amount = total_cost - discount
else:
    print("Discount not allowed")
    final_amount = total_cost

print("Final amount:", final_amount)


#Take a password as string input.
#If the password is "python123", set a boolean variable to True, otherwise False.
#Print "Login successful" or "Login failed" accordingly.

#password = "python123"
#user_pass = input("Enter your password :")
#if password == user_pass:
#    print("Login successfull")
#else:
#    login("Login failed")

#           OR    [It was without boolean, now below it is with boolean:]

password = input("Enter your password :")
is_correct = password == "python123"

if is_correct:
    print("Login successfull")
else:
    print("Login failed")


#Take two integers from the user.
#Print:
#their sum
#Their average (in float)

number1 = int(input("Enter 1st number :"))
number2 = int(input('Enter 2nd number :'))

sum = number1 + number2
average = sum / 2
print("Sum :", sum)
print("Average :", average)


#Take a number from the user.
#Store in a boolean variable whether the number is even or not.
#Print "Even number" or "Odd number".

number = int(input('Enter number :'))
is_even = number % 2 == 0
if is_even:
    print('Number is even')
else:
    print("Number is odd")

#complile question khud se kra hua:
name = input("Enter your name :")
age = int(input("Enter your age :"))
salary = float(input("Enter your salary :"))

if age >= 18 and salary > 20000:
    print("User is not a kid ")
else:
    print("user is kid")

# GPT ka :
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))
student_input = input("Are you a student? (yes/no): ")

# Convert student input into boolean
is_student = student_input.lower() == "yes"

# Check eligibility
if age >= 18 and salary > 20000 and not is_student:
    print("Hello", name, ", you are eligible for the Premium Credit Card.")
else:
    print("Hello", name, ", you are not eligible for the Premium Credit Card.")
