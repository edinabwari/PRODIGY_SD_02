import random 
random_number = random.randint(1,20)
guess_count = 0

def is_numeric(Value):
    try:
        float(Value)
        return True
    except ValueError:
        return False
    
while True:
    user_number = input("Enter a number from 1 to 20 : ")
    print()
    
    if is_numeric(user_number):
        user_number = float(user_number)
        guess_count += 1
        
        
        if float(user_number) < random_number:
            print("The user number is less than the random number ")
        elif user_number > random_number:
            print("The user number is greater than the random number")
        else:
            print(f"Congratulations! You guessed the correct number {random_number} in {guess_count} attempts.")
            break
    else:
        print("Invalid input! Enter a valid number.")