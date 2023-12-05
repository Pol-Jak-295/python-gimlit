#made by: pol-jak-295
# python 3.12

#first school python program
#python 3.12
#at error skip line and print the error message
import random
import tkinter as tk
import customtkinter as ctk
from functools import reduce
from tkinter import messagebox
def self_math_test():


    try:
        print(1 + 2 * (3 - 4 * (5 - 6)))
    except Exception as a:
        print(a)
    try:
        print(23//6+23%6)
    except Exception as b:
        print(b)
    try:
        print(23//(6+23)%6)
    except Exception as c:
        print(c)
    try:
        print(32//2*4)
    except Exception as d:
        print(d)
    try:
        print(32//(2**4))
    except Exception as e:
        print(e)
    try:
        print(32//(2%4))
    except Exception as f:
        print(f)
    try:
        print(32//(2//4))
    except Exception as g:
        print(g)




def self_var_test():
    float3= float(3)
    int4_6 = int(4.6)
    float_minus_6 = float(-6)
    print("real number 3 is: " + str(float3))
    print("number 4.6 is: " + str(int4_6))
    print("real number -6 is: " + str(float_minus_6))


variables = {}









def calculator_of_numbers():


    def save_value(var_name, entry):
        try:
            value = float(entry.get())
            variables[var_name] = value
        except ValueError:
            variables[var_name] = None
    
    def get_variable_values():
        num_variables = int(num_variables_entry.get())
        variable_entries = []
        submit_button.config(text="Submit")  # Change button text to "Submit"
        
        def submit_value():
            nonlocal variable_entries
            nonlocal num_variables
            
            save_value("var" + str(len(variable_entries) + 1), variable_entries[-1])  # Save the value of the current entry
            
            if len(variable_entries) < num_variables:
                label.config(text="Variable var" + str(len(variable_entries) + 2) + ":")  # Update label text
                entry.delete(0, tk.END)  # Clear the entry field
                variable_entries.append(entry)  # Add the entry to the list
            else:
                calculate_button.pack()  # Show the calculate button
                submit_button.config(text="Submit", state=tk.DISABLED)  # Change button text to "Submit" and disable it
        variables_entries = {}
        label = tk.Label(window, text="Variable var1:")
        label.pack()
        entry = tk.Entry(window)
        entry.pack()
        variable_entries.append(entry)
    
        submit_button.config(command=submit_value)  # Change button command to submit_value
    
    def calculate():
        values = [float(entry.get()) for entry in variable_entries]
        # Perform the calculations
        # ...
    
    # Create the tkinter window
    window = tk.Tk()
    window.title("Variable Calculator")
    window.geometry("300x200")  # Set window size to 300x200
    
    # Create the input fields
    num_variables_label = tk.Label(window, text="Enter the number of variables:")
    num_variables_label.pack()
    num_variables_entry = tk.Entry(window)
    num_variables_entry.pack()
    
    def get_num_variables():
        get_variable_values()
    
    # Create the button to submit the number of variables
    submit_button = tk.Button(window, text="Submit", command=get_num_variables)
    submit_button.pack()
    
    # Create the calculate button
    calculate_button = tk.Button(window, text="Calculate", command=calculate)
    
    # Run the tkinter window
    window.mainloop()
    

def rectangle_calculator():
    def calculator():
        width = float(entry_width.get())
        height = float(entry_height.get())
        
        area = width * height
        result_label.config(text="The area of a rectangle with width: {} and height: {} is: {} square units.".format(width, height, area))
        circumference = 2 * (width + height)
        circumference_label.config(text="The circumference of a rectangle with width: {} and height: {} is: {} units.".format(width, height, circumference))
        diagonal = (width ** 2 + height ** 2) ** 0.5
        diagonal_label.config(text="The diagonal of a rectangle with width: {} and height: {} is: {} units.".format(width, height, diagonal))
        window.geometry("500x200")
    window = tk.Tk()
    window.title("Rectangle Calculator")
    window.geometry("300x200")  # Set window size to 300x200

    # Create labels for width and height
    width_label = tk.Label(window, text="Width:")
    width_label.grid(row=0, column=0)

    # Create entry fields for width and height
    entry_width = tk.Entry(window)
    entry_width.grid(row=0, column=1)

    height_label = tk.Label(window, text="Height:")
    height_label.grid(row=1, column=0)

    entry_height = tk.Entry(window)
    entry_height.grid(row=1, column=1)
    
    # Create a button to calculate the rectangle properties
    calculate_button = tk.Button(window, text="Calculate", command=calculator)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Create labels to display the results
    result_label = tk.Label(window)
    result_label.grid(row=3, column=0, columnspan=2)
    
    circumference_label = tk.Label(window)
    circumference_label.grid(row=4, column=0, columnspan=2)
    
    diagonal_label = tk.Label(window)
    diagonal_label.grid(row=5, column=0, columnspan=2)

    window.mainloop()
    
    
    
    
def everyone_by_five():
    def calculator():
        # Prompt the cashier to enter the prices of five items
        price1 = float(entry1.get())
        price2 = float(entry2.get())
        price3 = float(entry3.get())
        price4 = float(entry4.get())
        price5 = float(entry5.get())

        # Calculate the sum of the prices
        total = price1 + price2 + price3 + price4 + price5

        # Print the sum of the prices
        result_label.config(text="The total sum is: " + str(total))
        messagebox.showinfo("Result", "The total sum is: " + str(total))
    window = tk.Tk()
    window.title("Everyone by Five")
    window.geometry("300x200")

    # Create labels and entry fields using grid layout
    label1 = tk.Label(window, text="Price of item 1:")
    label1.grid(row=0, column=0, padx=10, pady=5)

    entry1 = tk.Entry(window)
    entry1.grid(row=0, column=1, padx=10, pady=5)

    label2 = tk.Label(window, text="Price of item 2:")
    label2.grid(row=1, column=0, padx=10, pady=5)

    entry2 = tk.Entry(window)
    entry2.grid(row=1, column=1, padx=10, pady=5)

    label3 = tk.Label(window, text="Price of item 3:")
    label3.grid(row=2, column=0, padx=10, pady=5)

    entry3 = tk.Entry(window)
    entry3.grid(row=2, column=1, padx=10, pady=5)

    label4 = tk.Label(window, text="Price of item 4:")
    label4.grid(row=3, column=0, padx=10, pady=5)

    entry4 = tk.Entry(window)
    entry4.grid(row=3, column=1, padx=10, pady=5)

    label5 = tk.Label(window, text="Price of item 5:")
    label5.grid(row=4, column=0, padx=10, pady=5)

    entry5 = tk.Entry(window)
    entry5.grid(row=4, column=1, padx=10, pady=5)

    # Create a button to calculate the sum
    calculate_button = tk.Button(window, text="Calculate", command=calculator)
    calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Create a label to display the result
    result_label = tk.Label(window)
    result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    window.mainloop()

        
        
        
        
def more_or_less_than_100():
    def more_or_less_than_100():
    # Take input from the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Calculate the sum
        sum = num1 + num2

        # Print the sum
        print("The sum is:", sum)

        # Check if the sum is larger or smaller than 100
        if sum > 100:
            def more_or_less_than_100():
                sum = int(input("Enter the sum: "))
                if sum > 100:
                    messagebox.showinfo("Result", "The sum is larger than 100.")
                elif sum < 100:
                    messagebox.showinfo("Result", "The sum is smaller than 100.")
                else:
                    messagebox.showinfo("Result", "The sum is equal to 100.")
    pass
def multiplication_practice():
    def generate_random_numbers():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        return num1, num2

        def check_answer():
                user_answer = int(answer_entry.get())
                if user_answer == correct_answer:
                    messagebox.showinfo("Result", "Answer is correct!")
                else:
                    messagebox.showinfo("Result", f"You entered: {user_answer} and the correct answer is: {correct_answer}")

                answer_entry.delete(0, tk.END)
                generate_question()

        def generate_question():
                num1, num2 = generate_random_numbers()
                question_label.config(text=f"What is the result of {num1} * {num2}?")
                global correct_answer
                correct_answer = num1 * num2

        def main():
                name = name_entry.get()
                messagebox.showinfo("Welcome", f"Hey {name}, let's train multiplication!")

                generate_question()

    window = tk.Tk()
    window.title("Multiplication Practice")
    window.geometry("300x200")  # Set window size to 300x200

    name_label = tk.Label(window, text="Enter your name:")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack
    start_button = tk.Button(window, text="Start", command=main)
    start_button.pack
    question_label = tk.Label(window, text="")
    question_label.pack
    answer_label = tk.Label(window, text="Enter your answer:")
    answer_label.pack()
    answer_entry = tk.Entry(window)
    answer_entry.pack
    check_button = tk.Button(window, text="Check", command=check_answer)
    check_button.pack
    window.mainloop()

    pass
def fuel_usage_calculator():
    def calculate_fuel_usage():
                fuel_used = fuel_entry.get().strip().rstrip('l').rstrip('gal')
                distance = distance_entry.get().strip().rstrip('km').rstrip('mi')

                fuel_used_num = float(fuel_used)
                distance_num = float(distance)

                if fuel_used.endswith('l'):
                    fuel_usage_liters = (fuel_used_num / distance_num) * 100
                    fuel_used_gallons = fuel_used_num * 0.264172
                    fuel_usage_gallons = distance_num / fuel_used_gallons
                else:
                    fuel_used_liters = fuel_used_num * 3.78541
                    fuel_usage_liters = (fuel_used_liters / distance_num) * 100
                    fuel_usage_gallons = distance_num / fuel_used_num

                fuel_usage_liters = round(fuel_usage_liters, 2)
                fuel_usage_gallons = round(fuel_usage_gallons, 2)

                messagebox.showinfo("Result", f"Average fuel usage is: {fuel_usage_liters} liters per 100 kilometers\nAverage fuel usage is: {fuel_usage_gallons} miles per gallon")

    window = tk.Tk()
    window.title("Fuel Usage Calculator")
    window.geometry("300x200")  # Set window size to 300x200
    fuel_label = tk.Label(window, text="Enter the amount of fuel used (liters or gallons):")
    fuel_label.pack()
    fuel_entry = tk.Entry(window)
    fuel_entry.pack()
    distance_label = tk.Label(window, text="Enter the number of kilometers or miles traveled:")
    distance_label.pack()
    distance_entry = tk.Entry(window)
    distance_entry.pack()
    calculate_button = tk.Button(window, text="Calculate", command=calculate_fuel_usage)
    calculate_button.pack()
    window.mainloop()
    pass
def bmi_calculator():
    def calculate_bmi():
        weight = float(weight_entry.get())
        weight_unit = weight_unit_var.get()
        height_unit = height_unit_var.get()
        if height_unit == 'ft':
            feet = float(feet_entry.get())
            inches = float(inches_entry.get())
            height = (feet * 0.3048) + (inches * 0.0254)
        else:
            height = float(height_entry.get())
        if weight_unit == 'lbs':
            weight = weight * 0.45359237
        bmi = weight / (height * height)
        messagebox.showinfo("Result", f"Your BMI is: {bmi}")
        if bmi < 18.5:
            messagebox.showinfo("Weight Category", "You are too skinny, go for a burek")
        elif bmi < 25:
            messagebox.showinfo("Weight Category", "You are normal, go for a burek")
        else:
            messagebox.showinfo("Weight Category", "You are FAT AF, lay off the burek")
    window = tk.Tk()
    window.title("BMI Calculator")
    window.geometry("300x200")  # Set window size to 300x200
    weight_label = tk.Label(window, text="Enter your weight without the unit:")
    weight_label.pack()
    weight_entry = tk.Entry(window)
    weight_entry.pack()
    weight_unit_label = tk.Label(window, text="Enter the unit of weight (kg/lbs):")
    weight_unit_label.pack()
    weight_unit_var = tk.StringVar()
    weight_unit_combobox = tk.OptionMenu(window, weight_unit_var, "kg", "lbs")
    weight_unit_combobox.pack()
    height_unit_label = tk.Label(window, text="Enter the unit of height (m/ft):")
    height_unit_label.pack()
    height_unit_var = tk.StringVar()
    height_unit_combobox = tk.OptionMenu(window, height_unit_var, "m", "ft")
    height_unit_combobox.pack()
    height_frame = tk.Frame(window)
    height_frame.pack()
    height_label = tk.Label(height_frame, text="Enter your height without the unit:")
    height_label.pack()
    height_entry = tk.Entry(height_frame)
    height_entry.pack()
    feet_label = tk.Label(height_frame, text="Enter the number of feet:")
    feet_label.pack()
    feet_entry = tk.Entry(height_frame)
    feet_entry.pack()
    inches_label = tk.Label(height_frame, text="Enter the number of inches:")
    inches_label.pack()
    inches_entry = tk.Entry(height_frame)
    inches_entry.pack()
    calculate_button = tk.Button(window, text="Calculate", command=calculate_bmi)
    calculate_button.pack()
    window.mainloop()
    pass
def open_selected_function():
    function_name = function_var.get()
    if function_name == "more_or_less_than_100":
        more_or_less_than_100()
    elif function_name == "multiplication_practice":
        multiplication_practice()
    elif function_name == "fuel_usage_calculator":
        fuel_usage_calculator()
    elif function_name == "bmi_calculator":
        bmi_calculator()
    elif function_name == "calculator_of_numbers":
        calculator_of_numbers()
    elif function_name == "rectangle_calculator":
        rectangle_calculator()
    elif function_name == "everyone_by_five":
        everyone_by_five()
    elif function_name == "self_math_test":
        self_math_test()
    elif function_name == "self_var_test":
        self_var_test()
    else:
        messagebox.showinfo("Invalid Function", "Invalid function name.")
window = tk.Tk()
window.title("Function Selector")
window.geometry("300x200")  # Set window size to 300x200

function_label = tk.Label(window, text="Select the function you want to run:")
function_label.pack()

function_var = tk.StringVar()
function_combobox = tk.OptionMenu(window, function_var, "more_or_less_than_100", "multiplication_practice", "fuel_usage_calculator", "bmi_calculator", "calculator_of_numbers", "rectangle_calculator", "everyone_by_five")
function_combobox.pack(padx=10, pady=10)
#make a function to kill the current window and open the selected function
    
run_button = tk.Button(window, text="Run", command=open_selected_function)
run_button.pack(padx=10, pady=10)

window.mainloop()