#numbers = [10, 12, 15, 65, 18, 20]
#Index =    0   1   2   3   4   5
#numbers.append(90)
#print(numbers)



#numbers.remove(15)
#print(numbers)



#numbers[2] = 52
#print(numbers)


#print(numbers[:3])
#print(numbers[3:])
#print(numbers[2:5])


#numbers.insert(2, 200)
#print(numbers)


#numbers.pop(2)
#print(numbers)



#numbers = [10, 20, 30, 40, 50]

#numbers.append(60)
#print(numbers)
#numbers.insert(2, 25)
#numbers.remove(40)
#numbers.remove(50)
#print(len(numbers))
#print(numbers)




# Dictionary question practice below :

TIPS = {
    "student_1" : "Garvit",
    "student_2" : "Subhit",
    "student_3" : "Shaurya"
}


Galogotia = {
    "ananya" : "dhingra",
    "suvarcha" : "sharma",
    "ditya" : "narula"
}



Galogotia["ditya"] = "Love"
for key, value in Galogotia.items():
    print(key,":", value)


# Tuples : 

Tup = (10, 25, 36)
for i in Tup:
    print(i)


a = (10, 25, 36, 98, 254)
print(len(a))
print(a)




tags = {"abc", "zyx", "pqrs" }
print(tags)
tags.add("mno")
print(tags)
tags.remove("pqrs")
for i in tags:
    print(i)




a = {1, 2, 3}
b = {3, 4, 5}

c = a | b   # To merge in 1.
print(c)


d = a & b
print(d)  # Common element

e = a - b
print(e)   # Difference between a and b

f = b - a
print(f)  # To find what elemnts present in B not in A..






# Given data

list1 = [10, 20, 30, 40, 50]
tuple1 = (30, 40, 50, 60, 70)

student = {
    "name": "Rahul",
    "age": 21
}

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}




list1.append(60)
list1.insert(2, 25)
list1.remove(40)
for values in list1:
    print(values)
    print(len(list1))
    

print(tuple1[3])
print(len(tuple1))

student["city"] = "Delhi"








list = [10, 25, 16, 59, 42]

list.append(26)
print(list)
list.remove(26)
print(list)



list.insert(2,16)
print(list)

