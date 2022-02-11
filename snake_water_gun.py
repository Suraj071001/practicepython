import random

def snake_water_gun():
    print("enter your choice:\n'g' for gun\n'w' for water\n's' for snake")
    u_choice = input("-->")
    if c_choice == u_choice :
        print(f"opponent choice is {c_choice}")
        print(f"round draw (you both select same item)")
        global u
        u = "draw"
    elif c_choice == "g" and u_choice == "w" :
        print(f"opponent choice is {c_choice}")
        print(f"you won that round (opp. gun is worthless in water)")
        u = "won"
    elif c_choice == "g" and u_choice == "s" :
        print(f"opponent choice is {c_choice}")
        print("you lose that round (your snake is killed by opp.'s gun)")
        u = "lose"
    elif c_choice == "w" and u_choice == "s" :
        print(f"opponent choice is {c_choice}")
        print("you won that round (your snake will drink opp.'s water)")
        u = "won"
    elif c_choice == "w" and u_choice == "g" :
        print(f"opponent choice is {c_choice}")
        print("you lose that round (your gun is worthless in water)")
        u = "lose"
    elif c_choice == "s" and u_choice == "w" :
        print(f"opponent choice is {c_choice}")
        print("you lose that round (opp.'s snake will drink your water)")
        u = "lose"
    elif c_choice == "s" and u_choice == "g" :
        print(f"opponent choice is {c_choice}")
        print("you won that round (opp.'s snake is killed by your gun)")
        u = "won"
u_won = 0
o_won = 0
def decide_round() :
    global u_won
    global o_won
    if u == "draw" :
        print(f"No. of rounds you won : {u_won}\tNo. of rounds opponent won : {o_won}\n")
    elif u == "lose" :
        o_won += 1
        print(f"No. of rounds you won : {u_won}\tNo. of rounds opponent won : {o_won}\n")
    elif u == "won" :
        u_won += 1
        print(f"No. of rounds you won : {u_won}\tNo. of rounds opponent won : {o_won}\n")
rounds = 10
print("""Game has total 10 rounds 
if you won more round than opp. than you win """)
while rounds>0 :
    c_choice = random.choice(["s", "w", "g"])
    snake_water_gun()
    decide_round()
    rounds -= 1
    if rounds == 0 :
        if u_won>o_won :
            print("\nHurry ! You Won ")
        elif u_won<o_won :
            print("\nYou Lose")
        elif u_won==o_won :
            print("\nGame Draw")

