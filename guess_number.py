print("guess the no. b/w 1 and 200 ")
print("you have 10 guesses")
no_of_quesses = 10
hidden_number = 89
while no_of_quesses > 0 :
    n = int(input("enter the number :"))
    no_of_quesses = no_of_quesses -1
    print("no.of quesses left =",no_of_quesses)
    if n>hidden_number :
        print("your no. is greater than hidden number\n")
    elif n<hidden_number :
        print("your no. is less than hidden number.\n")
    elif n == hidden_number :
        print("hurry ! you won the game.")
        break
if no_of_quesses==0 :
    print("game over")