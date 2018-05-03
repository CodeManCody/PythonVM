
import sys
import prog4_1
import prog4_2
from prog4_2 import StackMachine

def main():

    print("Assignment #4-3, Cody Morgan, codymorgan89@gmail.com")

    _procLines = []

    s = StackMachine()

    with open(sys.argv[1],mode='r') as f:
        lines = [x.strip() for x in f.readlines()]

        for i in range(0,len(lines)):
            line = lines[i]
            try:
                _procLines.append(prog4_1.Tokenize(line))
            except ValueError as e:
                print("Error on line " + str(i+1) + ": " + str(e))
                return
                
        for i in range(0,len(lines)):
            line = lines[i]
            if(not prog4_1.Parse(_procLines[i])):
                print("Parse error on line " + str(i+1) + ": " + str(lines[i]))
                return

    while(s.CurrentLine < len(_procLines)):
        if(s.CurrentLine < 0):
            print("Trying to execute invalid line: " + s.CurrentLine)
            return
        try:
            v = s.Execute(_procLines[s.CurrentLine])
            if(v != None):
                print(v)
        except IndexError:
            print("Line " + str(s.CurrentLine) + ": " + lines[s.CurrentLine-1] + "  caused Invalid Memory Access")
            return

    print("Program terminated correctly")

if __name__ == "__main__":
    main()

            
            
            
