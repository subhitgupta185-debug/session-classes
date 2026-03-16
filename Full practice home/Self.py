User = input("Enter your name brother : ")
age = int(input("Enter your age : "))
password = input("Enter your password : ")
biometric = input("Is your biometric done ?(Yes/no) :")
biometric_user = "Yes"
actual_password = "Indira2123"
if age >= 18 and biometric == biometric_user and password == actual_password:
    print("Login allowed boss")
else:
    if password != actual_password:
        print("Incorrect password")
    print("Sorry boss go and finished previous things first!!!")


