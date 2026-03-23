import json

data = {                                        # Dictionary
    "title" : "Pk",
    "age" : 29

}

json_string = json.dumps(data)

# To write Json into a file, config.json :

with open("config.json", "w") as f :
    json.dump(data, f)


means = {
    "name" : "Subhit", 
    "age" : 20,
}
