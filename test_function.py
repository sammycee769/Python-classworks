def is_even(number):
    if(number % 2 == 0):
        return True
    else: return False 

def get_hours (minutes):
    hours = minutes // 60
    minutes_remaining = minutes % 60
    return hours,minutes_remaining

def multiply (number_one,number_two):
    result =0
    for count in range(number_two):
        result += number_one 
    return result
print(multiply(10,6))
