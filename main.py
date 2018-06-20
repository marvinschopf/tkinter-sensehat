from sense_hat import SenseHat
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
sense = SenseHat()

class Application():
	text = "_"
	button_text = None
	def __init__(self, master):
		self.frame = Frame(master)
		self.frame.pack()
		self.load_widgets()
	def load_widgets(self):
		self.button = Button(self.frame,
							text="QUIT",
							fg="red",
							bg="blue",
							command=self.frame.quit)
		self.button.pack(side=LEFT)
		
		self.button_text = Button(self.frame,
									text="Text",
									fg="green",
									bg="cyan",
									command=self.ask_text)
		self.button_text.pack(side=LEFT)
	
	def sense_hello(self):
		sense.show_message("Hello", 
		scroll_speed=0.05,
		text_colour=[255,255,0],
		back_colour=[0,0,255])
		
	def text_anzeigen(self):
		self.button_text.config(state='disabled')
		sense.show_message(self.text, 
		scroll_speed=0.05,
		text_colour=[255,255,0],
		back_colour=[0,0,255])
		self.button_text.config(state='normal')
		
	def ask_text(self):
		self.text = tkSimpleDialog.askstring("Text", "Welcher Text soll angezeigt werden?")
		if(self.text == None):
			tkMessageBox.showwarning("Fehler", "Es wurde kein Text angegeben.")
		else:
			self.text_anzeigen()

		
root = Tk()
app = Application(root)
root.mainloop()


