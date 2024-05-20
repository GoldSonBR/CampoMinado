from tkinter import *
import settings
import utils


root = Tk()
# Sobreposição das configuralções de janela
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("MineFieldProject")
root.resizable(False, False)

top_frame =Frame(
    root,
    bg='white', #Mudar depois
    width= settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='cyan', #Mudar depois
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='blue', #Mudar depois
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)


# Rodar Janela
root.mainloop()