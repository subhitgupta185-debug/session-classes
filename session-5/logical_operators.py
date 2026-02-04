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