
# def add(num):
#     return num + n

# print(add(13))

# this is a game where you choose a number between 1 and 30 then number n is subtracted from the user choice the is verified ass even or odd
# then choices have a limit of 10 after which the percentage is calculated as per the choice to be wrong or right
# number outside the specified number is considered wrong

n = 6
gameplay_time = 0
gamepoints = 0


# enables the user to pick the number
def pick():
    user_num = float(input('enter a number: '))
    
    if user_num > 30 or user_num < 1 :
        print('please select a no. between 1 and 30')
        return None
    
    return user_num  

# checks if the choice by the user is wrong or right  
def get_answer(user_num):   # user_answer is the answer provided by the user to verify if their answer is even or odd and done after giving the number.
    result = user_num - n
    
    # checks if the user_num is even or odd 
    if result %2 == 0:
        return 'even'
    else:
        return 'odd'
    
    
def correct_wrong(user_answer, actual_answer):   
    # verifies if the user_answer matches the actual_answer and returns 1 point if correct and 0 if wrong
    if actual_answer == user_answer:
        return 1
    else :
        return 0

# calculating the percentage
def percentage(gamepoints, gameplay_time):
    if gameplay_time == 10 :
        percent = (gamepoints/gameplay_time) * 100
        return percent

# loop to run the game
while gameplay_time < 10:
    print(f'round {gameplay_time + 1} of 10')
    
    # call the pick function to get the user number
    picked = pick()
    if picked is None:
        gameplay_time +=1
        continue
    
    # unpacking the returned value that was returned to pick() function
    user_num = picked  
    
    # get the user answer
    user_answer = input('is the number even or odd : ')
    
    # actual answer is same as the number given by the user
    actual_answer = get_answer(user_num)
    
    # function to check the wether wrong or right
    points = correct_wrong(user_answer, actual_answer)
    
    
    if gamepoints == 1:
        print('correct')
        gamepoints += points
    else :
        print(f"you're wrong...the correct answer is {actual_answer}")
        
    gameplay_time += 1
    
    percentage = percentage(gamepoints, gameplay_time)
    percent = percentage
    
print('GAME OVER!!!')
print(f"you have gotten {gamepoints}/10")
print(percent)



# still got problems to be fixed 