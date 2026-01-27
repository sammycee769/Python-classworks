names = ["Adebayo","Fola","Amina","Peace","christian","Ugo"]
name_list = [name for name in names if len(name) >= 5 if len(name) >4]
print(name_list)

student_tuple = ()
scores = 65,45,98,86,21
numbers = (23,76,9,90)
age = 31,
print(len(student_tuple))
print(len(scores))
print(len(numbers))
print(len(age))

number = [6,7]
number += numbers
print(number)

book =(["title"],9)
book[0].append("book")
book[0].append("car")
print(book)

num = [10,4,3,7,1,9,4,2,8,6]
def is_odd(x):
    return x%2!=0
print(list(filter(is_odd,num)))