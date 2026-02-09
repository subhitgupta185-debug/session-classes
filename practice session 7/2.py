def add(a, b):
    sum = a + b
    return sum
def subtraction(a, b):
    diff = a - b
    print(diff)

sum = add(2, 3)
subtraction( sum, 1)




2 + 3 - 1


# functions can return early to stop execution :
def check_access(is_verified):  # is_verified = False
    if not is_verified:   # not is_verified --> not False --> True
        return "Access denied"  # return Access denied..
    else:
        print("nice")
        print("Hey")
        print("Bye")
        return ("access granted")
        
access = check_access(False)
print(access)






# python allows returning multiple values:

def greetings(name):
    greeting_sentence = "Hey " + name
    return greeting_sentence , name
    
name, greeting_sentence = greetings("Subhit")
print(name)
print(greeting_sentence)







# practice.....
def add(a, b):
    sum = a + b
    return sum
def sub(a, b):
    subtraction = a - b
    return subtraction
def quantity(a, b):
    total = a * b
    return total
def average(a,b):
    total_cost = a / b
    print(total_cost)

summation = add(2000,5)
subtraction2 = sub(summation, 5)
total = quantity(subtraction2, 1000)
actuall_total = average(total, 10) 
    



# sum and average

def sum_and_average(range_value):     # range_value = 4
    sum = 0                                                   #i
    for i in range(range_value):           # for i in [0, 1, 2, 3 ]
        sum = sum + i                 # sum = 6
 
                    # average = sum / Total numbers
                    # sum / 4
    average = sum / range_value

    return sum, average

s, avg = sum_and_average(4)
print(s)
print(avg)
















def greetings(name):
    greetings_sentence = "Hello " + name
    return name, greetings_sentence

name, greeting_sentence = greetings("Subhit")





#def show_details(user_details):
   # Name = "Rahul"
    #Age = "52"
    #Job = "Teacher"
    #Income = 50000
    
    #return Name, Age, Job, Income

#Name, Age, Job, Income = show_details("Rahul details")
#print("Hey", Name)
#print("Great to know, you are :", Age, "years old.")
#print("Your status is ", Job)
#print("Your income is : ", Income)









def subject_marks(candidate_marks):
    physics = 98
    maths = 99
    chem = 99
    biology = 100
    english = 89
    return physics, maths, chem, biology, english

physics, maths, chem, biology, english = subject_marks("Rahuls marks")
print("Physics : ", physics)
print("Maths : ",maths)
print("Chem : ",chem)
print("Biology : ",biology)
print("English : ",english)

total = physics + maths + chem + biology + english
print("Total : ", total)
if total > 200:
    print("Passed successfully")
else:
    print("Failed successfully ")
    

# get name from terminal and print it by making it intp upper case.
# str.upper() str-->name, NAME


# get_name
# make_upper

def get_name():
    name = input(" Enter name : ")
    return name

def make_upper(name):
    return name.upper()

name = get_name()
Result = make_upper(name)
print(Result)


