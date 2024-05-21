from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # anexar o objeto na lista Cell.all
        Cell.all.append(self)



    def create_btn_object(self, location):

        btn = Button(
            location,
            bg='green',
            fg='black',
            width=4,
            height=2,
            bd=1,
            relief='solid',
            highlightcolor='black',
        )

        btn.bind('<Button-1>', self.left_click_action)# LeftClick
        btn.bind('<Button-3>', self.right_click_action)# RightCLick
        self.cell_btn_object = btn

    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="green",
            text=f"Codes Left:\n{Cell.cell_count}",
            font=("Modern DOS 8x8", 22)
        )
        Cell.cell_count_label_object = lbl


    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_lenght == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Great Job!', 'GAME OVER', 0)


        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')



    def get_cell_by_axis(self, x,y):
        # retornar uma Cell baseado no valor de X, Y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def surrounded_cells_mines_lenght(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_lenght)
            # Sobrepor texto do contador
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Codes Left:\n{Cell.cell_count}"
                )
            self.cell_btn_object.configure(
                bg='Black',
                fg='green',
                font = ("Modern DOS 8x8", 11)
            )
            # marca a cell como aberta (ultima linha do metodo)
            self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, 'DATA STOLEN!', 'GAME OVER', 0)
        sys.exit()


    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"