import random
random_number = random.randint(1,10)
user_input = int(input("Enter a number: "))

while(user_input != random_number):
    if(user_input > random_number):
        print("Too high")
    else:print("Too low")
    user_input = int(input("Enter a number: "))
print("correct")
