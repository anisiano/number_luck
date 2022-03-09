from tkinter import *
from random import sample
from tkinter import Label

window = Tk()

img = PhotoImage(file= "numbers.png")

imglabel = Label(window, image=img)

label1 = Label(window , relief = "groove", width = 2 )
label2 = Label(window , relief = "groove", width = 2 )
label3 = Label(window , relief = "groove", width = 2 )
label4 = Label(window , relief = "groove", width = 2 )
label5 = Label(window , relief = "groove", width = 2 )
label6 = Label(window , relief = "groove", width = 2 )

getbtn = Button(window)

restbtn = Button(window)

imglabel.grid()
label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getbtn.grid()
restbtn.grid()

imglabel.grid(row = 1, column = 1, padx = 10)
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = 10)
getbtn.grid(row = 2, column = 2, columnspan = 4)
restbtn.grid(row= 2, column = 6, columnspan = 2)

window.title(" Maded By XxTwiniTwinixX")
def reset():

 label1.configure(text= "...")
label2.configure(text= "...")
label3.configure(text= "...")
label4.configure(text= "...")
label5.configure(text= "...")
label6.configure(text= "...")
getbtn.configure(text= "Get My Lucky Number")
restbtn.configure(text="REAST")
def GET_number():
    nums = sample(range(0, 100), 6)



    label1.configure(text= nums[0])
    label2.configure(text= nums[1])
    label3.configure(text= nums[2])
    label4.configure(text= nums[3])
    label5.configure(text= nums[4])
    label6.configure(text= nums[5])
    getbtn.configure(state = DISABLED)
    restbtn.configure(state = NORMAL)

    getbtn.configure(state=NORMAL)
    restbtn.configure(state=DISABLED)
    getbtn.configure(commend = GET_number())
    restbtn.configure(commend = reset())
    window.resizable(0,0)









window.mainloop()
