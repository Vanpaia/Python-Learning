from Tkinter import *
from PIL import Image, ImageTk
from DnD_Character_Environment import d

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
		
		self.button.grid(row=40, column =40, sticky = W)
		
		self.b_dice = Button(frame, text="Throw d20", command=self.dice)
		self.b_dice.grid(row=0, column = 0, columnspan = 1, sticky = W)
		
		self.result = ""
		self.label_text = StringVar()
		self.label_text.set(self.result)
		self.label = Label(frame, textvariable = self.label_text)
		self.label.grid(row=0, column = 5, sticky = W)
		
	def dice(self):
		self.result = d(20)
		self.label_text.set(self.result)

root = Tk()
root.resizable(width=False, height=False)
root.geometry("800x600")

import_background = Image.open('C:\\Users\Hagen\Desktop\DnD_Artwork\App_Background.png')
image_background = ImageTk.PhotoImage(import_background)
background = Label(root, image = image_background)
background.place(x=0, y=0, relwidth=1, relheight=1)

app = App(root)

root.mainloop()
root.destroy()