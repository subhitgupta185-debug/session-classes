file = open("C:\\Users\subhi\Downloads\Session classes\session-classes\session 9\hello.txt", "r")
print(file.read())
file.close()

# everything can be seen, using file.read()


#file = open("C:\\Users\subhi\Downloads\Session classes\session-classes\session 9\hello.txt", "r")
#print(file.read())


# error happens  ???
#file.close()    # before closing the file


# with statement:

with open("C:\\Users\subhi\Downloads\Session classes\session-classes\session 9\hello.txt", "r") as fly:
    content = fly.read()
    print(content)


# Python guarentees: file close, even if crash happens, even if exception occurs.

# Read line by line:
#with open("C:\\Users\subhi\Downloads\Session classes\session-classes\session 9\hello.txt", "r") as f:
    #for line in f:
       # print(line)



with open("C:\\Users\subhi\Downloads\Session classes\session-classes\session 9\hello.txt", "r") as file:
    for line in file:
        content = line.strip()
        if content == "shubhendu":
            continue
       # print(content)


# readlines() --> readlines basically converts or stores all lines into a list 


with open("C:\\Users\subhi\Downloads\Session classes\session-classes\session 9\hello.txt", "r") as file:
    lines = file.readlines()
    print(lines)