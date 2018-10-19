from tkinter import *
from tkinter import ttk, Canvas
from tkinter import font



class AccountScreen(Frame):
        def __init__(self, parent, *args, **kwargs):
            # Main Frame
            Frame.__init__(self, parent, bg="red")
            self.welcome_msg = "Enter in your Account Number"

            self.canvas=Canvas()

            self.account_num = "account number"
            self.error_msg = "ERROR MESSAGE HERE"

            # Account Info Frame
            self.account_frame = Frame(self, bg = "yellow")
            self.account_frame.pack(side=TOP, pady=10)
            # Welcome Message
            self.welcomeLbl = Label(self.account_frame, font=(
                'Lucida Sans', 40),
                fg = "black", bg='#BDCBEF', text=self.welcome_msg)
            self.welcomeLbl.pack(side=TOP)
            # Error Message that will be triggered
            self.errorLbl = Label(self.account_frame, font=(
                'Lucida Sans', 20),
                fg = "RED", bg='#BDCBEF', text=self.error_msg)
            self.errorLbl.pack(side=TOP)
            # Account Info Label
            self.accountLbl = Label(self.account_frame, font=(
                'Lucida Sans', 20), fg= "#b5c0d1", bg = 'white', text = self.account_num)
            self.accountLbl.pack(side = TOP, pady=20)


            self.KeyFrame = Frame(self, bg="black")
           
            

class PayScreen:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background='#BDCBEF')
        
        # Set window bounds
        self.root.geometry("500x300")

        # state of fullscreen
        self.state = True

        # change state of fullscreen by calling function - start with fullscreen
        self.root.attributes("-fullscreen", self.state)
        self.root.bind("<F6>", self.toggle_fullscreen)
        
        self.account_page = AccountScreen(self.root)
        self.account_page.pack(side=TOP)

    def toggle_fullscreen(self, event = None):
        self.state = not self.state  # toggle for fullscreen and not full
        self.root.attributes("-fullscreen", self.state)


if __name__ == '__main__':
    # Run app until exited
    payer = PayScreen()
    payer.root.mainloop()