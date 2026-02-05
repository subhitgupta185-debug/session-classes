age = 17 
has_address = True

# if the age is greater than or equals to 18 and it has address , print("Entry allowed"), else denied.
# age>= 18 and has_address == True



if age >= 18 and has_address:  # age >= 18, 20 >= 18 True and True ==> True
    print("Entry allowed ")
else : 
    print("Entry denied")









balance = 500
price = 300
is_user_account_exists = False

# balance > price price > 0 is_user_account_exists == print order placed
# else order can't be placed 

if balance >= price and price > 0 and is_user_account_exists:  # Balance >= Price (True) as balance is 500 and price is 300.
    print("Order placed")                                             # Price > 0 (True) Price is 300 greater than 0..
else :                                                                # is_user_account_exists == True : (Yes it exists )
    print("Order can't be placed")




### or operators

login_google = False
login_email = True

if login_google or login_email :  # False or True ==> True
    print("Access graunted")
else :
    print("Access can't be graunted")


is_owner = True
is_admin = False

if is_owner or is_admin :                       # True or False ==> True
    print("Acess should be graunted")
else :
    print("Not graunted")



#Rough Work Practice....
#price = 120
#supercoin = 100
#voucher = 200

#if supercoin > price or voucher > price 
#print("")


is_blocked = False
# If the user not blocked, access graunted.

if is_blocked == True:
    print("Access graunted")

if not is_blocked : 
    print("Access not graunted")
    



marks = 95
# if marks are less than 95, print "Better luck next time."

if marks == 95:
    print("Passed")

if marks < 95:
    print("Better luck next time.")


completed = False 
# If user has not completed , print retry.

if not completed :
    print("Retry")