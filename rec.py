def sum_of_numbers(n):
    if n == 0:
        return 0
    return sum_of_numbers(n - 1) + n 

result = sum_of_numbers(5)
print(result) 
