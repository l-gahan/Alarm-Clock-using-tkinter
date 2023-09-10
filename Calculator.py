result=0
operandInput=None

while __name__=="__main__" :
    if operandInput!="=":
        userInput=int(input("insert number: "))
    if operandInput==None:
        result=userInput

    elif operandInput == "/":
        result=int(result/userInput)

    elif operandInput == "*":
        
        result=result*userInput
    elif operandInput == "+":
        
        result=result+userInput
    elif operandInput == "-":
        
        result=result-userInput
    print("\t"+str(result))
    
    operandInput=input("insert operand: ")
    print("\t"+operandInput)
    if operandInput == "=":
        print(result)
