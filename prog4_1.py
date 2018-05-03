#python3
#import prog4_1
#prog4_1.Tokenize("push pop hello")

_validTokens = ["push","pop","add","sub","mul","div","mod","skip","save","get"]
_valTokSize1 = ["pop","add","sub","mul","div","mod","skip"]
_valTokSize2 = ["push","save","get"]

def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def Tokenize(line):

    Token = line.split()

    for i in range(0,len(Token)):
        subTok = Token[i]
        if(not subTok in _validTokens and not isNumber(subTok)):
            raise ValueError("Unexpected Token: " + subTok)

    return Token

def Parse(Token):

    if(Token[0] in _valTokSize1 and len(Token) == 1):
        return True
    elif(Token[0] in _valTokSize2 and len(Token) == 2 and isNumber(Token[1])):
        return True

    return False

    

    





