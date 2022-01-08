import tkinter as tk
from tkinter import *

def getLambda(func, text):
    return lambda: func(text)

class Calc(Tk):
    def __init__(self):
        super().__init__()
        self.first_num = 0.0
        self.operator = None

    def _set_window_size_and_title(self, x, y, title_name):
        self.title(title_name)
        self.geometry(f'{x}x{y}')

    def _render_buttons(self):
        H = 2
        for num in range(10):
            button = tk.Button(self, text=num, width=8, height=H, command=getLambda(self._number_pressed, num))
            button.grid(row = 4 if num == 0 else 3 - int((num - 1) / 3), column = 0 if num == 0 else (num + 2) % 3, padx = 1, pady = 1)

        for i, op in enumerate(['/', '*', '-', '+']):
            button = tk.Button(self, text=op, width=8, height=H, command=getLambda(self._op_pressed, op))
            button.grid(row = 1 + i, column = 3, padx = 1, pady = 1)

        equals = tk.Button(self, text='=', width=18, height=H, command= lambda: self._equals_pressed())
        equals.grid(row=4, column=1, columnspan=2, padx=1, pady=1)

    def _render_textfield(self):
        self.inputs = tk.Entry(self, width=14)
        self.inputs.pack(fill=tk.X, expand=True)
        self.inputs.grid(row=0, column=0, columnspan=4)

    def _number_pressed(self, numChar):
        print('pressed ', numChar)
        if self.operator == '=':
            self.inputs.delete(0, END)
            self.operator = None
        self.inputs.insert(len(self.inputs.get()), numChar)

    def _op_pressed(self, operator):
        if self.operator is not None and self.operator != '=':
            self._equals_pressed()
        self.first_num = 0.0 if len(self.inputs.get()) == 0 else float(self.inputs.get())
        self.operator = operator
        print(self.first_num, self.operator, ' ? ')
        self.inputs.delete(0, END)

    def _equals_pressed(self):
        if self.operator is None or self.first_num is None:
            return
        second_num = 0.0 if len(self.inputs.get()) == 0 else float(self.inputs.get())
        print('second num = ', second_num)
        if self.operator == '*':
            result = self.first_num * second_num
        elif self.operator == '-':
            result = self.first_num - second_num
        elif self.operator == '+':
            result = self.first_num + second_num
        elif self.operator == '/':
            result = self.first_num / second_num
        else:
            result = 0.0
        print(self.first_num, self.operator, second_num, ' = ', result)
        self.inputs.delete(0, END)
        self.inputs.insert(0, str(result))
        self.first_num = result
        self.operator = '='

    def render(self, width, height):
        self._set_window_size_and_title(width, height, "Calculator App")
        self._render_textfield()
        self._render_buttons()


def main():
    WIDTH = 600
    HEIGHT = 360

    calculator = Calc()
    calculator.render(WIDTH, HEIGHT)
    calculator.mainloop()


if __name__ == '__main__':
    print("Starting calc")
    main()
