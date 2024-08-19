from tkinter import *
from tkinter import ttk
from random import randrange

#lango sukurimo funkcija
class DiceRoller: 
    def __init__(self, kauliukas):
        self.kauliukas = kauliukas
        self.kauliukas.geometry("750x250")
        self.kauliukas.title("Welcome to the Dice Roller. May the odds be ever in your favor")

        self.result_label = Label(self.kauliukas, text="", font=("Comic Sans", 16))
        self.result_label.pack(pady=100)

        self.create_buttons()
    #mygtuku kurimo funkcija
    def create_buttons(self):
        Button(self.kauliukas, text="Die 4", command=self.click_d4, font=("Comic Sans", 20)).place(x=30, y=30)
        Button(self.kauliukas, text="Die 6", command=self.click_d6, font=("Comic Sans", 20)).place(x=120, y=30)
        Button(self.kauliukas, text="Die 8", command=self.click_d8, font=("Comic Sans", 20)).place(x=210, y=30)
        Button(self.kauliukas, text="Die 10", command=self.click_d10, font=("Comic Sans", 20)).place(x=300, y=30)
        Button(self.kauliukas, text="Die 12", command=self.click_d12, font=("Comic Sans", 20)).place(x=405, y=30)
        Button(self.kauliukas, text="Die 20", command=self.click_d20, font=("Comic Sans", 20)).place(x=510, y=30)
        Button(self.kauliukas, text="Die 100", command=self.click_d100, font=("Comic Sans", 20)).place(x=615, y=30)

    #kauliuku mygtuko paspaudimo funkcija. Paspaudus inicijuoja rolinima 
    def click_d4(self):
        self.roll_dice(4)

    def click_d6(self):
        self.roll_dice(6)

    def click_d8(self):
        self.roll_dice(8)

    def click_d10(self):
        self.roll_dice(10)

    def click_d12(self):
        self.roll_dice(12)

    def click_d20(self):
        self.roll_dice(20)

    def click_d100(self):
        self.roll_dice(100)

    #rollina kauliukus
    def roll_dice(self, sides): 
        result = randrange(1, sides + 1)
        result_text = f"You rolled {result}\n"
        if result == sides:
            result_text += "You are very lucky"
        elif result >= 2:
            result_text += "Not bad"
        else:
            result_text += "Bad luck"
        
        #Rodo rezultata lange
        self.result_label.config(text=result_text)
        
                
langas = Tk()

dice_roller = DiceRoller(langas)


langas.mainloop()
