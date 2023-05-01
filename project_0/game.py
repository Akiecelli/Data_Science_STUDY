"Game guess the number"
import numpy as np
number = np.random.randint(1,101) #Find number
#game
count = 0 
while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100:  '))
    
    if predict_number > number:
        print('Count should be lesser')
    elif predict_number < number:
        print('Count should be bigger')
    else:
        print(f'You got it! This number is {number} for {count}')
        break