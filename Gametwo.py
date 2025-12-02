import random
random_number = random.randint(1,10)
user_input = int(input("Enter a number: "))
count = 0

while(user_input != random_number):
    if(count >= 3):
        if(user_input > random_number):
            print("Too high")
        elif(user_input < random_number)
            print("Too low")
        elif(user_input == random_number)
            print("correct")
            break;

    user_input = int(input("Enter a number: "))
    print("correct")
    
    user_input = int(input("Enter a number: "))
    for count in range(3):
        if(user_input > random_number):
            print("Too high")
        else:print("Too low")
        user_input = int(input("Enter a number: "))
    print("correct")
