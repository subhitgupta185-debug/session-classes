import json

json_response = '''
{ 
    "user" : {
    "id" : 123,
    "profile" : {
        "name" : "shubhendu",
        "roles" : ["admin","editor"]
     }
    }
}
'''

parsed_dict = json.loads(json_response)
print(type(parsed_dict))

user = parsed_dict["user"]
print(user)

profile = user["profile"]
print(profile)

name = profile["name"]                  #  parsed_dict["user"]["profile"]["name"]
print(name) 

# or to access directly :

name = parsed_dict["user"]["profile"]["name"]
print(name)



roles = parsed_dict["user"]["profile"]["roles"]
print(type(roles))
for i in roles:
    print(i)
 # or
#print(roles[0]) 
#print(roles[1])    To access a single variable..


val = parsed_dict.get("user").get("profile").get("abc")
print(val)