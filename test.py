import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

FQND_tab = ttk.Frame(tabControl)
Network_tab = ttk.Frame(tabControl)

tabControl.add(FQND_tab, text ='Tab 1')
tabControl.add(Network_tab, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")

ttk.Label(FQND_tab,
          text ="Welcome to \
		GeeksForGeeks").grid(column = 0,
							row = 0,
							padx = 30,
							pady = 30)
ttk.Label(Network_tab,
		  text ="Lets dive into the\
		world of computers").grid(column = 0,
									row = 0,
									padx = 30,
									pady = 30)

root.mainloop()
