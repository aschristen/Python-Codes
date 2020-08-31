import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image
#from Tricount_optimized import create_list_friends_amounts

root=tk.Tk()
root.title("Calculator")

e=tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10,pady=10)

def Calculate(number):
   current=e.get()
   e.delete(0,tk.END)
   e.insert(0, str(current)+ str(number))

def Clear():
  e.delete(0, tk.END)

def sum_numbers():
  first_number=e.get()
  global f_num
  global type_math
  type_math="addition"
  f_num=int(first_number)
  e.delete(0, tk.END)

def subtract_numbers():
  global f_num
  global type_math
  first_number=e.get()
  type_math="subtraction"
  f_num=int(first_number)
  e.delete(0, tk.END)

def multiply_numbers():
  global f_num
  global type_math
  first_number=e.get()
  type_math="multiplication"
  f_num=int(first_number)
  e.delete(0, tk.END)

def divide_numbers():
  global f_num
  global type_math
  first_number=e.get()
  type_math="division"
  f_num=int(first_number)
  e.delete(0, tk.END)

def equal():
  second_number=e.get()
  e.delete(0, tk.END)
  if(type_math=="addition"):
    e.insert(0, f_num+int(second_number))
  elif(type_math=="multiplication"):
    e.insert(0, f_num*int(second_number))
  elif(type_math=="subtraction"):
    e.insert(0, f_num-int(second_number))
  else:
    e.insert(0,f_num/int(second_number)) 

button_1=tk.Button(root, text="1", padx=40, pady=20, command=lambda:Calculate(1))
button_2=tk.Button(root, text="2", padx=40, pady=20, command=lambda:Calculate(2))
button_3=tk.Button(root, text="3", padx=40, pady=20, command=lambda:Calculate(3))
button_4=tk.Button(root, text="4", padx=40, pady=20, command=lambda:Calculate(4))
button_5=tk.Button(root, text="5", padx=40, pady=20, command=lambda:Calculate(5))
button_6=tk.Button(root, text="6", padx=40, pady=20, command=lambda:Calculate(6))
button_7=tk.Button(root, text="7", padx=40, pady=20, command=lambda:Calculate(7))
button_8=tk.Button(root, text="8", padx=40, pady=20, command=lambda:Calculate(8))
button_9=tk.Button(root, text="9", padx=40, pady=20, command=lambda:Calculate(9))
button_0=tk.Button(root, text="0", padx=40, pady=20, command=lambda:Calculate(0))
button_sum=tk.Button(root, text="+", padx=40, pady=51, command=sum_numbers)
button_subtract=tk.Button(root, text="-", padx=40, pady=20, command=subtract_numbers)
button_multipy=tk.Button(root, text="*", padx=40, pady=20, command=multiply_numbers)
button_divide=tk.Button(root, text="/", padx=40, pady=20, command=divide_numbers)
button_equal=tk.Button(root, text="=", padx=40, pady=51, command=equal)
button_C=tk.Button(root, text="C", padx=90, pady=20, command=Clear)

button_subtract.grid(row=1,column=3)
button_multipy.grid(row=1,column=2)
button_divide.grid(row=1,column=1)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=0)
button_sum.grid(row=2,column=3, rowspan=2)

button_equal.grid(row=4,column=3, rowspan=2)
button_C.grid(row=5,column=1, columnspan=2)

button_quit=tk.Button(root, text="Exit", padx=134, pady=20, command=root.quit)
button_quit.grid(row=6, column=0, columnspan=3)

root.mainloop()