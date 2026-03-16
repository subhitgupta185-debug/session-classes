
def add(a,b):
    return a + b

sum = add(12, 15)

def mul(sum,b):
    return sum*b

result = mul(sum, 2)
print(result)


#num = int(input("Enter number : "))  # User will eneter their number
#def check_possitive(num):
    #if num > 0:
     #   return("positive")          # Use return rather than print
    #else:
     #   return("Negetive")
#result = check_possitive(num)
#print(result)


    

#Returning multiple value :
#a = int(input("Enter 1st number : "))
#b = int(input("Enter 2nd number : "))
#def calculate(a,b):
 #   return a + b, a - b

#sum, diff = calculate(a,b)
#print(sum)
#print(diff)



def sum_average(range_value):
    sum = 0
    for i in range(range_value):
        sum = sum + i

    average = sum / range_value
    return sum, average
    
result = sum_average(5)
print(result)



def show_salary(salary):
    A = 52000
    B = 20000
    C = 171000
    D = 524100
    E = 251406258

    return A,B,C,D,E

A,B,C,D,E = show_salary("subhit")
print("A:", A)
print("B:", B)
print("C:",C)
print("D:",D)
print("E:",E)

def get_name(name):
    name = input("Enter your name :")
    return name 

def make_upper(name):
    return name.upper()

name = get_name()
result = make_upper(name)
print(result)