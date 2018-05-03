# import prog4_1
# import prog4_2
# from prog4_2 import StackMachine
# s = StackMachine()
# s.Execute(prog4_1.Parse(prog4_1.Tokenize("push 5")))


class StackMachine:

    def __init__(self):
        self._data = []
        self._Memory = {}
        self.CurrentLine = 0


    def Execute(self, Token):
        #print(self._data)
        self.CurrentLine += 1
        
        if(Token[0] == "push"):
            self._data.append(int(Token[1]))
            return

        elif(Token[0] == "pop"):
            if(len(self._data) == 0):
                raise IndexError("Invalid Memory Access")
            else:
                return self._data.pop()

        elif(Token[0] == "add"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _sum = first + second
                self._data.append(_sum)
                return
            
        elif(Token[0] == "sub"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _dif = first - second
                self._data.append(_dif)
                return

        elif(Token[0] == "mul"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _prod = first * second
                self._data.append(_prod)
                return

        elif(Token[0] == "div"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _quo = first / second
                self._data.append(_quo)
                return

        elif(Token[0] == "mod"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _mod = first % second
                self._data.append(_mod)
                return

        elif(Token[0] == "skip"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                if(first == 0):
                    self.CurrentLine += second
                return
            
        elif(Token[0] == "save"):
            if(len(self._data) == 0):
                raise IndexError("Invalid Memory Access")
            else:
                saveVal = self._data.pop()
                loc = int(Token[1])
                self._Memory[loc] = saveVal
                return

        elif(Token[0] == "get"):
            loc = int(Token[1])
            if(loc in self._Memory):
                saveVal = self._Memory[loc]
                self._data.append(saveVal)
                return
            else:
                raise IndexError("Invalid Memory Access")
            



        
            
            
