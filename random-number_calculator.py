from random import randint 

guess_num = randint(1,10)
user_input = -1
trial_period = 1

while guess_num != user_input:
    print("Trial number %d: " % trial_period, end='' )
    user_input = int(input())
    if user_input < guess_num:
        print("Too low")
    elif user_input > guess_num:
        print("Too high")
    else:
        print("You got it write")
    trial_period += 1