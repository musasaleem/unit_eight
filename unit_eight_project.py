import tkinter

root = tkinter.Tk()
root.title("BlackJack")
Blackjack = tkinter.Label(root, text="BlackJack")
Blackjack.grid(row=1, column=1)
explanation = tkinter.Label(root, text="You will be given 2 cards on random and having an option to draw another card. "
                                       "You win if your cards are higher than the dealers and less than 21")
explanation.grid(row=2, column=1)
hit = tkinter.Button(root, text="hit")
hit.grid(row=3, column=1)
stay = tkinter.Button(root, text="stay")
stay.grid(row=4, column=1)
root.mainloop()
