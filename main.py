def probabilityCalculator():
    
    uniqueInputOptions = input('Enter number of unique possibilities (int only): ')
    timesRun = input('enter number of times program is run: ')
    
    uniqueInputOptions = int(uniqueInputOptions)
    timesRun = int(timesRun)
    
    totalPossibilities = uniqueInputOptions**timesRun
    chanceOfUniqueOutput = 100/totalPossibilities
    iChanceOfUniquOutput = int(chanceOfUniqueOutput)
    
    if iChanceOfUniquOutput != 0 :
    
        print('The chance of you getting any one unique string of output is ', chanceOfUniqueOutput,'%.')
    elif timesRun == 0 or uniqueInputOptions == 0:
        print('There is 0% chance of any event occuring.')
    else:
        print('The chance of any unique output is too small to calculate')



def possibilitycalculator():
    
    uniqueInputOptions = input('Enter number of unique possibilities (int only): ')
    timesRun = input('enter number of times program is run: ')
    
    uniqueInputOptions = int(uniqueInputOptions)
    timesRun = int(timesRun)
    
    totalPossibilities = (1/uniqueInputOptions)*timesRun
    chanceOfUniqueOutput = totalPossibilities * 100

    print('The chance of you getting any one unique output is ', chanceOfUniqueOutput,'%.')



while True:
    
    choice = input('select 1 or 2: ')
    
    if choice =='1':
        probabilityCalculator()
        
    elif choice == '2':
        possibilitycalculator()
        
    elif choice =='3':
        break
        
    else:
        
        print('invalid input')