name = input("Enter your name : ")
Age = int(input("Enter your age : "))


with open("practice.log", "a") as abc:
    if Age >= 25:
        print("Match found")
    else: 
        print("Match didn't found")
    abc.write(f"user : {name}\n")
    abc.write(f"Your age : {Age}\n")
    abc.write("Program closed")
