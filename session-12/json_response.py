import json 
                                    # Below are the strings :
response = '''                                 
{
    "Name" : "Subhit",
    "Age" : 20,
    "Number" : 9992862576,
    "Other" : {
        "Email" : "subhitgupta185@gmail.com",
        "College" : "TIIPS"    
    }
}
'''




### { " n a m e " : }
## Breaks into piece. { --> start object, name --> saring  :--> seprator, 30 --> number} --> end object [ It is known as Lexical analysis (It's apart from syllabus very deep concept)]
## structure validation:
## Converts into dictionary
parsed = json.loads(response)   # parsed converts the string into the dictionary 
print("Type of Response :", type(parsed))
print("Your response : ", parsed)

