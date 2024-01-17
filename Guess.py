import random 
def is_numeric(Value):
    try:
        float(Value)
        return True
    except ValueError:
        return False
random_number = random.randint(1,20)
#print("Random number is : ", random_number)
user_number = input("Enter a number from 1 to 20: ")
if int(user_number) == random_number:
    print(f"user number is {user_number} while random number is {random_number}")

elif int(user_number) < random_number:
    less = random_number - int(user_number)
    print(f"user number is {user_number} while random number is{random_number} thus less {less}")
    
else:
    more = int(user_number) - random_number
    print(f"user number is {user_number} while random number is {random_number} thus more {more}")
