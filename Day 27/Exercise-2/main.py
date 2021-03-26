from tkinter import Entry,Tk,Label,Button

window = Tk()
window.title(" Mile to Km Converter ")
window.config(padx=15, pady=15)

#Input
inputMiles = Entry(width=10)
inputMiles.grid(row=0, column=1)

#text1
unit1Text =  Label(text="Miles")
unit1Text.grid(row=0, column=2)

#text2
isEqualto = Label(text="is Equal to")
isEqualto.grid(row=1, column=0)

#result
resultLabel = Label(text="0")
resultLabel.grid(row=1, column=1)

#text1
unit1Text =  Label(text="Km")
unit1Text.grid(row=1, column=2)

def calckm():
    miles = int(inputMiles.get())
    km = round(miles * 1.6, 2)
    resultLabel["text"] = f"{km}"

#button
resultBtn = Button(text="Calculate", command=calckm)
resultBtn.grid(row=2,column=1)

window.mainloop()