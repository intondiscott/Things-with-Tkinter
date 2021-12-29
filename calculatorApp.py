import tkinter as tk
from tkinter import *
    
class calc(Tk):
    def set_window_size_and_title(self,x,y, title_name):
        self.x = x
        self.y = y
        self.title_name = title_name
        self.title(title_name)
        self.geometry(f'{x}x{y}')

    def num_buttons(self):
        global num_button
        num_button= []
        operator_key = ['+', '-', '*', '/']

        for num in range(10):
            num_button.append(num)
            num_button[num] = tk.Button(text=num,width=8,height=4)

        plus_button = tk.Button(text=operator_key[0],width=8, height=4)
        plus_button['command'] = lambda: self.get_first_number(self.get_operation(operator_key[0]))
        plus_button.grid(row=4, column=3, padx=1, pady=1)

        sub_button = tk.Button(text=operator_key[1],width=8, height=4)
        sub_button['command'] = lambda: self.get_first_number(self.get_operation(operator_key[1]))
        sub_button.grid(row=3,column=3, padx=1, pady=1)

        multiply_button = tk.Button(text=operator_key[2],width=8, height=4)
        multiply_button['command'] = lambda: self.get_first_number(self.get_operation(operator_key[2]))
        multiply_button.grid(row=2,column=3, padx=1, pady=1)

        divide_button = tk.Button(text=operator_key[3],width=8, height=4)
        divide_button['command'] = lambda: self.get_first_number(self.get_operation(operator_key[3]))
        divide_button.grid(row=1, column=3, padx=1, pady=1)

        equals = tk.Button(text='=', width=18, height=4, command=lambda: self.result())
        equals.grid(row=4,column=1,columnspan=2, padx=1, pady=1)

        num_button[7].grid(row=1,column=0, padx=1, pady=1)
        num_button[8].grid(row=1, column=1, padx=1, pady=1)
        num_button[9].grid(row=1, column=2, padx=1, pady=1)
        num_button[4].grid(row=2, column=0, padx=1, pady=1)
        num_button[5].grid(row=2, column=1, padx=1, pady=1)
        num_button[6].grid(row=2, column=2, padx=1, pady=1)
        num_button[1].grid(row=3, column=0, padx=1, pady=1)
        num_button[2].grid(row=3, column=1, padx=1, pady=1)
        num_button[3].grid(row=3, column=2, padx=1, pady=1)
        num_button[0].grid(row=4, column=0, padx=1, pady=1)

        num_button[0]['command'] = lambda: self.button_function(num_button[0]['text'])
        num_button[1]['command'] = lambda: self.button_function(num_button[1]['text'])
        num_button[2]['command'] = lambda: self.button_function(num_button[2]['text'])
        num_button[3]['command'] = lambda: self.button_function(num_button[3]['text'])
        num_button[4]['command'] = lambda: self.button_function(num_button[4]['text'])
        num_button[5]['command'] = lambda: self.button_function(num_button[5]['text'])
        num_button[6]['command'] = lambda: self.button_function(num_button[6]['text'])
        num_button[7]['command'] = lambda: self.button_function(num_button[7]['text'])
        num_button[8]['command'] = lambda: self.button_function(num_button[8]['text'])
        num_button[9]['command'] = lambda: self.button_function(num_button[9]['text'])

    def draw_textfield(self):
        global inputs
        inputs = tk.Entry()
        inputs.config(width=24,border=10,font=20)
        inputs.grid(row=0, column=0, columnspan=4)

    def button_function(self,text):
        cur_idx = inputs.get()
        inputs.delete(0,END)
        inputs.insert(0,str(cur_idx)+str(text))

    def result(self):
        second_num = inputs.get()
        answer = 0
        if operation_value == '*':
            answer = int(first_num) * int(second_num)
        if operation_value == '-':
            answer = int(first_num) - int(second_num)
        if operation_value == '+':
            answer = int(first_num) + int(second_num)
        if operation_value == '/':
            answer = int(first_num) / int(second_num)

        inputs.delete(0, END)
        inputs.insert(0,str(answer))

    def get_operation(self,operator):
       global operation_value
       self.operator = operator
       operation_value = operator
       return operation_value

    def get_first_number(self,key):
       self.key = key
       global first_num
       first_num = inputs.get()
       inputs.delete(0,END)

def main():
    WIDTH = 300
    HIGHT = 360
    TITLE = "Calculator App"

    calculator = calc()
    calculator.set_window_size_and_title(WIDTH, HIGHT, TITLE)
    calculator.draw_textfield()
    calculator.num_buttons()
    calculator.mainloop()
if __name__ == '__main__':
   main()
    