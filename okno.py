from tkinter import *


class GUI(Frame):
    def __init__(self, master):

        super(GUI,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text = "Jestem etykietą!")
        self.lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.bttn1 = Button(self, text = "Nic nie robię")
        self.bttn1.grid(row = 1, column = 0, columnspan = 2, sticky = W)
        self.ent1 = Entry(self)
        self.ent1.insert(0,"Default Value")
        self.ent1.grid()
        self.bttn2 = Button(self, text = "ja też nic nie robię")
        self.bttn2.grid()
        self.bttn3 = Button(self)
        self.bttn3["text"] = "Ja jednak coś robię!"
        self.bttn3["command"] = self.updateLabel
        self.bttn3.grid()

    def updateLabel(self):
        self.lbl["text"]= "Coś zostało zrobione"
        self.lbl.grid()


root = Tk()
root.title("Proste okno interfejsu")
root.geometry("225x100")
app = GUI(root)
app.grid()
root.mainloop()