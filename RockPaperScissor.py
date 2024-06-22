import random
print("Rules of the Rock-Paper-Scissor game as follows ")
print("Rock vs Paper->Paper Wins")
print("Rock vs Paper->Paper Wins")
print("Rock vs Scissor->Rock Wins")
print("Paper vs Scissor->Scissor Wins")
while True:
    print("Choices are  \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice=int(input("Enter your choice :"))
    if choice == 1:
        choice_name= 'Rock'
        print("""
                    ___
                ---'   __)
                      (___)
                      (___)
                      (__)
                ---._(__)
                """)
    elif choice == 2:
        choice_name= 'Paper'
        print("""
                     ___
                ---'    _)_
                           __)
                          ___)
                         ___)
                ---.____)
                """)
    elif choice==3:
        choice_name= 'Scissors'
        print("""
                    ___
                ---'   _)_
                          __)
                       ____)
                      (__)
                ---._(__)
                """)
    else:
        print("Invalid choice!")
    print("User choice is \n",choice_name)
    print("Now its Computers Turn....")
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'rocK'
        print("""
                    ___
                ---'   __)
                      (___)
                      (___)
                      (__)
                ---._(__)
                """)
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
        print("""
                     ___
                ---'    _)_
                           __)
                          ___)
                         ___)
                ---.____)
                """)
    else:
        comp_choice_name = 'scissoR'
        print("""
                    ___
                ---'   _)_
                          __)
                       ____)
                      (__)
                ---._(__)
                """)
    print(choice_name,'Vs',comp_choice_name)
    """if choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW" """   
    if (choice==1 and comp_choice==2):
        print('paper wins ,computer wins..',end="")
        result='papeR'
    elif (choice==2 and comp_choice==1):
        print('paper wins,you wins..',end="")
        result='Paper'
         
       
    if (choice==1 and comp_choice==3):
        print('Rock wins ,you wins',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins , computer wins..',end= "")
        result='rocK'
         
    if (choice==2 and comp_choice==3):
        print('Scissors wins,computer wins..',end="")
        result='scissoR'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins,you win..',end="")
        result='Rock'
    print("Do you want to play again?Type (Y/N)")
    ans = input()
    if ans =='N':
        break
