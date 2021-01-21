from string import ascii_uppercase as l
from tkinter import * 
from tkinter import messagebox

class vigenere:
	def __init__(self):
		self.ft = [l[i:]+l[:i] for i in range(len(l))]
	def vig(self,text,keyword):
		need = ""
		'''
		0 1 2 3 4
		5 6 7 8 9
		10 11 12 13 14
		'''
		for i in range(len(text)):
			need = need + keyword[int(i-int(i/len(keyword))*len(keyword))]
		return need

c = vigenere()

top = Tk()
top.geometry("350x160")   
	
Label(top,text = "EncryptedText : ").place(x = 5,y = 20)
pt = Entry(top,width = 40)
pt.place(x=90,y=20)

Label(top,text = "Keyword : ").place(x = 20,y = 50)
kw = Entry(top, width = 40)
kw.place(x = 90,y = 50)

from itertools import cycle
def ende(te,key):
	return ''.join(chr(ord(c)^ord(k)) for c,k in zip(te, cycle(key)))

def transmit():
	final = ""
	n=5
	try:
		for r in pt.get().split('`'):
			final = final + chr(int(r))

		final = ende(final,kw.get().upper())

		flip = [final[i:i+n] for i in range(0, len(final), n)]
		final = ""
		for w in flip:
			if len(w)== n:
				final = final + w[::-1]
			else:
				final = final +w

		f2 = final
		final = ""
		for i,w in enumerate(c.vig(f2,kw.get().upper())):
			final = final + (chr(ord(f2[i])-(ord(w)-65)))
		messagebox.showinfo("Encrypted Message", final)
	except:
		messagebox.showerror("Error", "Please make sure every field has been filled correctly")

submit_button = Button(top,text = "Calculate",command=transmit).place(x = 120,y = 100) 
top.mainloop()

