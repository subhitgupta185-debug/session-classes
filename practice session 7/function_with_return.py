def add(a, b): # a = 2, b = 3
    sum = a + b # sum = 5
    return sum #return 5. # dead end
    print(sum)

def subtract(a, b): #a = 5, b = 1
    diff = a - b #5 - 1 = 4
    print(diff) #4


output = add(2, 3) #sum = 5
print(output)
subtract(output , 1) #subtract (5, 1)






#functions can return early to stop executions
def check_access(is_verified): 
    if not is_verified: # not False if true:
        return "Access denied" # return access denied
    else : 
        print("Nice")
        print("Hello")
        print("Bye")
        return "Access graunted"
    
access = check_access(False) #access = "Access denied"
print(access)

