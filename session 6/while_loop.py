#count = 0


#while count < 77:  # while the condition is true keep looping , count = 0, 0 < 3
    #print(count) # 0
    #print("Hello") # hello
   # count = count + 7 # count = 0 + 5 = 5



# You ask user to enter password till he/she did'nt enter the correct password.

actual_password = "admin123"

password = ""
while password != actual_password: #"aferd" != admin123 # == / != [ When admin123 == admin123, it becomes false so python breaks the loop.]
    password = input("Enter your password : ")
    print("You entered password is wrong, please try again.")
