import random
import time 



def roll():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    return dice_1 + dice_2


def wait():
    time.sleep(.5)

def player_won(bet, human_bankroll, cpu_bankroll):
    human_bankroll +=  bet * 2
    print("Player1 won!: ",bet ," dollars")
   

def cpu_won(bet, human_bankroll, cpu_bankroll):
   cpu_bankroll += bet * 2
   #human_bankroll -=  bet
   print("Player1 lost: ", bet, " dollars\n")
   
   


def main():
    global human_bankroll, cpu_bankroll
    human_bankroll = 100
    cpu_bankroll = 100

    while True:
        bet = 0
        bet = input("How much do you want to bet? ")
        if bet.isdigit():
            bet = int(bet)
            if int(bet) > human_bankroll:
                print("You don't have enough funds for that bet.")
                continue
        else:
            print("Bet must be a number")
            continue


        
        human_turn = roll()
        print("You rolled: " , human_turn)
        wait()
        cpu_turn = roll()
        wait()
        print('The CPU rolled: ' , cpu_turn)
        
        #human turn
        if human_turn > cpu_turn:
            human_bankroll -= bet
            cpu_bankroll -= bet
            print("Your turn player1\n")
            value = roll()
            wait()
            print("You rolled a: ", value)
            wait() 
            if value == 7 or value == 11:
                player_won(bet,human_bankroll,cpu_bankroll)
            elif value == 2 or value == 3 or value == 12:
                cpu_won(bet,human_bankroll,cpu_bankroll)
            else:
                point = value
                wait()
                print("The point is: ", point)
                while True:
                    value = roll()
                    if value == point:
                        print("The point was rolled.")
                        player_won(bet,human_bankroll,cpu_bankroll)
                        break
                    elif value == 7:
                        print("The roll was 7.")
                        cpu_won(bet,human_bankroll,cpu_bankroll)
                        break
                   
        else:
            #CPU turn 
            human_bankroll -= bet
            cpu_bankroll -= bet
            print("It's the computer's turn\n")
            value = roll()
            wait()
            print("CPU rolled a: ", value)
            if value == 7 or value == 11:
                print("CPU won the come out\n")
                cpu_won(bet,human_bankroll,cpu_bankroll)
            elif value == 2 or value == 3 or value == 12:
                player_won(bet,human_bankroll,cpu_bankroll)
            else:
                point = value
                print("The point is: ", point)
                while True:
                    value = roll()
                    if value == point:
                        print("The point was rolled.")
                        cpu_won(bet,human_bankroll,cpu_bankroll)
                        break
                    elif value == 7:
                        print("The roll was 7.")
                        player_won(bet,human_bankroll,cpu_bankroll)
                        break                 
        print("CPU has ", cpu_bankroll, "dollars left \n")
        print("You have ", human_bankroll, "dollars left \n")                  
        if cpu_bankroll == 0 or human_bankroll == 0:
            print("Oops! Someone has no more money to bet")
            break
    print("Game Over!")        

if __name__ == "__main__":
    main()




