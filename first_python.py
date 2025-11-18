name = "bola"
age = 16
amount = 25.6
is_fail = True

print(type(name))
print(type(age))
print(type(amount))
print(type(is_fail))

print(len(name))
#print(len(age))
#print(len(amount))
#print(len(is_fail))

#Arithmetic operator
print(age * amount)
print(amount - age)
print(age ** 2)
print("=" * 25)
print("name" * 5)
print(25** 0.5)

#escape characters
print("This is ade's bike")
print('This is ade\'s bike')
print("this is hot tea \\ bread")

my_code_doc = """
The code is meant to collect user name and their age and print it out one after the other

"""
print(my_code_doc)

#collecting input from terminal

age = int(input("Enter user input; "))

#age = int(age)
#print(age, type(age))

#age = "rex"
#print(age, type(age))

#age = False
#print(age, type(age))

if age > 25:
    print ("You are allowed to vote in the election")
elif age < 25 and age > 18 or age == 25:
    print("you can only have a voter''s card")
elif age < 18 and age > 12:
    print("you can't have a voters card")
else: print ("you are unable to vote")
