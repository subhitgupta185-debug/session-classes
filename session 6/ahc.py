def sum_and_average(range_value):
    sum = 0
    for i in range(range_value):
        sum = sum + i

        average = sum / range_value
        return sum, range_value
    
Summation, Avg = sum_and_average(6)
print(Summation)
print(Avg)






