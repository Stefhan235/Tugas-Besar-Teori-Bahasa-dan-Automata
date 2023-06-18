def lexicalAnalyzer(string):
    i = 0
    state = 0

    while (i < len(string)): 
        if (state == 0):
            if (string[i] == 'd'):
                state = 1
            elif (string[i] == 'w'):
                state = 2
            elif (string[i] == 't'):
                state = 5
            elif (string[i] == 'f'):
                state = 7
            elif (string[i] == '{') or (string[i] == '}') or (string[i] == ';') or (string[i] == '(') or (string[i] == ')') or (string[i] == 'a') or (string[i] == 'b') or (string[i] == '+') or (string[i] == '-') or (string[i] == '/') or (string[i] == '*') or (string[i] == '%'):
                state = 13
            elif (string[i] == '=') or (string[i] == '>') or (string[i] == '<'):
                state = 11
            elif (string[i] == '!'):
                state = 12
            else:
                state = -1
        
        elif (state == 1):
            if (string[i] == 'o'):
                state = 13
            else:
                state = -1
        
        elif (state == 2):
            if (string[i] == 'h'):
                state = 3
            else:
                state = -1
            
        elif (state == 3):
            if (string[i] == 'i'):
                state = 4
            else:
                state = -1
        
        elif (state == 4):
            if (string[i] == 'l'):
                state = 10
            else: 
                state = -1
        
        elif (state == 5):
            if (string[i] == 'r'):
                state = 6
            else: 
                state = -1

        elif (state == 6):
            if (string[i] == 'u'):
                state = 10
            else: 
                state = -1
        
        elif (state == 7):
            if (string[i] == 'a'):
                state = 8
            else: 
                state = -1
        
        elif (state == 8):
            if (string[i] == 'l'):
                state = 9
            else: 
                state = -1
        
        elif (state == 9):
            if (string[i] == 's'):
                state = 10
            else: 
                state = -1

        elif (state == 10):
            if (string[i] == 'e'):
                state = 13
            else: 
                state = -1
        
        elif (state == 11):
            if (string[i] == '='):
                state = 13
            else: 
                state = -1
        
        elif (state == 12):
            if (string[i] == '='):
                state = 13
            else: 
                state = -1

        i = i + 1
    
    if (state == 13) or (state == 11):
        return True
    else:
        return False


def parser(syntax):
    stack = []
    state = 'i'
    stack.append('#')
    state = 'p'
    stack.append("statement")
    state ='q'

    head = 0
    if head < len(syntax): 
        symbol = syntax[head]

    topOfStack = stack[-1]
    
    while (topOfStack != "#") and (state != "error"): 
        if (topOfStack == "statement"):
            if (symbol == "do"):
                stack.pop()
                stack.append(";")
                stack.append(")")
                stack.append("kondisi")
                stack.append("(")
                stack.append("while")
                stack.append("}")
                stack.append(";")
                stack.append("aksi")
                stack.append("{")
                stack.append("do")
            else:
                state = "error"
        
        elif (topOfStack == "aksi"):
            if (symbol == "a") or (symbol == "b"):
                stack.pop()
                stack.append("variabel")
                stack.append("operator")
                stack.append("variabel")
                stack.append("=")
                stack.append("variabel")
            else:
                state = "error"

        elif (topOfStack == "kondisi"):
            if (symbol == "a") or (symbol == "b"):
                stack.pop()
                stack.append("variabel")
                stack.append("comparator")
                stack.append("variabel")
            elif (symbol == "true"):
                stack.pop()
                stack.append("true")
            elif (symbol == "false"):
                stack.pop()
                stack.append()
            else:
                state = "error"

        elif (topOfStack == "variabel"):
            if (symbol == "a"):
                stack.pop()
                stack.append("a")
            elif (symbol == "b"):
                stack.pop()
                stack.append("b")
            else:
                state = "error"
        
        elif (topOfStack == "operator"):
            if (symbol == "+"):
                stack.pop()
                stack.append("+")
            elif (symbol == "-"):
                stack.pop()
                stack.append("-")
            elif (symbol == "*"):
                stack.pop()
                stack.append("*")
            elif (symbol == "/"):
                stack.pop()
                stack.append("/")
            elif (symbol == "%"):
                stack.pop()
                stack.append("%")
            else:
                state = "error"
        
        elif (topOfStack == "comparator"):
            if (symbol == "=="):
                stack.pop()
                stack.append("==")
            elif (symbol == "!="):
                stack.pop()
                stack.append("!=")
            elif (symbol == ">"):
                stack.pop()
                stack.append(">")
            elif (symbol == ">="):
                stack.pop()
                stack.append(">=")
            elif (symbol == "<"):
                stack.pop()
                stack.append("<")
            elif (symbol == "<="):
                stack.pop()
                stack.append("<=")
            else:
                state = "error"

        elif (topOfStack == "do"):
            if (symbol == "do"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else: 
                state = "error"
                
        elif (topOfStack == "{"):
            if (symbol == "{"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head] 
            else:
                state = "error"
        
        elif (topOfStack == "}"):
            if (symbol == "}"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"

        elif (topOfStack == ";"):
            if (symbol == ";"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"

        elif (topOfStack == "while"):
            if (symbol == "while"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"

        elif (topOfStack == "("):
            if (symbol == "("):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == ")"):
            if (symbol == ")"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "a"):
            if (symbol == "a"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"

        elif (topOfStack == "b"):
            if (symbol == "b"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "+"):
            if (symbol == "+"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "-"):
            if (symbol == "-"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"

        elif (topOfStack == "*"):
            if (symbol == "*"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "/"):
            if (symbol == "/"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "%"):
            if (symbol == "%"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"

        elif (topOfStack == "true"):
            if (symbol == "true"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"

        elif (topOfStack == "false"):
            if (symbol == "false"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "=="):
            if (symbol == "=="):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "!="):
            if (symbol == "!="):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == ">"):
            if (symbol == ">"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == ">="):
            if (symbol == ">="):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "<"):
            if (symbol == "<"):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "<="):
            if (symbol == "<="):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
        
        elif (topOfStack == "="):
            if (symbol == "="):
                stack.pop()
                head = head + 1
                if head < len(syntax): 
                    symbol = syntax[head]
            else:
                state = "error"
             
        topOfStack = stack[-1]

    if (state != "error"):
        stack.pop()
        state = "f"
    
    if (state != "f"):
        return False
    
    return True

def main():
    syntaxInput = input("Input C++ Syntax : ")
    splitSyntax = syntaxInput.split()
    lexicalAnalyzerOutput = lexicalAnalyzer(syntaxInput)
    parserOutput = parser(splitSyntax)

    if (lexicalAnalyzerOutput) and (parserOutput):
        print("Lexical Analyzer : Valid")
        print("Parser           : Valid")
    elif (not lexicalAnalyzerOutput) and (parserOutput):
        print("Lexical Analyzer : Invalid")
        print("Parser           : Valid")
    elif (lexicalAnalyzerOutput) and (not parserOutput):
        print("Lexical Analyzer : Valid")
        print("Parser           : Invalid")
    elif (not lexicalAnalyzerOutput) and (not parserOutput):
        print("Lexical Analyzer : Invalid")
        print("Parser           : Invalid")
    
if __name__ == '__main__':
    main()