import time
import random
import sys

snakes=[32,36,48,62,88,95,97]
d_snakes=[10,6,26,18,24,56,78]

ladders=[1,4,8,21,28,50,71,88]
i_ladders=[38,14,20,42,76,67,92,99]
c_name='Computer'

p_pos=0
c_pos=0

def intro():
    string="\nWelcome to SNAKE AND LADDER.\nVersion: 1.0.0\n" \
           "Snakes position: 32-->10, 36-->6,48-->26, 62--18, 88-->24, 95-->56, 97-->78\n" \
           "Ladder positon: 1-->38, 4-->14,8-->20,21-->42, 28-->76, 50-->67, 71-->92, 88-->99\n"
    for words in string:
        print(words,end="")
        time.sleep(0.02)

def roll_a_die():
    die = random.randint(1,6)
    return die

def exi_t():
    string = "Your chances are over.Game exiting!!!"
    for words in string:
        print(words, end="")
        time.sleep(0.01)
    sys.exit()

def game(pos,player):
    if pos==100:
        if player==1:
            print("\n     \ \ \ | |  | / / /      ")
            print("Game Over!!. You win the game")
            print("      / / / | | | \ \ \      ")
        else:
            print("\n     \ \ \ | |  | / / /      ")
            print("Game Over!!. Computer wins the game")
            print("      / / / | | | \ \ \      ")
        time.sleep(10)
        sys.exit()

    elif pos>100:
        print("score above 100. Try again!!")
        return 1

#check the current position
def chek_sn_or_ladd(pos):
    if pos in snakes:
        print("Oops!!Caught by a snake.")
        ind=snakes.index(pos)
        pos=d_snakes[ind]
        return pos
    elif pos in ladders:
        print("Hurray!!. Got a ladder. Climb up.")
        ind=ladders.index(pos)
        pos=i_ladders[ind]
        return pos
    else:
        return pos

#introduction of the game
print("Select the mode.(1/2)\n"
      "1. Player v/s Computer\n"
      "2. Multiplayer\n")
ch=int(input())
if ch==1:
    name=input("Enter your name: ")
    print("Your opponent is __"+c_name+"__")
    print("______________________________________\n")
intro()

#game starts here
print("__Your turn__")
print("Press '1' to roll the die")
ch = int(input())
chance = 3
while (ch != 1):
    print("something went wrong!!.\nTry again to press '1'")
    print("You have ",chance-1," chance left")
    ch = int(input())
    chance-=1
    if chance == 1:
        exi_t()

die=roll_a_die()
while(p_pos!=100 or c_pos!=100):
    print("you rolled ", die, ".")
    p_pos += die
    p_pos=chek_sn_or_ladd(p_pos)
    val=game(p_pos,1)
    if val==1:
        p_pos-=die
    print("You are at postion: ",p_pos)
    die = roll_a_die()
    print("Computer rolled: ",die)
    c_pos+=die
    c_pos=chek_sn_or_ladd(c_pos)
    val = game(c_pos,0)
    if val == 1:
        c_pos -= die
    print("Computer's position at: ",c_pos)
    print("\n Your turn, press any key to roll a die")
    ch=input()
    if ch==1:
        die=roll_a_die()
