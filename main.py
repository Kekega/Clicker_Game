try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from Kappa_class import Click_Kappa


def autoclick():

    """Updates current_clicks every second"""

    gui.total_clicks += gui.auto_click
    gui.current_clicks += gui.auto_click
    gui.current_clicks_variable.set(gui.current_clicks)

    master.after(1000, autoclick)


def update_gui():

    """Updates gui every 0.05 sec"""
    column_num = 0
    for name in gui.names:
        if gui.current_clicks >= getattr(gui, name + '_price'):
            getattr(gui, name + '_button').place(x=582, y=7+65*column_num)
        else:
            getattr(gui, name + '_button').place_forget()
        column_num += 1

    if gui.current_clicks > gui.one_click_price:
        gui.one_click_button.place(x=744, y=472)
    else:
        gui.one_click_button.place_forget()

    master.after(50, update_gui)


master = Tk()
# Setting the window
master.minsize(1200, 625)
master.geometry("1200x625")
master.resizable(0, 0)

gui = Click_Kappa(master)

# Updating
autoclick()
update_gui()

# Main loop
master.mainloop()
