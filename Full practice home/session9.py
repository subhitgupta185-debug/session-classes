file = open("C:\\Users\subhi\Downloads\Session classes\session-classes\Full practice home\session9abc.txt", "r") as fly:
content = fly.read()
print(content)

print(file.read())
file.close()


with open("C:\\Users\subhi\Downloads\Session classes\session-classes\Full practice home\session9abc.txt", "r") as fly:
    content = fly.read()
    print(content)


with open("C:\\Users\subhi\Downloads\Session classes\session-classes\Full practice home\session9abc.txt", "r") as file:
    for line in file:
        print(line)