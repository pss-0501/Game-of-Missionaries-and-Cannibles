#Python program to illustrate Missionaries & cannibals Problem - MINI Project
# Rules
print("\n")
print("\tGame Start\nNow the task is to move all of them to right side of the river")
print("Rules:\n1. The boat can carry at most two people\n2. If cannibals number is greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board \n4. The boat must have at least one person on board.")

left_Miss = 3		 #Left side Missionaries number
left_Can = 3		 #Left side Cannibals number
right_Miss = 0		 #Right side Missionaries number
right_Can = 0		 #Right side cannibals number
user_Miss = 0	 #User input for number of missionaries for right to left side travel
user_Can = 0	 #User input for number of cannibals for right to left travel
k = 0
print("\nM M M C C C | >>> --- | \n")       #Number of Players on Left side

# To move left to right
def Left_TO_Right():
    while True:         #This loop is for Input. Infinite loop till proper input is received 
        print("Left side -> right side river travel")
        #User Input
        user_Miss = int(input("Enter number of Missionaries travel => "))	
        user_Can = int(input("Enter number of Cannibals travel => "))

        if((user_Miss==0)and(user_Can==0)):
            print("Travel not possible if boat is empty!")
            print("Please Re-enter the values : ")
        #User Input Total <= 2; missionary number should be >0 for tavel; Cannibal number should be >0 for travel
        elif(((user_Miss+user_Can) <= 2)and((left_Miss-user_Miss)>=0)and((left_Can-user_Can)>=0)):
            return (user_Miss,user_Can)
            #break           # Break second loop if user input is correct and check win loss conditions
        else:
            print("Wrong or Invalid input! Read the rules and please re-enter : ")

        



# To move right to left
def Right_To_Left():
    while True:
        print("Right side -> Left side river travel")
        user_Miss = int(input("Enter number of Missionaries travel => "))
        user_Can = int(input("Enter number of Cannibals travel => "))
        
        if((user_Miss==0)and(user_Can==0)):
            print("Travel not possible if boat is empty!")
            print("Please Re-enter the values : ")
        elif(((user_Miss+user_Can)<=2)and((right_Miss-user_Miss)>=0)and((right_Can-user_Can)>=0)):
            return (user_Miss,user_Can)
            #break  #continue with the program; end function
        else:
            print("Wrong or Invalid input! Read the rules and please re-enter : ")

# To check lose condition
def You_Lose():
    if(((left_Can==3)and (left_Miss == 1))or((left_Can==3)and(left_Miss==2))or((left_Can==2)and(left_Miss==1))or((right_Can==3)and (right_Miss == 1))or((right_Can==3)and(right_Miss==2))or((right_Can==2)and(right_Miss==1))):
        print("Cannibals eat missionaries:\nYou lost the game")
        return False

# To check win condition
def You_Win():
    if((right_Miss+right_Can) == 6):
            print("You won the game : \n\tCongrats")
            print("Total attempt")
            print(k)
            return True
            #break

# Game Starts
try:
    while True:         # This loop is for checking condition of win & lose. Loop is infinite until lose or won
        
        #Left_TO_Right()

        """while True:         #This loop is for Input. Infinite loop till proper input is received 
            print("Left side -> right side river travel")
            #User Input
            user_Miss = int(input("Enter number of Missionaries travel => "))	
            user_Can = int(input("Enter number of Cannibals travel => "))

            if((user_Miss==0)and(user_Can==0)):
                print("Travel not possible if boat is empty!")
                print("Please Re-enter the values : ")
            #User Input Total <= 2; missionary number should be >0 for tavel; Cannibal number should be >0 for travel
            elif(((user_Miss+user_Can) <= 2)and((left_Miss-user_Miss)>=0)and((left_Can-user_Can)>=0)):
                break           # Break second loop if user input is correct and check win loss conditions
            else:
                print("Wrong or Invalid input re-enter : ")"""

        user_Miss,user_Can = Left_TO_Right()

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

        k += 1
        
        if (You_Lose() == False):
            break

        """if(((left_Can==3)and (left_Miss == 1))or((left_Can==3)and(left_Miss==2))or((left_Can==2)and(left_Miss==1))or((right_Can==3)and (right_Miss == 1))or((right_Can==3)and(right_Miss==2))or((right_Can==2)and(right_Miss==1))):
            print("Cannibals eat missionaries:\nYou lost the game")
            break"""

        if (You_Win() == True):
            break

        """if((right_Miss+right_Can) == 6):
            print("You won the game : \n\tCongrats")
            print("Total attempt")
            print(k)
            break"""

        #Right_To_Left()

        """while True:
            print("Right side -> Left side river travel")
            user_Miss = int(input("Enter number of Missionaries travel => "))
            user_Can = int(input("Enter number of Cannibals travel => "))
        
            if((user_Miss==0)and(user_Can==0)):
                print("Empty travel not possible")
                print("Re-enter : ")
            elif(((user_Miss+user_Can)<=2)and((right_Miss-user_Miss)>=0)and((right_Can-user_Can)>=0)):
                break
            else:
                print("Wrong input re-enter : ")"""

        user_Miss,user_Can = Right_To_Left()

        left_Miss += user_Miss
        left_Can += user_Can
        right_Miss -= user_Miss
        right_Can -= user_Can

        k += 1
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

        if (You_Lose() == False):
            break

        """if(((left_Can==3)and (left_Miss == 1))or((left_Can==3)and(left_Miss==2))or((left_Can==2)and(left_Miss==1))or((right_Can==3)and (right_Miss == 1))or((right_Can==3)and(right_Miss==2))or((right_Can==2)and(right_Miss==1))):
            print("Cannibals eat missionaries:\nYou lost the game")
            break"""

except EOFError as e:
	print("\nInvalid input please retry !!")
except ValueError as e:
    print("\nValue Error has occurred! Please retry !!")
