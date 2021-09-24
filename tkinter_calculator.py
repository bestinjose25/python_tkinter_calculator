import parser
from tkinter import *
root=Tk()
# root.geometry("180x180")
root.title("Calculator")    # to show the title
root.config(bg="grey")
resultDisplay=Entry(root,bd=7)    #bd is border
resultDisplay.grid(row=1,columnspan=8,sticky=W+E) #sticky enthinannu ariyilaa


#getting user input and displaying in the text box ,(1 button is clicked then entry box should display 1)
i=0
def getValue(Number):
    global i
    resultDisplay.insert(i,Number) #insert is used for inserting particular value into the particular index value
    i+=1


def clearAll():
    resultDisplay.delete(0,END)

def clearSingle():
    entireString=resultDisplay.get()
    if len(entireString):
        newSting=entireString[:-1]   #eghne koduthal namku last term ozhike ullathu kittum(if,{2,3,5,6,7} then,{2,3,4,6} will be the output)
        clearAll()                 # to delete previous output
        resultDisplay.insert(0, newSting)  #
    else:
        clearAll()
        resultDisplay.insert(0, "error")


def getOperator(opera):
    global i
    length= len(opera)
    resultDisplay.insert(i,opera)
    i+=length

def calculate():
    entireString=resultDisplay.get()
    try:
        a = parser.expr(entireString).compile()
        resultAnswer = eval(a)
        clearAll()
        resultDisplay.insert(0, resultAnswer)
    except:
        clearAll()
        resultDisplay.insert(0,"operation not valid")


#button creating

button7=Button(root,text="7",padx=10,pady=5, command=lambda :getValue(7))
button7.grid(row=2,column=1)
button8=Button(root,text="8", padx=10,pady=5,command=lambda :getValue(8))
button8.grid(row=2,column=2)
button9=Button(root,text="9",padx=10,pady=5, command=lambda :getValue(9))
button9.grid(row=2,column=3)
button4=Button(root,text="4",padx=10,pady=5, command=lambda :getValue(4))
button4.grid(row=3,column=1)
button5=Button(root,text="5",padx=10,pady=5, command=lambda :getValue(5))
button5.grid(row=3,column=2)
button6=Button(root,text="6",padx=10,pady=5, command=lambda :getValue(6))
button6.grid(row=3,column=3)
button1=Button(root,text="1",padx=10,pady=5, command=lambda :getValue(1))
button1.grid(row=4,column=1)
button2=Button(root,text="2",padx=10,pady=5, command=lambda :getValue(2))
button2.grid(row=4,column=2)
button3=Button(root,text="3",padx=10,pady=5, command=lambda :getValue(3))
button3.grid(row=4,column=3)
button0=Button(root,text="0",padx=10,pady=5, command=lambda :getValue(0))
button0.grid(row=5,column=1)

# We can create button without saving into a variable that is below
Button(root,text="pi",padx=10,pady=5, command= lambda : getOperator('3.14')).grid(row=2,column=4)
Button(root,text=".",padx=12,pady=5, command= lambda : getOperator('.')).grid(row=2,column=5)
Button(root,text="(",padx=10,pady=5, command= lambda : getOperator('(')).grid(row=2,column=6)
Button(root,text=")",padx=10,pady=5, command= lambda : getOperator(')')).grid(row=2,column=7)
Button(root,text="+",padx=11,pady=5, command= lambda : getOperator('+')).grid(row=3,column=4)
Button(root,text="-",padx=11,pady=5, command= lambda : getOperator('-')).grid(row=3,column=5)
Button(root,text="exp",padx=3,pady=5, command= lambda : getOperator('**')).grid(row=3,column=6)
Button(root,text="!",padx=10,pady=5).grid(row=3,column=7)
Button(root,text="*",padx=12,pady=5, command= lambda : getOperator('*')).grid(row=4,column=4)
Button(root,text="/",padx=11,pady=5, command= lambda : getOperator('/')).grid(row=4,column=5)
Button(root,text="^2",padx=6,pady=4, command= lambda : getOperator('**2')).grid(row=4,column=6)
Button(root,text="%",padx=6,pady=5, command= lambda : getOperator('%')).grid(row=4,column=7)

Button(root,text="AC",padx=5,pady=5,bg="light green",command=lambda :clearAll(),bd=2).grid(row=5,column=2)
Button(root,text="<--",padx=5,pady=5,bg="light green",command= lambda : clearSingle(),bd=2).grid(row=5,column=3)
Button(root,text="=",padx=61,pady=5,command= lambda : calculate()).grid(row=5,column=4, columnspan=4)








root.mainloop()