def main():
    #while True
    while True:
        #get math expression input from user
        expression = input("Enter expression here(using +, -, *, or /): ")
        #use the split method to get parts of the expression
        expression_parts = expression.split(" ")
        #check the length of the list returned from .split
        #if len(list) not = 3
        if not len(expression_parts) == 3:
            #output an incorrect formay message and reprompt(continue)
            print("ERROR: Please format your expression correctly")
        #try
        try:
            #get x and y and z value from the list
            #and check if X and Z are integers by concerting to int
            x = int(expression_parts[0])
            z = int(expression_parts[2])
           
        #except:
        except:
            #output error message and reprompt(continue)
            print("ERROR: Please enter valid characters")
            continue
        #check that operator is either +, -, *, or /
        #if operator not in [+, -, *, or /]
        y = expression_parts[1]
        operator_sign = y
            #output error message
            #reprompt user (continue)
        if operator_sign not in ["+", "-", "*", "/"]:
            print("ERROR: Please enter a valid operator")
            continue
        #determine the operation to carry out based on the value of the operator
        #use if/elif/else block to carry out the operation
        if (operator_sign == '+'):
            answer = x + z
            print(f"{x} + {z} = {answer: .1f} ")
        elif (operator_sign == "-"):
            answer = x - z
            print(f"{x} - {z} = {answer: .1f}")
        elif (operator_sign == "/"):
            if (z == 0):
                print("ERROR: Cannot divide by 0")
                continue
            answer = x / z
            print(f"{x} / {z} = {answer: .1f}")
        else:
            answer = x * z
            print(f"{x} * {z} = {answer: .1f}")
# != means not equal
main()