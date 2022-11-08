from http.client import OK
import random



def start():
    ...
    #This function starts the guessing game loop logic. The function will pool and 
    #wait until the user inputs their guess and will wxit once some conditions are met. 

    animal = ['duck', 'swan', 'shark', 'tiger', 'snake', 'cat', 'dog']
    choice = animal [random.randint(0, len(animal)-1)]
    #duck choice
    if choice == 'duck':
        print("this animal is a small bird that swims and flies, and lives near ponds and rivers")
        i = input('guess the animal: ')
        if i == 'duck' or i == 'Duck':
            print('you are correct')
            return
        else: 
            print('you are wrong')
            
    #swan choice
    if choice == 'swan':
        print("this animal is a big bird with a long neck that swims and flies, and lives near ponds and rivers")
        i = input('guess the animal: ')
        if i == 'swan' or i == 'Swan':
            print('you are correct')
            return
        else: 
            print('you are wrong')
            
    #shark choice
    if choice == 'shark':
        print("this animal is a large fish that swims in the ocean and eats meat")
        i = input('guess the animal: ')
        if i == 'shark' or i == 'Shark':
            print('you are correct')
            return
        else: 
            print('you are wrong')
        
    #Tiger choice
    if choice == 'Tiger':
        print("This animal is a big cat that lives in the rain forest")
        i = input('guess the animal: ')
        if i == 'tiger' or i == 'Tiger':
            print('you are correct')
            return
        else: 
            print('you are wrong')
            
    #snake choice
    if choice == 'snake':
        print("this animal is a long reptile that has no arms or legs")
        i = input('guess the animal: ')
        if i == 'snake' or i == 'Snake':
            print('you are correct')
            return
        else: 
            print('you are wrong')
        
    #cat choice
    if choice == 'cat':
        print("this animal is a small house pet that loves fish and milk")
        i = input('guess the animal: ')
        if i == 'cat' or i == 'Cat':
            print('you are correct')
            return
        else: 
            print('you are wrong')
            
    #dog choice
    if choice == 'dog':
        print("this animal is a big or small house pet that is considered mans best friend")
        i = input('guess the animal: ')
        if i == 'dog' or i == 'Dog':
            print('you are correct')
            return
        else: 
            print('you are wrong')
            
    # guess loop
    guess = ""
    numofguesses = 0
    while numofguesses < 4: 
        numofguesses = numofguesses + 1 
        if guess == choice: 
            print("You win!") 
    option = input("Do you want to try again or quit? ") 
    if option == "try again": 
        print("") 
    elif option == "quit": 
        return 
    if guess != choice: 
        print("Try again!") 
        guess = input("What is the animal? ") 
        if guess != choice: 
            print("Try again!") 
            guess = input("What is the animal? ") 
        
    

start()

