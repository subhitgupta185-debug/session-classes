tags = {"abc", "bcs", "xyz", "adc"}
print(tags)

tags.add("shubhit")
tags.remove("abc")

for i in tags:
    print(i)


a = {1, 2, 3}
b = {3, 4, 5}

# (1, 2, 3, 5, 6)
c = a | b
print(c)

# common elements between a and b

d = a & b
print(d)


# difference between a and b :
e = a - b
print(e)

# to find what elements exist in B not in A 
e = b - a
print(e)