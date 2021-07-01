def operation(symbol, num1, num2):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "/":
        return num1/num2
    elif symbol == "*":
        return num1*num2   

def main():
    print("Welcome to the Calculator App.")
    num1 = float(input("What's the first number? "))
    c = "y"

    while c == "y":
        print("""
        +
        -
        *
        /
        """)
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        result = operation(op_symbol,num1,num2)
        print(f"{num1} {op_symbol} {num2}  = {result}")
        num1 = result
        c = input(f"Type 'y' to continue calculatinf with {result}, or type 'n' to start a new calculation.")
        if c == "n":
            main()

main()