import tkinter

window  = tkinter.Tk()
window.title(" My GUI Program ")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#Label
my_label = tkinter.Label(text="Super Dooper Doo.", font=("Arial", 12))
my_label.grid(row=0, column=0)

def buttonClicked():
    my_label["text"] = my_input.get()
    print("I Got Clicked")

#Button
my_btn = tkinter.Button(text="Super dhan ba", command=buttonClicked)
my_btn.grid(row=1, column=1)

#Button2
my_btn2 = tkinter.Button(text="Super dhan ba 2", command=buttonClicked)
my_btn2.grid(row=0, column=2)

#Input
my_input = tkinter.Entry(width=10)
my_input.grid(row=4, column=4)
print(my_input.get())

window.mainloop()