try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
    
master = Tk()


click = 0
mult = 1
dcp1 = 0
autoclickers = 0

def purchaseDoubleClicksCommand():
    global click
    global mult
    if click >= 50:
        mult += 1
        click = click - 50


def purchaseAutoClickerCommand():
    global click
    global autoclickers
    if click >= 30:
        autoclickers += 1  # add an autoclicker
        click = click - 30


def autoclick():
    global master
    global click
    global autoclickers
    click += autoclickers  # get clicks from autoclickers
    master.after(1000, autoclick)  # do this again 1 second later


def text_upd():
    global master
    global click
    global mult
    global autoclickers

    clicks_text['text'] = "clicks: " + str(click)
    mult_text['text'] = "clicks multiplicator: " + str(mult)
    auto_text['text'] = "autocklicks per second: " + str(autoclickers)

    master.after(50, text_upd)


def buttonCommand():
    global click
    global mult
    click += 1*(mult)


click_button = Button(master,
                      text="Click",
                      bg='#3b83bd',
                      activebackground='#007ba7',
                      borderwidth=5,
                      command=buttonCommand,
                      font=("Fixedsys", 20))

click_button.place(x=100, y=50, anchor=NW)

purchaseDoubleClickButton = Button(master,
                                   text="Purchase Double Clicks",
                                   bg='#3b83bd',
                                   activebackground='#007ba7',
                                   borderwidth=5,
                                   command=purchaseDoubleClicksCommand,
                                   font=("Fixedsys", 20))
purchaseDoubleClickButton.place(x=100, y=150, anchor=NW)

purchaseAutoClickerButton = Button(master,
                                   bg='#3b83bd',
                                   activebackground='#007ba7',
                                   borderwidth=5,
                                   text="Purchase Auto Clicker",
                                   command=purchaseAutoClickerCommand,
                                   font=("Fixedsys", 20))
purchaseAutoClickerButton.place(x=100, y=250, anchor=NW)

master.title("Clicker v1.0.4")

master.minsize(1200, 625)
master.geometry("1200x625")
master.resizable(0, 0)

clicks_text = Label(master,
                    text="clicks: " + str(click),
                    font=("Fixedsys", 25),
                    anchor=NW
                    )

clicks_text.place(x=500, y=50, anchor=NW)

mult_text = Label(master,
                  text="clicks multiplicator: " + str(mult),
                  font=("Fixedsys", 25),
                  anchor=NW
                  )

mult_text.place(x=500, y=150, anchor=NW)

auto_text = Label(master,
                  text="autoclicks per second: " + str(autoclickers),
                  font=("Fixedsys", 25),
                  anchor=NW
                  )

auto_text.place(x=500, y=250, anchor=NW)

mult_price_text = Label(master,
                        text="2x multiplication price = 50",
                        font=("Fixedsys", 25),
                        anchor=NW
                        )

mult_price_text.place(x=100, y=350, anchor=NW)

auto_price_text = Label(master,
                        text="autoclickers price = 30",
                        font=("Fixedsys", 25),
                        anchor=NW
                        )

auto_price_text.place(x=100, y=450, anchor=NW)



exit_button = Button(master,
                     bg='#808080',
                     activebackground='#818181',
                     borderwidth=5,
                     font=("Fixedsys", 20),
                     text='EXIT',
                     command=master.destroy
)

exit_button.place(x=920, y=500, anchor=NW)

autoclick()
text_upd()

mainloop()
