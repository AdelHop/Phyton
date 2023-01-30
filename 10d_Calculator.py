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
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the secend number?: "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick any operation from the line above: ")

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick anather operation from the line above: ")
num3 =  int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
secend_answer = calculation_function(calculation_function(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {secend_answer}")

# function = operations["*"]
# function(2,3)