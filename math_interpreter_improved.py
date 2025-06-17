"""
Function to get valid expression inputs from the user
Input: None
Outputs: (int)X, (int)Z, (string)Y
"""
def get_valid_expression_inputs():
    while True:
        expression = input("Enter expression here: ")
        #get math expression input from user
        #use the split method to get parts of the expression
        expression_parts = expression.split(" ")
        #check the length of the list returned from .split
        #if len(list) not = 3
        if not len(expression_parts) == 3:
            #output an incorrect formay message and reprompt(continue)
            print("ERROR: Please format your expression correctly")
        try:
            #get x and y and z value from the list
                #and check if X and Z are integers by concerting to int
                x = int(expression_parts[0])
                z = int(expression_parts[2])
                y = str(expression_parts[1])
        except:
            #output error message and reprompt(continue)
            print("ERROR: Please enter valid characters")
            continue
        if y not in ["+", "-", "*", "/"]:
            print("ERROR: Please enter a valid operator")
            continue
        if (y == "/" and z == 0):
            print("ERROR: Cannot divide by 0")
            continue
        return x, y, z
"""
Function to evaluate an expression
Input: (int)X, (string)Y, (int)Z
Output: Answer
"""
def evaluate_expression(x:int, y:str, z:int):
    if (y == '+'):
            answer = x + z
    elif (y == "-"):
            answer = x - z
    elif (y == "/"):
        if (z == 0):
            print("ERROR: Cannot divide by 0")
        answer = x / z
    else:
            answer = x * z
    return answer


def main():
    while True:
        #call the get_invalid_expression_inputs function to get x, y, and z
        x, y, z = get_valid_expression_inputs()

        #call evaluate_expression to get the answer for the expression
        answer = evaluate_expression(x, y, z)
        #print the answer
        print(f"{x} {y} {z} = {answer: .1f}")
        #ask the user if they want to evaluate another expression
        #rerun the program if the user wants to continue, otherwise, end the program
        do_again = input("Would you like to evaluate another expression? Enter y to continue: ")
        if do_again == "y" or do_again == "Y":
            continue
        else:
             break
main()