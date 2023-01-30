def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1*n2

def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    question = "n"
    answer = []
    num3 = []
    while question == "n" or question == "y":
        if question == "y":
            operation_symbol = input("Pick anather operation: ")
            num3 = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            final_answer = calculation_function(answer, num3)
            print(f"{answer} {operation_symbol} {num3} = {final_answer}")
            answer = final_answer
            question = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.: ")


        elif question == "n":

            num1 = float(input("What's the first number?: "))
            num2 = float(input("What's the secend number?: "))
            for symbol in operations:
                print(symbol)

            operation_symbol = input("Pick any operation from the line above: ")

            calculation_function = operations[operation_symbol]
            first_answer = calculation_function(num1, num2)
            answer = first_answer
            print(f"{num1} {operation_symbol} {num2} = {first_answer}")
            question = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.: ")

calculator()

# function = operations["*"]
# function(2,3)