from Tkinter import *
import math
import tkFont

def closeApp(): 
    app.quit()



#total = loan * (interest/(1-(1+interest) ** (-term)))

def calculateLabel(*args):
    if payment.get() != "" and payoffTime.get() == "":
        loan = float(balance.get())
        yearlyinterest = float(interestRate.get())
        interest = (yearlyinterest/100)/12
        payments = float(payment.get())
        if payments < (interest*loan) + (.01*loan):
            minimumpayment = (interest*loan) + (.01*loan)
            labelText.set("Enter a valid payment")
            labelText2.set("Minimum payment: " + str(minimumpayment))
        else:
            total = -math.log(1-interest*loan/payments)/ math.log(1+interest)
            total = math.ceil(total)
            total = int(total)
            minimumpayment = (interest*loan) + (.01*loan)
            labelText.set("Debt free in " + str(total) + " months.")
            labelText2.set("Minimum payment: " + str(minimumpayment))
    elif payoffTime.get() != "" and payment.get() == "":
        yearlyinterest = float(interestRate.get())
        interest = (yearlyinterest/100)/12
        loan = float(balance.get())
        time = int(payoffTime.get())
        total = (interest*loan)/(1-(1+interest)**-time)
        total = round(total,2)
        minimumpayment = (interest*loan) + (.01*loan)
        labelText.set(str(total) + " monthly payment")
        labelText2.set("Minimum payment: " + str(minimumpayment))
    elif payoffTime.get() == "" and payment.get() == "" or payoffTime.get() != "" and payment.get() != "":
        labelText.set("Please enter a value for Desired Payoff Date or Monthly Payment ")

app = Tk()
app.title("CC Repayment Calculator")
app.geometry('500x200+200+200')
app.bind("<Return>",calculateLabel)

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Quit",command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)

label2 = Label(app, text='CC Balance')
label2.grid(row=1)

balance = IntVar()
balance.set("")
balance = Entry(app, textvariable=balance)
balance.focus_set()
balance.grid(row=1, column=1)


label3 = Label(app, text='Interest Rate')
label3.grid(row=2)

interestRate = IntVar()
interestRate.set("")
interestRate = Entry(app, textvariable=interestRate)
interestRate.grid(row=2, column=1)

label4 = Label(app, text='Monthly payment')
label4.grid(row=3)

payment = IntVar()
payment.set("")
payment = Entry(app, textvariable=payment)
payment.grid(row=3, column=1)

label5 = Label(app, text='Desired Payoff Date')
label5.grid(row=4)

payoffTime = IntVar()
payoffTime.set("")
payoffTime = Entry(app, textvariable=payoffTime)
payoffTime.grid(row=4, column=1)

frame1 = Frame(app,width=180,height=75)

labelText = StringVar()
labelText2 = StringVar()
labelText.set("")
labelText2.set("")
label1 = Label(frame1, textvariable=labelText,font=('bold'),fg='red')
label6 = Label(frame1, textvariable=labelText2,font=('bold'),fg='green')
frame1.grid_propagate(0)
label1.grid(row=1,column=0)
label6.grid(row=2,column=0)
frame1.grid(row=6,column=0)

calculateButton = Button(app, text="Click to calculate", width=20, command=calculateLabel)
calculateButton.grid(row=10,column=2)

closeButton = Button(app, text="Close", width=20, command=closeApp)
closeButton.grid(row=10,column=1)

app.config(menu=menubar)

app.mainloop()
