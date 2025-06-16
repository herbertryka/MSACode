def main():
    #while True
    while True:
        #get math expression input from user
        expression = input("Enter expression here: ")
        #use the split method to get parts of the expression
        expression_parts = expression.split(" ")
        #check the length of the list returned from .split
        #if len(list) not = 3
        if len(expression_parts) not in [3]:
            #output an incorrect formay message and reprompt(continue)
            print("ERROR: Please format your expression correctly")
        #try
        try:
            #get x and y and z value from the list
            x = expression_parts[0]
            z = expression_parts[2]
            #and check if X and Z are integers by concerting to int
        #except:
            #output error message and reprompt(continue)
        
        #check that operator is either +, -, *, or /
        #if operator not in [+, -, *, or /]
            #output error message
            #reprompt user (continue)
        #determine the operation to carry out based on the value of the operator
        #use if/elif/else block to carry out the operation





    
    x = expression_parts[0]
    y = expression_parts[1]
    z = expression_parts[2]
main()