def first_and_last_characters(word):   
    if len(word) < 2:
        return("''")
    else:
        return(word[0]+word[1]+word[-2]+word[-1])
#print(first_and_last_characters("n"))
def add_ing(word):   
    if len(word) < 3:
        return word
    if word[-3]+word[-2]+word[-1] == "ing":
        return(word + "ly")
    else:
        return(word+"ing")
#print(add_ing("abcing"))


def check_last_first_index(words):
    bength = ""
    largest = len(words[0])
    for string in words:
        if len(string) > largest:
            largest = len(string)
            if largest == len(string):
                bength += string
    return largest, bength
 

print(check_last_first_index(["samuel", "ayobama", "amela", "smas"]))

def odd(word):
    new_word=""
    for count in range(len(word)):
        if count % 2 != 0:
            new_word+=word[count]
    return new_word
#print(odd("samuel"))


def is_smallest(numbers):
    smallest = numbers[0] 

    for count in numbers:
        if count < smallest:
            smallest = count
    return(smallest)
#print( is_smallest([12,10,7,9,56,8,5]))


def is_largest(numbers):
    smallest = numbers[0] 

    for count in numbers:
        if count > largest:
            largest = count
    return(largest)
def multiply(string,number):
    if type(number) == float:
        return string
    else:
        return string * number
print(multiply("hello",3.5))

def square(numbers):
    new_number=[]
    for count in numbers:
        count*=count
        new_number.append(count)
    return new_number
print(square([2,3,4,5]))
def addition(numbers):
    counter=0
    for count in numbers:
        count*=count
        counter+=count 

    return counter
print(addition([2,3,4,5]))










