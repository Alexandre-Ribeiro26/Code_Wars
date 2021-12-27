def sum_two_smallest_numbers(numbers):
    numbers.sort() 
    
    a = sum(numbers[:2])
    
    return a 
