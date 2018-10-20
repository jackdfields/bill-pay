from tkinter import *
from tkinter import ttk, Canvas
from tkinter import font



class AccountScreen(Frame):
        def __init__(self, parent, *args, **kwargs):
            # Main Frame
            Frame.__init__(self, parent, bg="red")
            self.welcome_msg = "Enter in your Account Number"

            self.account_num = "account number"
            self.error_msg = "ERROR MESSAGE HERE"

            # Account Info Frame
            self.account_frame = Frame(self, bg = "yellow")
            self.account_frame.pack(side=TOP, pady=50)
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
            self.G_frame = Frame(self)

            self.filler_frame=Frame(self.G_frame)
            self.filler_frame.grid(row = 0 , column=0)
            self.filler_frame1=Frame(self.G_frame)
            self.filler_frame1.grid(row = 0 , column=1)
            self.filler_frame2=Frame(self.G_frame)
            self.filler_frame2.grid(row = 0 , column=2)
            
            self.G_frame.pack()
            
            
            # Account Info Label
            self.accountLbl = Label(self.filler_frame1, font=(
                'Lucida Sans', 20), fg= "#b5c0d1", bg = 'white', text = self.account_num, width=50, height=2)
            self.accountLbl.pack(side = TOP, pady=30, padx=100)
            
class KeyBoard(Frame):
    """Layout touch screen keyboard"""
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='#BDCBEF')
        self.KeyFrame = Frame(self, bg="#BDCBEF")

        # 3 columns of keyboard 
        self.k_row1=Frame(self.KeyFrame)
        self.k_row1.grid(row = 1 , column=0)
        self.k_row2=Frame(self.KeyFrame)
        self.k_row2.grid(row = 2 , column=0)
        self.k_row3=Frame(self.KeyFrame)
        self.k_row3.grid(row = 3 , column=0)
        
        # command portion - if button pressed - Q is passed in
        self.Blank_button = Button(self.k_row1, text = ' ', font=(
             'Lucida Sans', 26),  fg="black", bg = '#BDCBEF', width=4, borderwidth=0, relief="flat")
        self.Q_button = Button(self.k_row1, text = 'Q', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('Q')).grid(row=0, column=1)
        self.W_button = Button(self.k_row1, text = 'W', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('W')).grid(row=0, column=2)
        self.E_button = Button(self.k_row1, text = 'E', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('E')).grid(row=0, column=3)
        self.R_button = Button(self.k_row1, text = 'R', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('R')).grid(row=0, column=4)
        self.T_button = Button(self.k_row1, text = 'T', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('T')).grid(row=0, column=5)
        self.Y_button = Button(self.k_row1, text = 'Y', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('Y')).grid(row=0, column=6)
        self.U_button = Button(self.k_row1, text = 'U', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('U')).grid(row=0, column=7)
        self.I_button = Button(self.k_row1, text = 'I', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('I')).grid(row=0, column=8)
        self.O_button = Button(self.k_row1, text = 'O', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('O')).grid(row=0, column=9)
        self.P_button = Button(self.k_row1, text = 'P', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('P')).grid(row=0, column=10)
        
        # Second row of keyboard
        self.A_button = Button(self.k_row2, text = 'A', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('A')).grid(row=0, column=1)
        self.S_button = Button(self.k_row2, text = 'S', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('S')).grid(row=0, column=2)
        self.D_button = Button(self.k_row2, text = 'D', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('D')).grid(row=0, column=3)
        self.F_button = Button(self.k_row2, text = 'F', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('F')).grid(row=0, column=4)
        self.G_button = Button(self.k_row2, text = 'G', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('G')).grid(row=0, column=5)
        self.H_button = Button(self.k_row2, text = 'H', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('H')).grid(row=0, column=6)
        self.J_button = Button(self.k_row2, text = 'J', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('J')).grid(row=0, column=7)
        self.K_button = Button(self.k_row2, text = 'K', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('K')).grid(row=0, column=8)
        self.L_button = Button(self.k_row2, text = 'L', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('L')).grid(row=0, column=9)

        # Third row of keyboard
        self.Z_button = Button(self.k_row3, text = 'Z', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('Z')).grid(row=0, column=1)
        self.X_button = Button(self.k_row3, text = 'X', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('X')).grid(row=0, column=2)
        self.C_button = Button(self.k_row3, text = 'C', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('C')).grid(row=0, column=3)
        self.V_button = Button(self.k_row3, text = 'V', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('V')).grid(row=0, column=4)
        self.B_button = Button(self.k_row3, text = 'B', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('B')).grid(row=0, column=5)
        self.N_button = Button(self.k_row3, text = 'N', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('N')).grid(row=0, column=6)
        self.M_button = Button(self.k_row3, text = 'M', font=(
             'Lucida Sans', 26),  fg="black", bg = 'white', width=4, command=lambda: self.button_press('M')).grid(row=0, column=7)

        self.KeyFrame.pack(pady=100)

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
        self.key_page = KeyBoard(self.root)
        self.key_page.pack(side=TOP, pady=100)


    def toggle_fullscreen(self, event = None):
        self.state = not self.state  # toggle for fullscreen and not full
        self.root.attributes("-fullscreen", self.state)


if __name__ == '__main__':
    # Run app until exited
    payer = PayScreen()
    payer.root.mainloop()