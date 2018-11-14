import tkinter
import random


def draw_card():
    return random.randint(1, 10)


def no_moves():
    User = int(UTotal.get())
    Deals = int(Dtotal.get())
    if User > Deals:
        recognize.set("User win")
    elif User < Deals:
        recognize.set("Dealer Win")
    elif User > 21:
        recognize.set("Dealer Win")
    elif User == JokDealser:
        recognize.set("Tie")


def BigHit():
    Hit = int(UTotal.get())
    Hit += draw_card()
    UTotal.set(Hit)
    Dealer = int(Dtotal.get())
    if Hit > Dealer:
        recognize.set("User win")
    elif Hit < Dealer:
        recognize.set("Dealer Win")
    elif Hit > 21:
        recognize.set("Dealer Win")
    elif Hit == Dealer:
        recognize.set("Tie")


root = tkinter.Tk()
root.title("BlackJack")
Blackjack = tkinter.Label(root, text="BlackJack")
Blackjack.grid(row=1, column=2)
explanation = tkinter.Label(root, text="You will be given 2 cards on random and having an option to draw another card. "
                                       "You win if your cards are higher than the dealers and less than 21")


Ace = draw_card() + draw_card()
Joker = draw_card() + draw_card()

Dtotal = tkinter.StringVar()
UTotal = tkinter.StringVar()
recognize = tkinter.StringVar()
Dtotal.set(Joker)
UTotal.set(Ace)

explanation.grid(row=2, column=2)
hit = tkinter.Button(root, text="hit", command=BigHit)
hit.grid(row=3, column=2)
stay = tkinter.Button(root, text="stay", command=no_moves)
stay.grid(row=4, column=2)


img = tkinter.PhotoImage(file="Try1.png")
panel = tkinter.Label(root, image=img)
panel.grid(row=3, column=1)
img1 = tkinter.PhotoImage(file="Try2.png")
panel1 = tkinter.Label(root, image=img)
panel1.grid(row=3, column=3)


user_total = tkinter.Label(root, text="Your total is:")
user_total.grid(row=5, column=1)
dealer_total = tkinter.Label(root, text="Dealer total is:")
dealer_total.grid(row=5, column=3)

KingUser = tkinter.Label(root, textvariable=UTotal)
KingUser.grid(row=6, column=1)
KingDealer = tkinter.Label(root, textvariable=Dtotal)
KingDealer.grid(row=6, column=3)


Final = tkinter.Label(root, textvariable=recognize)
Final.grid(row=7, column=2)


root.mainloop()
