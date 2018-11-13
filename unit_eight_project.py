import tkinter
import random


def draw_card():
    return random.randint(1, 10)




root = tkinter.Tk()
root.title("BlackJack")
Blackjack = tkinter.Label(root, text="BlackJack")
Blackjack.grid(row=1, column=2)
explanation = tkinter.Label(root, text="You will be given 2 cards on random and having an option to draw another card. "
                                       "You win if your cards are higher than the dealers and less than 21")
Ace = draw_card() + draw_card()
Joker = draw_card() + draw_card()


def no_move():
    user = int(UTotal.get())
    dealer = int(Dtotal())
    if user > dealer:
        recognize.set("User win")
    elif user < dealer:
        recognize.set("Dealer Win")
    elif user > 21:
        recognize.set("Dealer Win")
    elif user == dealer:
        recognize.set("Tie")


Dtotal = tkinter.StringVar()
UTotal = tkinter.StringVar()
recognize =tkinter.StringVar()
explanation.grid(row=2, column=2)
hit = tkinter.Button(root, text="hit")
hit.grid(row=3, column=2)
stay = tkinter.Button(root, text="stay", command=no_move)
stay.grid(row=4, column=2)
img = tkinter.PhotoImage(file="Try1.png")
panel = tkinter.Label(root, image=img)
panel.grid(row=3, column=1)
img1 = tkinter.PhotoImage(file="Try2.png")
panel1 = tkinter.Label(root, image=img)
panel1.grid(row=3, column=3)
user_total = tkinter.Label(root, text="Your total is:")
user_total.grid(row=5, column=1)
KingUser = tkinter.Label(root, text=Ace)
KingUser.grid(row=6, column=1)
KingDealer = tkinter.Label(root, text=Joker)
KingDealer.grid(row=6, column=3)
dealer_total = tkinter.Label(root, text="Dealer total is:")
dealer_total.grid(row=5, column=3)
Final_stay = tkinter.Label(root, textvariable=recognize)
Final_stay.grid(row=7, column=2)
# UserJamba = tkinter.Label(root, text=stay)
# UserJamba.grid(row=6, column=1)


root.mainloop()
