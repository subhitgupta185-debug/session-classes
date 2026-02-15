user = {
    "name" : "Abheejeet",
    "Age" : 58,
    "Phone no ": 99922545,
    "key": "value2"

}

print(user["name"])
print(user["Age"])
user_2 = {
    "Namw" : "Abhimanyu",
    "Age" : 74,
    "phone no": 998562547,
    "is_valid_user" : False
}

row1 = {
    "colm1" : "value1",
    "colm2" : "value2",
    'colm3' : "value3"
}


user["email"] = "abc@gamil.com"
print(user["email"])

user["phone no"] = 85952248
print(user["phone no"])


print(user)


for key, value in user_2.items():
    if key == "is_valid_user" and value == False:
     print("User invalid")
    print(key, value) # key, value