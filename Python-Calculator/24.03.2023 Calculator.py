def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False



def convert_number(string):
    if is_number(string):
        return float(string)



def ask_for_number(force_valid_input):
    while True:
        input_user = input("Give the number: ")
        if is_number(input_user):
            return float(input_user)
        if not force_valid_input:
            return None
        print("This didn't look like a number, try again.")



def is_valid_operator(operator):
    if operator in ["+","-","*","/"]:
        return True
    return False



def ask_for_an_operator(force_valid_input):
    while True:
        operator =input("Please provide an operator (one of +, -, *, /): ")
        if is_valid_operator(operator):
            return operator
        else:
            if not force_valid_input:
                return None
            print("Unknown operator.")



def calc(operator,a,b):
    result = None
    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return result
    elif operator == "+":
            result = a + b
    elif operator == "-":
            result = a - b
    elif operator == "*":
            result = a * b
    elif operator == "/":
        try:
            result = a / b
        except ZeroDivisionError:
            print("Division by zero ")
    return result

def simple_calculator():
    while True:
        a = ask_for_number(force_valid_input=False)
        if a is None:
            exit()
        else:
            operator = ask_for_an_operator(force_valid_input = True)
            b = ask_for_number(force_valid_input=True)
            result = calc(operator,a,b)
            if result is not None:
                print(f'The result is {result}.')

if __name__ == "__main__":
    simple_calculator()

