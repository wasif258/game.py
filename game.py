import random
l=["paper","rock","scisser"]
cchoice=random.choice(l)

while True:
    ccount=0
    ucount=0
    choiceforplay=input('''
       please enter the value which you want
       1 play
       2 stop           
                ''')
    # Step1
    if choiceforplay=="1":
        for i in range(1,6):
            choice=input('''
            1 paper
            2 rock
            3 scisser       
                        ''')
            if choice=="1":
                uchoice="paper"
            elif choice=="2":
                uchoice="rock"
            elif choice=="3":
                uchoice="scisser"
            else:
                print("invalid choice please choose the valid number")
    #Step2 
            if uchoice==cchoice:
                print("you select :-",uchoice)
                print("computer select :-",cchoice)
                print("This round is draw")
                ccount=ccount+1
                ucount=ucount+1
            elif (uchoice=="paper" and cchoice=="rock")  or (uchoice=="scisser" and cchoice=="paper") or (uchoice=="rock" and cchoice=="scisser"):
                print("you select :-",uchoice)
                print("computer select :-",cchoice)
                print("You won this round")
                ucount=ucount+1
            else:
                print("you select :-",uchoice)
                print("computer select :-",cchoice)
                print("computer won this round")
                ccount=ccount+1
    #Step3    
        if ucount==ccount:
            print("Your score is :",ucount)
            print("Computer score is :",ccount)
            print("Game is draw")
        elif ucount>ccount:
            print("Your score is :",ucount)
            print("Computer score is :",ccount)
            print("You won this game")
        else:
            print("Your score is :",ucount)
            print("Computer score is :",ccount)
            print("Computer won this game")
            
            
    elif choiceforplay=="2":
        break
    else:
        print("invalid choice please choose a valid number")
