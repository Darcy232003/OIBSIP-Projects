
from tkinter import *
from tkinter import messagebox


def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height

def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight


def calculate_bmi(a=""):
    print(a)
    '''
      This function calculates the result
    '''
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)


if __name__ == '__main__':
    TOP = Tk()
    # noinspection PyTypeChecker
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("400x300")
    TOP.configure(background="#5e6472")
    TOP.title("BMI Calculator")
    TOP.resizable(width=False, height=False)

    label1 = Label(TOP, bg="#5e6472", fg="white", text="BMI Calculator", font=("Arial", 15, "bold"), pady=10)
    label1.pack()

    label2 = Label(TOP, bg="#5e6472", fg="white", text="Enter Weight (in kg):", font=("Arial", 10, "bold"), pady=5)
    label2.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Arial 11")
    ENTRY1.place(x=240, y=60)

    label3 = Label(TOP, bg="#5e6472", fg="white", text="Enter Height (in cm):", font=("Arial", 10, "bold"), pady=5)
    label3.place(x=55, y=100)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Arial 11")
    ENTRY2.place(x=240, y=100)

    BUTTON = Button(bg="#2187e7", bd=12, text="Calculate BMI", padx=10, pady=10, command=calculate_bmi,
                    font=("Arial", 12, "bold"))
    BUTTON.place(x=140, y=150)

    result_label = Label(TOP, bg="#5e6472", fg="white", font=("Arial", 12))
    result_label.place(x=140, y=200)

    TOP.mainloop()
