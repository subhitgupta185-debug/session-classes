values = (10, 12, -1, 15)

# keep printing values until -1 is found :

for i in values: # [10, 12, -1, 15]
    if i == -1:
        break
    else:
        print(i) #10, 12


# wrong -->
#for i in values:
 #   if i == -1:
  #       print(i)
   # else:
    #    break


for i in values:
    if i == -1:
        continue
    else:
        print(i)
