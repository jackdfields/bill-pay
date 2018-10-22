from tkinter import *
from tkinter import ttk, Canvas
from tkinter import font



class AccountScreen(Frame):

    def select_it(self, value):
        self.account_num.set(value)
        print(self.account_num.get())
        
    
    def __init__(self, parent, *args, **kwargs):
        # Main Frame
        Frame.__init__(self, parent, bg="#BDCBEF")

        self.welcome_msg = "Enter in your Account Number"
        self.error_msg = "ERROR MESSAGE HERE"
        self.account_num = StringVar(value="account number")

        # Account Info Frame
        self.account_frame = Frame(self, bg = "black")
        self.account_frame.pack(side=TOP, pady=50)
        # Keyboard Frame
        self.KeyFrame = Frame(self, bg="#BDCBEF")
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

        #----GRID----#
        self.G_frame = Frame(self, bg='#BDCBEF')

        self.filler_frame=Frame(self.G_frame)
        self.filler_frame.grid(row = 0 , column=0)
        self.filler_frame1=Frame(self.G_frame,  bg='#BDCBEF')
        self.filler_frame1.grid(row = 0 , column=1)
        self.filler_frame2=Frame(self.G_frame)
        self.filler_frame2.grid(row = 0 , column=2)
            
        self.G_frame.pack()
            
            
        # Account Info Label
        # use text variable as it will help change the writing of the text rather than an obj name
        self.accountLbl = Label(self.filler_frame1, font=(
            'Lucida Sans', 20), fg= "#b5c0d1", bg = 'white', textvariable = self.account_num, width=50, height=2)
        self.accountLbl.pack(side = TOP, pady=30, padx=100)

        # 3 columns of keyboard 
        self.k_row1=Frame(self.KeyFrame)
        self.k_row1.grid(row = 1 , column=0)
        self.k_row2=Frame(self.KeyFrame)
        self.k_row2.grid(row = 2 , column=0)
        self.k_row3=Frame(self.KeyFrame)
        self.k_row3.grid(row = 3 , column=0)
                
        # First Row of Keybaord
        buttons_r1 = ['Q','W','E','R','T','Y','U','I','O','P']

        for button in buttons_r1:
            command = lambda x=button: self.select_it(x)
            Button(self.k_row1, text = button, width = 4,  font=(
                'Lucida Sans', 26),  fg="black", bg = 'white', command=command).grid(row=0, column = buttons_r1.index(button))
            
        # Second row of keyboard
        buttons_r2 = ['A','S','D','F','G','H','J','K','L']

        for button in buttons_r2:
            command = lambda x=button: self.select_it(x)
            Button(self.k_row2, text = button, width = 4,  font=(
                'Lucida Sans', 26),  fg="black", bg = 'white', command=command).grid(row=0, column = buttons_r2.index(button))

            # Third row of keyboard
            buttons_r3 = ['Z','X','C','V','B','N','M']

        for button in buttons_r3:
            command = lambda x=button: self.select_it(x)
            Button(self.k_row3, text = button, width = 4, font=(
                'Lucida Sans', 26), fg="black", bg="white", command=command).grid(row = 0, column = buttons_r3.index(button))
                
        self.KeyFrame.pack(side=BOTTOM, pady=150)
 
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
        self.account_page.pack(side=TOP, pady=50)

    def toggle_fullscreen(self, event = None):
        self.state = not self.state  # toggle for fullscreen and not full
        self.root.attributes("-fullscreen", self.state)


if __name__ == '__main__':
    # Run app until exited
    payer = PayScreen()
    payer.root.mainloop()