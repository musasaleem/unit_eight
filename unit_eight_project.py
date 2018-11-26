# Name: Musa Saleem
# Date: 11/26/18
# Last Modified: 11/26/18
# Comments: This is a game of blackjack by using buttons. I used functions to make buttons and used "if" statements
# to declare the winner. I formatted the positions and added pictures in my game.

import tkinter
import random


def draw_card():
    """
    Importing the random range of numbers you can get when getting another card
    :return: nothing
    """
    return random.randint(1, 10)



def no_moves():
    """
    The results of who wins the game, if the user chooses to stay
    :return: nothing
    """
    user = int(UTotal.get())
    deals = int(Dtotal.get())
    if user > 21:
        recognize.set("Dealer win")
    elif user < deals:
        recognize.set("Dealer Win")
    elif user > deals:
        recognize.set("User Win")
    elif user == deals:
        recognize.set("Tie")


def BigHit():
    """
    The results of who wins the game, if the user chooses to draw another card, or hit
    :return: nothing
    """
    Hit = int(UTotal.get())
    Hit += draw_card()
    UTotal.set(Hit)
    Dealer = int(Dtotal.get())
    if Hit > 21:
        recognize.set("Dealer win")
    elif Hit < Dealer:
        recognize.set("Dealer Win")
    elif Hit > Dealer:
        recognize.set("User Win")
    elif Hit == Dealer:
        recognize.set("Tie")


root = tkinter.Tk()  # imports the game
root.title("BlackJack")  # Title of the game, "BlackJack"
Blackjack = tkinter.Label(root, text="BlackJack")  # Places title of game on the game
Blackjack.grid(row=1, column=2)  # Placement of the tile of the game
explanation = tkinter.Label(root, text="You will be given 2 cards on random and having an option to draw another card. "
                                       "You win if your cards are higher than the dealers and less than 21")
# Description of the game
explanation.grid(row=2, column=2)  # Placement of the explanation


Ace = draw_card() + draw_card()  # draw_card(): function drawing a card from 1-10. Initial value of the user cards.
Joker = draw_card() + draw_card()  # draw_card(): function drawing a card from 1-10. Initial value of the dealers cards.


Dtotal = tkinter.StringVar()  # Holds dealer total
UTotal = tkinter.StringVar()  # Holds user total
recognize = tkinter.StringVar()  # Label to show who wins
Dtotal.set(Joker)  # Setting the dealer total
UTotal.set(Ace)  # Setting the User total


hit = tkinter.Button(root, text="hit", command=BigHit)  # gives the button the command of BigHit which adds a card
hit.grid(row=3, column=2)  # Placing the hit button
stay = tkinter.Button(root, text="stay", command=no_moves)  # gives button the command of no_moves: keeps cards as is
stay.grid(row=4, column=2)  # Placing the stay button


img = tkinter.PhotoImage(file="Try1.png")  # Imports the photo
panel = tkinter.Label(root, image=img)  # Another function for importing the photo
panel.grid(row=3, column=1)  # Places the photo
img1 = tkinter.PhotoImage(file="Try2.png") # Imports the second photo
panel1 = tkinter.Label(root, image=img)  # Another function for importing the second photo
panel1.grid(row=3, column=3)  # Places the second photo


user_total = tkinter.Label(root, text="Your total is:")  # The label for giving the user total
user_total.grid(row=5, column=1)  # The placement of where the label will be for the user total
dealer_total = tkinter.Label(root, text="Dealer total is:")  # The label for giving the dealer total
dealer_total.grid(row=5, column=3)  # The placement of where the label will be for the dealer total

KingUser = tkinter.Label(root, textvariable=UTotal)  # The user total
KingUser.grid(row=6, column=1)  # The placement for user total
KingDealer = tkinter.Label(root, textvariable=Dtotal)  # The dealer total
KingDealer.grid(row=6, column=3)  # The placement for dealer total


Final = tkinter.Label(root, textvariable=recognize)  # Gives the final result
Final.grid(row=7, column=2)  # Places the final result


root.mainloop()
