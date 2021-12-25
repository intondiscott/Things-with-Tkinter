import tkinter as tk
from tkinter import *


class number_incrementer(Tk):
    count = 0

    def init(self):
        self.mainloop()

    def size_of_window(self, x, y):
        self.x = x
        self.y = y
        self.geometry(f'{x}x{y}')

    def button(self):
        button = tk.Button(self, text="number incrementer", command=self.counter)
        button.grid(column=0, row=0)

    def counter(self):
        self.count += 1
        self.label()

    def label(self):
        label = tk.Label(self, fg="dark blue", font=("Times", 30))
        label.config(text=self.count)
        label.grid(column=0, row=2)


def main():
    WIDTH = 40
    HIGHT = 80
    run = number_incrementer()
    run.size_of_window(WIDTH, HIGHT)
    run.button()
    run.mainloop()


main()
