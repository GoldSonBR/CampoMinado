from tkinter import *


root = Tk()
# Sobreposição das configuralções de janela
root.configure(bg='antique white')
root.geometry('1440x720')
root.title("MineFieldProject")
root.resizable(False, False)

top_frame =Frame(
    root,
    bg='red', #Mudar depois
    width= 1440,
    height=180
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='green', #Mudar depois
    width=360,
    height=540
)
left_frame.place(x=0, y=180)

# Rodar Janela
root.mainloop()