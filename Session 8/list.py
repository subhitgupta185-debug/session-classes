score = [4, 6, 8, 9, 5]
#index = 0  1  2  3  4


# index is always starts with 0

# name of list [Index]
value = score[1]
#print(value)

value2 = score[3]
#print(value2)



# modifying list :
# adding at the end
# removing some value
# replicating the value

marks = [20, 40, 56, 98, 99]
#index = 0  1    2   3   4
# Adding a marks at the end ; 89
# marks = [20, 40, 56, 98, 99, 89]
marks.append(89)
#print(marks)

# remove 40
#print(marks[1])
#marks.remove(20)
#print(marks[3])



# update attendence : 

attendence = [32, 25, 1, 16, 84, 52]
#index         0    1   2  3   4   5   
print(attendence[2])
attendence[2] = 34
print(attendence[2])
print(attendence[4])
attendence[4] = 99
print(attendence[4])



# List slicing (Sub list) ;
world_list = [50, 52, 20, 62, 85]
# world_list1 = [50, 52, 20]
# world_list2= [20, 62, 85]
# world_list3 = [52, 20, 62]

world_list1 = world_list[0:3]
print(world_list1)
# To print last numbers of a list
world_list2 = world_list[2:]
print("Second record : ", world_list2)
# To print all starting without marking specifically
world_list3 = world_list[:3]
print(world_list3)






abc = [1, 2, 3]
abc.insert(0, 10) #Insert index value
print(abc[0])
abc.insert(1, 26)
print(abc[1])
abc.insert(2,25)
print(abc[2])




print(abc)
abc.pop(1)
print(abc)



c = [25, 15, 7]
empty_list = []
for i in c :
    empty_list.append(i)
print(empty_list)




d = [3, 4, 5]
# insert values = [1, 3, 4, 6, 5]

d.insert(0, 1)
d.insert(3, 6)
print(d)