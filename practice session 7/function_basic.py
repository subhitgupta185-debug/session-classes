def greet(): 
    print("Hello")

greet()


def greetings(name):
    print("Hello", name)

greetings("aman")


#Multiple parameters 

def calculate_total(unit_price, quantity): #unit_price = 300, quantity =3 
    total = unit_price * quantity 
    print(total) #total = 900

calculate_total(300, 3)