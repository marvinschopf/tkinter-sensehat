from sense_hat import SenseHat
from Tkinter import *
sense = SenseHat()

class Application():
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
		
		self.button_hello = Button(self.frame,
									text="Hello",
									fg="green",
									bg="cyan",
									command=self.sense_hello)
		self.button_hello.pack(side=LEFT)
	
	def sense_hello(self):
		sense.show_message("Hello", 
		scroll_speed=0.05,
		text_colour=[255,255,0],
		back_colour=[0,0,255])

		
root = Tk()
app = Application(root)
root.mainloop()


