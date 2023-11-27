#made by: pol-jak-295
# python 3.12

#first school python program
#python 3.12
#at error skip line and print the error message
import random
import tkinter as tk
import customtkinter as ctk
from functools import reduce

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

def save_value(var_name, entry):
    try:
        value = float(entry.get())
        variables[var_name] = value
    except ValueError:
        variables[var_name] = None

def calculator_of_numbers():
    # Calculate the instructions
    values = list(variables.values())

    first_instruction = sum(values)


    first_quarter = values[0:len(values)//4]
    second_quarter = values[len(values)//4:2*len(values)//4]
    third_quarter = values[2*len(values)//4:3*len(values)//4]
    last_quarter = values[3*len(values)//4:4*len(values)//4]

    pt1 = reduce(lambda x, y: x*y, second_quarter)
    pt2 = reduce(lambda x, y: x*y, third_quarter)
    pt3 = reduce(lambda x, y: x*y, last_quarter)
    pt4 = reduce(lambda x, y: x*y, first_quarter)
    second_instruction = sum(first_quarter + second_quarter) - sum(third_quarter + last_quarter)
    third_instruction = pt1*pt2*pt3*pt4
    fourth_instruction = (pt1*pt2) / (pt3*pt4)


    # Display the output in the tkinter window
    output_text.set("1. " + str(first_instruction) + "\n" +
                    "2. " + str(second_instruction) + "\n" +
                    "3. " + str(third_instruction) + "\n" +
                    "4. " + str(fourth_instruction))

# Create the tkinter window
    window = tk.Tk()
    window.title("Variable Calculator")

    # Create the input fields
    num_variables = int(input("Enter the number of variables: "))
    for i in range(1, num_variables+1):
        label = tk.Label(window, text="Variable var" + str(i) + ":")
        label.pack()
        entry = tk.Entry(window)
        entry.pack()
        button = tk.Button(window, text="Save", command=lambda var_name="var"+str(i), entry=entry: save_value(var_name, entry))
        button.pack()
    
    # Create the button to calculate the instructions
    calculate_button = tk.Button(window, text="Calculate", command=calculate)
    calculate_button.pack()
    
    # Create the output label
    output_text = tk.StringVar()
    output_label = tk.Label(window, textvariable=output_text)
    output_label.pack()
    
    # Run the tkinter window
    window.mainloop()




def rectangle_calculator():
    window = tk.Tk()
    window.title("Rectangle Calculator")
    
    
    
    """width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    area = width * height
    print("The area of a rectangle with width:", width, "and height:", height, "is:", area, "square units.")
    circumference = 2 * (width + height)
    print("The circumference of a rectangle with width:", width, "and height:", height, "is:", circumference, "units.")
"""


def everyone_by_five():

    # Prompt the cashier to enter the prices of five items
    price1 = float(input("Enter the price of item 1: "))
    price2 = float(input("Enter the price of item 2: "))
    price3 = float(input("Enter the price of item 3: "))
    price4 = float(input("Enter the price of item 4: "))
    price5 = float(input("Enter the price of item 5: "))

    # Calculate the sum of the prices
    total = price1 + price2 + price3 + price4 + price5

    # Print the sum of the prices
    print("The total sum is:", total)


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
        
        
        
        
        
        
        
        
        
def more_or_less_than_100():
    # Function implementation goes here
    pass
def multiplication_practice():
    # Function implementation goes here
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
    else:
        messagebox.showinfo("Invalid Function", "Invalid function name.")
window = tk.Tk()
window.title("Function Selector")
function_label = tk.Label(window, text="Select the function you want to run:")
function_label.pack()
function_var = tk.StringVar()
function_combobox = tk.OptionMenu(window, function_var, "more_or_less_than_100", "multiplication_practice", "fuel_usage_calculator", "bmi_calculator")
function_combobox.pack()
run_button = tk.Button(window, text="Run", command=open_selected_function)
run_button.pack()
window.mainloop()