from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pandas as pd
import numpy as np

class BankApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Application")
        self.root.geometry("500x500+200+200")
        self.userpassword = {}
        self.history = {}
        self.login()

    # login and signup page
    def login(self):
        self.login_frame = Frame(self.root)
        self.login_frame.pack()

        self.label = Label(self.login_frame, text="Welcome to Yash Bank", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, pady=10)
        self.user_label = Label(self.login_frame, text="Account Number:")
        self.user_label.grid(row=1, column=0, padx=5, pady=5)
        self.user_entry = Entry(self.login_frame)
        self.user_entry.grid(row=1, column=1, padx=5, pady=5)
        self.password_label = Label(self.login_frame, text="Password:")
        self.password_label.grid(row=2, column=0, padx=5, pady=5)
        self.password_entry = Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)
        self.login_button = Button(self.login_frame, text="Login", command=self.login_b)
        self.login_button.grid(row=3, column=1, padx=5, pady=10)
        self.signup_button = Button(self.login_frame, text="Signup", command=self.signup)
        self.signup_button.grid(row=3, column=0, padx=5, pady=10)

    def login_b(self):
        for x,y in self.userpassword.items():
            if self.user_entry.get()==x and self.password_entry.get()==y:
                self.workpage()
            else:
                messagebox.askretrycancel('error','invelid account number or password')

    def signup(self):
        self.login_frame.pack_forget()
        self.signupframe = Frame(self.root)
        self.signupframe.pack()

        self.FN = Label(self.signupframe, text="First name").grid(row=2, column=0)
        self.SN = Label(self.signupframe, text="Surname").grid(row=3, column=0)
        self.DOB = Label(self.signupframe, text="Date of birth").grid(row=4, column=0)
        self.PN = Label(self.signupframe, text="Phone number").grid(row=5, column=0)
        self.G = Label(self.signupframe, text="Gender").grid(row=6, column=0)
        self.CN = Label(self.signupframe, text="Account Number").grid(row=7, column=0)
        self.NP = Label(self.signupframe, text="Password").grid(row=8, column=0)
        self.REP = Label(self.signupframe, text="Re-enter password").grid(row=9, column=0)
        self.EN_e = Entry(self.signupframe)
        self.EN_e.grid(row=2, column=1)
        self.SN_e = Entry(self.signupframe)
        self.SN_e.grid(row=3, column=1)
        self.DOB_e = Entry(self.signupframe)
        self.DOB_e.grid(row=4, column=1)
        self.PN_e = Entry(self.signupframe)
        self.PN_e.grid(row=5, column=1)
        n = StringVar()
        self.G_e = Combobox(self.signupframe, width=10, textvariable=n)
        self.G_e["values"] = ('male', 'female', 'other')
        self.G_e.grid(row=6, column=1)
        self.G_e.current(0)
        self.AN_e = Entry(self.signupframe)
        self.AN_e.grid(row=7, column=1)
        self.NP_e = Entry(self.signupframe, show="*")
        self.NP_e.grid(row=8, column=1)
        self.REP_e = Entry(self.signupframe)
        self.REP_e.grid(row=9, column=1)
        self.submit_b = Button(self.signupframe, text="Submit", command=self.save_data)
        self.submit_b.grid(row=10, column=1, padx=5, pady=10)

    def save_data(self):
        account_number = self.AN_e.get()
        password = self.NP_e.get()
        self.userpassword[account_number] = password
        self.signupframe.pack_forget()
        self.login()

    # work page
    def workpage(self):
        self.login_frame.pack_forget()
        self.work_frame = Frame(root)
        self.work_frame.pack(pady=10)

        self.money_tran = Label(self.work_frame, text="Money transaction", font=("Helvetica", 16))
        self.money_tran.grid(row=0, column=0, padx=5, pady=5)
        self.deposit = Button(self.work_frame, text="Deposit", command=self.depositpage)
        self.deposit.grid(row=1, column=0, padx=5, pady=5)
        self.withdrawal = Button(self.work_frame, text="Withdrawal", command=self.withdrawalpage)
        self.withdrawal.grid(row=1, column=1, padx=5, pady=5)
        self.send_money = Button(self.work_frame, text="Send Money", command=self.sendmoneypage)
        self.send_money.grid(row=2, column=0, padx=5, pady=5)
        self.loan = Button(self.work_frame, text="Loan")
        self.loan.grid(row=2, column=1, padx=5, pady=5)
        self.transaction_history = Button(self.work_frame, text="Transaction History")
        self.transaction_history.grid(row=3, column=0, padx=5, pady=5)

    # deposit page
    def depositpage(self):
        self.work_frame.pack_forget()
        self.deposit_frame = Frame(root)
        self.deposit_frame.pack(pady=10)

        self.deposit_l = Label(self.deposit_frame, text="Deposit", font=("Helvetica", 16))
        self.deposit_l.grid(row=0, column=1, padx=5, pady=5)
        self.deposit_amount = Label(self.deposit_frame, text='Deposit Amount')
        self.deposit_amount.grid(row=1, column=0, padx=5, pady=5)
        self.deposit_amount_e = Entry(self.deposit_frame)
        self.deposit_amount_e.grid(row=1, column=1, padx=5, pady=5)
        self.password_number = Label(self.deposit_frame, text='Password')
        self.password_number.grid(row=2, column=0, padx=5, pady=5)
        self.password_number_e = Entry(self.deposit_frame, show="*")
        self.password_number_e.grid(row=2, column=1, padx=5, pady=5)
        self.deposit_b = Button(self.deposit_frame, text="Deposit", command=self.deposit)
        self.deposit_b.grid(row=3, column=1, padx=5, pady=5)
        self.back_b = Button(self.deposit_frame, text="Back", command=self.backdeposit)
        self.back_b.grid(row=0, column=0, padx=5, pady=5)

    def backdeposit(self):
        self.deposit_frame.pack_forget()
        self.work_frame.pack()

    # deposit
    def deposit(self):
        pass

    # withdrawal page
    def withdrawalpage(self):
        self.work_frame.pack_forget()
        self.withdrawal_frame = Frame(root)
        self.withdrawal_frame.pack(pady=10)

        self.withdrawal_l = Label(self.withdrawal_frame, text="Withdrawal", font=("Helvetica", 16))
        self.withdrawal_l.grid(row=0, column=1, padx=5, pady=5)
        self.withdrawal_amount = Label(self.withdrawal_frame, text='Withdrawal Amount')
        self.withdrawal_amount.grid(row=1, column=0, padx=5, pady=5)
        self.withdrawal_amount_e = Entry(self.withdrawal_frame)
        self.withdrawal_amount_e.grid(row=1, column=1, padx=5, pady=5)
        self.password_number = Label(self.withdrawal_frame, text='Password')
        self.password_number.grid(row=2, column=0, padx=5, pady=5)
        self.password_number_e = Entry(self.withdrawal_frame, show="*")
        self.password_number_e.grid(row=2, column=1, padx=5, pady=5)
        self.withdrawal_b = Button(self.withdrawal_frame, text="Withdrawal", command=self.withdrawal)
        self.withdrawal_b.grid(row=3, column=1, padx=5, pady=5)
        self.back_b = Button(self.withdrawal_frame, text="Back", command=self.backwithdrawal)
        self.back_b.grid(row=0, column=0, padx=5, pady=5)

    def backwithdrawal(self):
        self.withdrawal_frame.pack_forget()
        self.work_frame.pack()

    # withdrawal
    def withdrawal(self):
        pass

    # send Money page
    def sendmoneypage(self):
        self.work_frame.pack_forget()
        self.sendmoney_frame = Frame(root)
        self.sendmoney_frame.pack(pady=10)
        self.sendmoney_l = Label(self.sendmoney_frame, text="Send Money", font=("Helvetica", 16))
        self.sendmoney_l.grid(row=0, column=1, padx=5, pady=5)
        self.by_phone = Button(self.sendmoney_frame, text="Phone Number")
        self.by_phone.grid(row=1, column=0, padx=5, pady=5)
        self.by_upiid = Button(self.sendmoney_frame, text="UPI Id")
        self.by_upiid.grid(row=1, column=1, padx=5, pady=5)
        self.by_account = Button(self.sendmoney_frame, text="Account")
        self.by_account.grid(row=2, column=0, padx=5, pady=5)
        self.back_b = Button(self.sendmoney_frame, text="Back", command=self.backsendmoney)
        self.back_b.grid(row=0, column=0, padx=5, pady=5)

    def backsendmoney(self):
        self.sendmoney_frame.pack_forget()
        self.work_frame.pack()

    # loan page

    # transaction history

root = Tk()
app = BankApplication(root)
root.mainloop()
