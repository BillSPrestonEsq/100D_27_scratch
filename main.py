from tkinter import *

def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input = Entry()
input.grid(row=2, column=3)

my_label = Label(text="I am a label", font=("Arial",24,"bold"))
my_label.grid(row=0, column=0)
my_label["text"] = "New Text"

button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

button2 = Button(text="Click me too", command=button_clicked)
button2.grid(row=0, column=2)




window.mainloop()


#
# # def add(*args):
# #     sum = 0
# #     for n in args:
# #         sum += n
# #
# #     print(sum)
# #
# # add(1, 2, 3, 4, 5)
# #
# # def calculate(n, **kwargs):
# #     n += kwargs["add"]
# #     n *= kwargs["multiply"]
# #     return n
# #
# # print(calculate(2, add=3, multiply=5))
#
# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
# my_car = Car(make="Nissan")
# print(my_car.model)