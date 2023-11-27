#first school python program
#python 3.12
#at error skip line and print the error message
import random




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

def calculator_of_numbers():
    print("using variables in the vars dictionary (feel free to add, remove or change the values)")
    vars = {'a' : 1, 'b' : 2 , 'c' : 3, 'd' : 4}
    #print the sum of all the variables in the dictionary even if the number of variables changes
    from functools import reduce

    first_instruction = sum(vars.values())

    pt1 = sum(list(vars.values())[0:len(vars)//2])
    pt2 = sum(vars.values()) - pt1
    second_instruction = pt1 - pt2

    third_instruction = reduce(lambda x, y: x*y, vars.values())

    fourth_instruction = str(reduce(lambda x, y: x*y, list(vars.values())[0:len(vars)//2])) + str(reduce(lambda x, y: x*y, list(vars.values())[len(vars)//2:]))

    print("1. " + str(first_instruction))
    print("2. " + str(second_instruction))
    print("3. " + str(third_instruction))
    print("4. " + str(fourth_instruction))




def rectangle_calculator():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    area = width * height
    print("The area of a rectangle with width:", width, "and height:", height, "is:", area, "square units.")
    circumference = 2 * (width + height)
    print("The circumference of a rectangle with width:", width, "and height:", height, "is:", circumference, "units.")



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
        print("The sum is larger than 100.")
    elif sum < 100:
        print("The sum is smaller than 100.")
    else:
        print("The sum is equal to 100.")







def multiplication_practice():

    def generate_random_numbers():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        return num1, num2

    def check_answer(num1, num2, user_answer):
        correct_answer = num1 * num2
        if user_answer == correct_answer:
            print("Answer is correct!")
        else:
            print(f"You entered: {user_answer} and the correct answer is: {correct_answer}")

    def main():
        name = input("Enter your name: ")
        print(f"Hey {name}, would you like to train multiplication?")

        while True:
            num1, num2 = generate_random_numbers()
            print(f"What is the result of {num1} * {num2}?")
            user_answer = int(input("Enter your answer: "))
            check_answer(num1, num2, user_answer)

            continue_choice = input("Do you want to continue? (y/n): ")
            if continue_choice.lower() not in ['y', 'yes']:
                break

    if __name__ == "__main__":
        main()





def fuel_usage_calculator ():
    # Prompt the user for the amount of fuel used
    fuel_used = input("Enter the amount of fuel used (liters or gallons): ").strip().rstrip('l').rstrip('gal')

    # Prompt the user for the distance traveled
    distance = input("Enter the number of kilometers or miles traveled: ").strip().rstrip('km').rstrip('mi')

    # Convert the fuel used and distance to floating point numbers
    fuel_used_num = float(fuel_used)
    distance_num = float(distance)

    # Check if the user entered fuel usage in liters or gallons
    if fuel_used.endswith('l'):
        # Calculate fuel usage in liters per 100 kilometers
        fuel_usage_liters = (fuel_used_num / distance_num) * 100
        # Convert fuel usage from liters to gallons
        fuel_used_gallons = fuel_used_num * 0.264172
        # Calculate fuel usage in miles per gallon
        fuel_usage_gallons = distance_num / fuel_used_gallons
    else:
        # Convert fuel usage from gallons to liters
        fuel_used_liters = fuel_used_num * 3.78541
        # Calculate fuel usage in liters per 100 kilometers
        fuel_usage_liters = (fuel_used_liters / distance_num) * 100
        # Calculate fuel usage in miles per gallon
        fuel_usage_gallons = distance_num / fuel_used_num

    # Round the fuel usage values to 2 decimal points
    fuel_usage_liters = round(fuel_usage_liters, 2)
    fuel_usage_gallons = round(fuel_usage_gallons, 2)

    # Print the fuel usage in liters per 100 kilometers and miles per gallon
    l_100km = "Average fuel usage is: {} liters per 100 kilometers".format(fuel_usage_liters)
    mpg = "Average fuel usage is: {} miles per gallon".format(fuel_usage_gallons)
    print(l_100km + "\n" + mpg)










def bmi_calculator ():
    def calculate_bmi(weight, height):
        # Convert weight to kilograms if it was entered in pounds
        if weight_unit == 'lbs':
            weight = weight * 0.45359237

        # Convert height to meters if it was entered in feet and inches
        if height_unit == 'ft':
            height = (height * 0.3048) + (inches * 0.0254)
        elif height_unit == 'in':
            height = height * 0.0254

        # Calculate BMI
        bmi = weight / (height * height)

        return bmi

    # Prompt the user for weight input
    weight = float(input("Enter your weight without the unit: "))
    weight_unit = input("Enter the unit of weight (kg/lbs): ")

    # Prompt the user for height input
    height_unit = input("Enter the unit of height (m/ft): ")
    if height_unit == 'ft':
        feet = float(input("Enter the number of feet: "))
        inches = float(input("Enter the number of inches: "))
    else:
        height = float(input("Enter your height without the unit: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Print the calculated BMI
    print("Your BMI is:", bmi)

    # Determine the weight category based on the BMI and print the corresponding message
    if bmi < 18.5:
        print("You are too skinny")
    elif bmi < 25:
        print("You are normal")
    else:
        print("You are FAT AF")







