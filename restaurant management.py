import tkinter as tk                        #import
import time , random
import requests
import json
from tkinter.messagebox import showinfo, showerror
#https://www.tutorialspoint.com/python/python_gui_programming.htm
#https://www.youtube.com/watch?v=hqC9tioGCi0
#https://www.youtube.com/watch?v=uPaH6Lpa7eA
#https://www.youtube.com/watch?v=Bj3_-qmdjYk
operator=''
def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': '7pkjFqMPavrKScoyCJYWbstTB8591OlLwmDUQ26GxEedzHfi3ZQZJkDnl2sv7t0V36OayrjC9qwof8RP',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


def btn_send():
    num = textNumber.get()
    msg = textMsg.get("1.0",END)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


def btn_Send():
    root = tk.Tk()
    root.title("Message Sender ")
    root.geometry("400x550")

    global textNumber
    textNumber = tk.Entry(root,font=( "Helvetica", 22, "bold"))
    textNumber.grid(row=0,column=0)

    global textMsg
    textMsg = tk.Text(root)
    textMsg.grid(row=1,column=0)

    sendBtn = tk.Button(root, text="SEND SMS", command=btn_send)
    sendBtn.grid(row=3,column=0)

    root.mainloop()

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btncleardisplay():
    global operator
    operator=''
    text_Input.set('')

def btnequal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=''

def Exit():
    window.destroy()
def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Soda.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    CoDrinks= float(Drinks.get())
    CoFries = float(Fries.get())
    CoBurger= float(Burger.get())
    CoSoda= float(Soda.get())
    CoChicken_Burger=float(Chicken_Burger.get())
    CoCheese_Burger= float(Cheese_Burger.get())

    CostofDrinks= CoDrinks*50
    CostofFries = CoFries*25
    CostofBurger= CoBurger*75
    CostofSoda= CoSoda*15
    CostofChicken_Burger=CoChicken_Burger*110
    CostofCheese_Burger= CoCheese_Burger*100

    costOfMeal=CostofDrinks+CostofFries+CostofBurger+CostofSoda+CostofChicken_Burger+CostofCheese_Burger
    service="₹",str('%.2f'%(costOfMeal/99))
    taxPaid="₹",str('%.2f'%(costOfMeal*0.2))
    subTotal="₹",str('%.2f'%(costOfMeal))
    overAllCost="₹",str('%.2f'%(costOfMeal*(1+1/99+0.2)))

    Cost.set(costOfMeal)
    Service_Charge.set(service) 
    Tax.set(taxPaid)
    SubTotal.set(subTotal) 
    Total.set(overAllCost)

 
     

#create window
window = tk.Tk()                            #The second line initializes a Tk object, called window
window.title("Restaurant management system")                                          #sets a title for the window

#window.geometry("1600x800+0+0")               #sets the width and height of the window..
window.attributes("-fullscreen", True)

#create frame
f1=tk.Frame(window, height=50 , width =1600,bg="powder blue",relief='sunken')
f1.pack(side='top')

f2=tk.Frame(window, height=700 , width =800,relief='sunken')
f2.pack(side='left')

f3=tk.Frame(window, height=700 , width =300,relief='sunken')
f3.pack(side='right')

#Headings
label_info = tk.Label(f1,font=('arial',45,'bold'),text = " Restaurant Management System ",fg="Steel blue",bd=10,anchor='w')
label_info.grid(row=0,column=0)

localtime=time.asctime(time.localtime(time.time()))
label_info = tk.Label(f1,font=('arial',20,'bold'),text = localtime,fg="Steel blue",bd=10,anchor='w')
label_info.grid(row=1,column=0)

#calculator
text_Input = tk.StringVar()

txtDisplay = tk.Entry (f3,font=('arial',20,'bold'),textvariable = text_Input, bd=30,insertwidth=4,bg='powder blue', justify = 'right').grid(columnspan=4)

btn7 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
btnadd = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
btn4 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
btnsubtract = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick("-")).grid(row=2,column=3)
btn1 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
btnmulti = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*")).grid(row=3,column=3)
btn0 = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick("0")).grid(row=4,column=0)
btnclear = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'), command=btncleardisplay,text="C").grid(row=4,column=1)
btnequals = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="=",command=btnequal).grid(row=4,column=2)
btndivision = tk.Button (f3, padx = 16, bd = 8, fg ="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/")).grid(row=4,column=3)

#menu section
rand = tk.StringVar()

Fries = tk.StringVar()
Burger= tk.StringVar()
Soda= tk.StringVar()
Chicken_Burger= tk.StringVar()
Cheese_Burger= tk.StringVar()
Drinks= tk.StringVar()

SubTotal= tk.StringVar()
Total= tk.StringVar()
Service_Charge= tk.StringVar()
Tax= tk.StringVar()
Cost= tk.StringVar()


label_Drinks = tk.Label(f2,font=('arial',16,'bold'),text = " Drinks",bd=16,anchor='w').grid(row=0,column=0)
text_Drinks= tk.Entry(f2,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=0,column=1)

label_fries = tk.Label(f2,font=('arial',16,'bold'),text = " Fries",bd=16,anchor='w').grid(row=1,column=0)
text_fries = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=1,column=1)

label_Burger = tk.Label(f2,font=('arial',16,'bold'),text = " Burger",bd=16,anchor='w').grid(row=2,column=0)
text_Burger = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=2,column=1)

label_Soda = tk.Label(f2,font=('arial',16,'bold'),text = " Soda",bd=16,anchor='w').grid(row=3,column=0)
text_Soda = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Soda,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=3,column=1)

label_Chicken_Burger = tk.Label(f2,font=('arial',16,'bold'),text = " Chicken_Burger",bd=16,anchor='w').grid(row=4,column=0)
text_Chicken_Burger = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Chicken_Burger,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=4,column=1)

label_Cheese_Burger = tk.Label(f2,font=('arial',16,'bold'),text = " Cheese_Burger ",bd=16,anchor='w').grid(row=5,column=0)
text_Cheese_Burger = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Cheese_Burger,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=5,column=1)

label_reference = tk.Label(f2,font=('arial',16,'bold'),text = " reference",bd=16,anchor='w').grid(row=0,column=2)
text_reference = tk.Entry(f2,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=0,column=3)

label_Service_Charge = tk.Label(f2,font=('arial',16,'bold'),text = " Service_Charge",bd=16,anchor='w').grid(row=1,column=2)
text_Service_Charge = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=1,column=3)

label_Tax = tk.Label(f2,font=('arial',16,'bold'),text = " Tax",bd=16,anchor='w').grid(row=2,column=2)
text_Tax = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=2,column=3)

label_Cost = tk.Label(f2,font=('arial',16,'bold'),text = " Cost",bd=16,anchor='w').grid(row=3,column=2)
text_Cost = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=3,column=3)

label_SubTotal = tk.Label(f2,font=('arial',16,'bold'),text = "SubTotal",bd=16,anchor='w').grid(row=4,column=2)
text_SubTotal = tk.Entry(f2,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=4,column=3)

label_Total = tk.Label(f2,font=('arial',16,'bold'),text = "Total",bd=16,anchor='w').grid(row=5,column=2)
text_Total = tk.Entry(f2,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right').grid(row=5,column=3)


btnTotal=tk.Button(f2,padx=10,pady=8,fg="black",font=('arial',16,'bold'),text = " Total",bd=16,width=10,bg="powder blue",command=Ref).grid(row=6,column=0)
btnReset=tk.Button(f2,padx=10,pady=8,fg="black",font=('arial',16,'bold'),text = " Reset",bd=16,width=10,bg="powder blue",command=Reset).grid(row=6,column=1)
btnExit=tk.Button(f2,padx=10,pady=8,fg="black",font=('arial',16,'bold'),text = " Exit",bd=16,width=10,bg="powder blue",command=Exit).grid(row=6,column=2)
btnsend=tk.Button(f2,padx=10,pady=8,fg="black",font=('arial',16,'bold'),text = " Send",bd=16,width=10,bg="powder blue",command=btn_Send).grid(row=6,column=3)






window.mainloop()                           #creates the whole window to execute. 
""" 
The basic syntax of widgets is:

tk.Widget_name(parent,options)  

The basic widgets in Tkinter are frames, labels, buttons, check buttons, radio buttons, entries, and combo boxes. """




"""
#window at centre
win.resizable(False, False)  # This code helps to disable windows from resizing
window_height = 500
window_width = 900
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


 #create label
mylabel = tk.Label(text = "Press to ring doorbell ")  #A label is a class in Tkinter which is used to display text or image.
mylabel.grid(column=0,row=0)                #A grid is used to label at a position using row and column values


#create button
mybutton = tk.Button(window, text = "doorbell")     #window as the first argument of the Button method, to connect the button to our window.
mybutton.grid(column=1,row=0)
# In order to make the button work, we need to handle events (like clicking a button).
#The second thing is we need to bind the button to the event.
def doorbell(event):
    print(" You rang the Doorbell !")
mybutton.bind("<Button-1>",doorbell)            #<Button-1> is the left click short key of the mouse
 """













#Convert .py to exe
#pip install pyinstaller
#pyinstaller -F -w  file_name.py 

#add icon to exe
#pyinstaller -F -w -i  icon_name.ico  file_name.py  