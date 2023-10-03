#Python program to illustrate Missionaries & cannibals Problem - MINI Project

# To move left to right
def Left_TO_Right(left_Miss,left_Can):
    try:
        while True:         #This loop is for Input. Infinite loop till proper input is received 
            print("Left side -> right side river travel")
            #User Input
            user_Miss = input("Press q to exit the game or Enter number of Missionaries travel (0,1,2) => ")

            if(user_Miss == 'q'):
                print("Thanks for Playing! GoodBye!! ")
                exit()
            user_Miss = int(user_Miss)

            user_Can = input("Press q to exit the game or Enter number of Cannibals travel (0,1,2) => ")

            if(user_Can == 'q'):
                print("Thanks for Playing! GoodBye!! ")
                exit()           
            user_Can = int(user_Can)    #Type Casting
            
            if((user_Miss==0)and(user_Can==0)):
                print("Travel not possible if boat is empty!")
                print("Please Re-enter the values : ")
                #User Input Total <= 2; missionary number should be >0 for tavel; Cannibal number should be >0 for travel
            elif(((user_Miss+user_Can) <= 2)and((left_Miss-user_Miss)>=0)and((left_Can-user_Can)>=0)):
                return (user_Miss,user_Can)
                #break           # Break second loop if user input is correct and check win loss conditions
            else:
                print("Wrong or Invalid input! Read the rules and please re-enter : ")
    except ValueError:
        print('Error Occurred. Please enter values as per rules and try again later! ')
    except Exception:
        print('Error! Try again later! ')


# To move right to left
def Right_To_Left(right_Miss,right_Can):
    try:
        while True:
            print("Right side -> Left side river travel")
            user_Miss = input("Press q to exit the game or Enter number of Missionaries travel (0,1,2) => ")

            if(user_Miss == 'q'):
                print("Thanks for Playing! GoodBye!! ")
                exit()

            user_Miss = int(user_Miss)

            user_Can = input("Press q to exit the game or Enter number of Cannibals travel (0,1,2) => ")
            
            if(user_Can == 'q'):
                print("Thanks for Playing! GoodBye!! ")
                exit()

            user_Can = int(user_Can)    #Type Casting

            if((user_Miss==0)and(user_Can==0)):
                print("Travel not possible if boat is empty!")
                print("Please Re-enter the values : ")
                #User Input Total <= 2; missionary number should be >0 for tavel; Cannibal number should be >0 for travel
            elif(((user_Miss+user_Can)<=2)and((right_Miss-user_Miss)>=0)and((right_Can-user_Can)>=0)):
                return (user_Miss,user_Can)
                #break  #continue with the program; end function
            else:
                print("Wrong or Invalid input! Read the rules and please re-enter : ")
    except ValueError:
        print('Error Occurred. Please enter values as per rules and try again later! ')
    except Exception:
        print('Error! Try again later! ')



def Lets_Play():
    # Game Starts
    # Rules
    print("\n")
    print("Game Start!\nNow the task is to move all of them to right side of the river")
    print("Rules:\n1. The boat can carry at most two people\n2. If cannibals number is greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board \n4. The boat must have at least one person on board.")

    left_Miss = 3		 #Left side Missionaries number
    left_Can = 3		 #Left side Cannibals number
    right_Miss = 0		 #Right side Missionaries number
    right_Can = 0		 #Right side cannibals number
    user_Miss = 0	 #User input for number of missionaries for right to left side travel
    user_Can = 0	 #User input for number of cannibals for right to left travel
    attempts = 0
    print("\nM M M C C C | >>> --- >>> | \n")       #Number of Players on Left side

    #Start here
    try:
        while True:         # This loop is for checking condition of win & lose. Loop is infinite until lose or won
            
            #Left_TO_Right()
            #Function to move left to right
            user_Miss,user_Can = Left_TO_Right(left_Miss,left_Can)

            left_Miss = (left_Miss - user_Miss) #Updating left side Missionary
            left_Can = (left_Can - user_Can)    #Updating left side Cannibals
            right_Miss += user_Miss #Updating right side Missionary
            right_Can += user_Can   #Updating right side Cannibals

            print('\n')
            for i in range(0,left_Miss):
                print('M ',end='')
            for i in range(0,left_Can):
                print('C ',end='')
            print("| --> | ",end="")
            for i in range(0,right_Miss):
                print('M ',end='')
            for i in range(0,right_Can):
                print('C ',end='')
            print('\n')

            attempts += 1

            #To check losing condition as per rules
            if(((left_Can==3)and (left_Miss == 1))or((left_Can==3)and(left_Miss==2))or((left_Can==2)and(left_Miss==1))or((right_Can==3)and (right_Miss == 1))or((right_Can==3)and(right_Miss==2))or((right_Can==2)and(right_Miss==1))):
                print("Cannibals eat missionaries:\nYou lost the game")
                KeepPlaying()
                break

            #To check winning condition
            if((right_Miss+right_Can) == 6):
                print("You won the game : \n\tCongrats")
                print("Total attempt", attempts)
                KeepPlaying()
                #print(k)
                break

            #Right_To_Left()
            #Function to move right to left
            user_Miss,user_Can = Right_To_Left(right_Miss,right_Can)

            left_Miss += user_Miss
            left_Can += user_Can
            right_Miss -= user_Miss
            right_Can -= user_Can

            attempts += 1
            print("\n")
            for i in range(0,left_Miss):
                print("M ",end="")
            for i in range(0,left_Can):
                print('C ',end='')
            print("| <-- | ",end="")
            for i in range(0,right_Miss):
                print('M ',end='')
            for i in range(0,right_Can):
                print('C ',end='')
            print("\n")

            # To check losing condition
            if(((left_Can==3)and (left_Miss == 1))or((left_Can==3)and(left_Miss==2))or((left_Can==2)and(left_Miss==1))or((right_Can==3)and (right_Miss == 1))or((right_Can==3)and(right_Miss==2))or((right_Can==2)and(right_Miss==1))):
                print("Cannibals eat missionaries:\nYou lost the game")
                KeepPlaying()
                break

    except EOFError:
        print("\nInvalid input please retry !!")
    except ValueError:
        print("\nValue Error has occurred! Please retry !!")
    except Exception:
        print("Error Occurred! Please try again !!")
        KeepPlaying()


def KeepPlaying():
    while True:
        Play_Again = input("Do you want to play again? Press y to play or Press enter to quit: ")
        if(Play_Again == 'y'):
            Lets_Play()
        elif(Play_Again == ''):
            print("Thanks for Playing! GoodBye!! ")
            exit()
        else:
            print("Invalid Input! Please try again. ")

print("Lets Play Cross the River !! ")
Lets_Play()