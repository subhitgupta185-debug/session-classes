name = input("Enter your name : ")


with open("output.log", "a") as file :
    file.write("Program started\n")
    file.write(f"user : {name}\n")
    file.write("program ended!")