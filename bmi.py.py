from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def BMI():
    try:
        h = float(Height.get())
        w = float(Weight.get())

        # Convert height into meters
        m = h / 100
        bmi = round(float(w / m**2), 1)

        label1.config(text=bmi)

        if bmi <= 18.5:
            label2.config(text="Underweight!")
            label3.config(text="You have lower weight than normal body!")
        elif 18.5 < bmi <= 25:
            label2.config(text="Normal!")
            label3.config(text="It indicates that you are healthy!")
        elif 25 < bmi <= 30:
            label2.config(text="Overweight!")
            label3.config(text="You are slightly overweight! A doctor may advise to lose some weight for health reasons.")
        else:
            label2.config(text="Obese!")
            label3.config(text="Health may be at risk if you do not lose weight!")
    except ValueError:
        label1.config(text="Error")
        label2.config(text="Invalid input!")
        label3.config(text="Please enter valid numbers.")

# Icon
# Uncomment the following line if you have an icon file
# image_icon = PhotoImage(file="user.png")
# root.iconphoto(False, image_icon)

# Heading
heading = Label(root, text="BMI CALCULATOR", font="arial 20 bold", bg="#f0f1f5", fg="#1f6e68")
heading.pack(pady=20)  # Add some vertical padding

# Bottom Box
Label(root, width=92, height=18, bg="lightblue").pack(side=BOTTOM)

# Scale for Height
current_value = tk.DoubleVar()
def slider_changed(event):
    Height.set('{:.2f}'.format(current_value.get()))

style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

# Scale for Weight
current_value2 = tk.DoubleVar()
def slider_changed2(event):
    Weight.set('{:.2f}'.format(current_value2.get()))

style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

# Entry boxes
Height = StringVar()
Weight = StringVar()

height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)

# Labels for Height and Weight
Label(root, text="Height (cm)", font="arial 12", bg="lightblue").place(x=35, y=130)
Label(root, text="Weight (kg)", font="arial 12", bg="lightblue").place(x=255, y=130)

# Button to calculate BMI
Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=280, y=300)

# Labels for displaying results
label1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=305)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430)

label3 = Label(root, font="arial 10 bold", bg="lightblue")
label3.place(x=200, y=500)

root.mainloop()