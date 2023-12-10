import sys
from abc import ABC, abstractmethod



class PrePro:

    def filter(code):
        code = code.split("\n")
        for i in range(len(code)):
            if "//" in code[i]:
                code[i] = code[i].split("//")[0]
        code = "\n".join(code)
        return code


class Node:
    def __init__(self, value, children: list):
        self.value = value
        self.children = children

    @abstractmethod
    def Evaluate(self, symbolTable):
        pass

class BinOp(Node):
    def Evaluate(self, symbolTable):
        dir = self.children[1].Evaluate(symbolTable)
        esq = self.children[0].Evaluate(symbolTable)
        if self.value == "+" and esq[0] == "inteiro" and dir[0] == "inteiro":
            return (('int', esq[1] + dir[1]))
        elif self.value == "-" and esq[0] == "inteiro" and dir[0] == "inteiro":
            return (('int', esq[1] - dir[1]))
        elif self.value == "*" and esq[0] == "inteiro" and dir[0] == "inteiro":
            return (('int', esq[1] * dir[1]))
        elif self.value == "/" and esq[0] == "inteiro" and dir[0] == "inteiro":
            return (('int', esq[1] // dir[1]))
        elif self.value == "==" and esq[0] == dir[0]:
            return (('int', int(esq[1] == dir[1])))
        elif self.value == "||" and esq[0] == "inteiro" and dir[0] == "inteiro":
            return (('int', int(esq[1] or dir[1])))
        elif self.value == "&&" and esq[0] == "inteiro" and dir[0] == "inteiro":
            return (('int', int(esq[1] and dir[1])))
        elif self.value == ">" and esq[0] == dir[0]:
            return (('int', int(esq[1] > dir[1])))
        elif self.value == "<" and esq[0] == dir[0]:
            return (('int', int(esq[1] < dir[1])))
        elif self.value == '.':
            return (('string', str(esq[1]) + str(dir[1])))
        else:
            raise Exception("Invalid syntax")
        

class UnOp(Node):
    def Evaluate(self, symbolTable):
        if self.value == "+" and self.children[0].Evaluate(symbolTable)[0] == "inteiro":
            return ('int', +self.children[0].Evaluate(symbolTable)[1])
        elif self.value == "-" and self.children[0].Evaluate(symbolTable)[0] == "inteiro":
            return ('int', -self.children[0].Evaluate(symbolTable)[1])
        elif self.value == "!" and self.children[0].Evaluate(symbolTable)[0] == "inteiro":
            return ('int', int(not self.children[0].Evaluate(symbolTable)[1]))
        else:
            raise Exception("Invalid syntax")
        
class IntVal(Node):
    def Evaluate(self, symbolTable):
        return ('int', self.value)
    
class NoOp(Node):
    def Evaluate(self, symbolTable):
        pass

class Token:
    def __init__(self,type, value):
        self.type = type
        self.value = value

class Tokenizer:

    comands = ["imprimir", "se", "senao", "para", "entrada", "var", "inteiro", "texto"]
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None
    
    def selectNext(self):
        if self.position < len(self.source):
            element = self.source[self.position]
            n = ""
            if element == " " or element == "\t": 
                self.position += 1
                self.selectNext()
            elif element.isdigit():
                while self.position < len(self.source):
                    n += element
                    if self.position + 1 < len(self.source) and self.source[self.position + 1].isdigit():
                        self.position += 1
                        element = self.source[self.position]
                    else:
                        self.position += 1
                        break
                self.next = Token("inteiro", int(n))
            elif self.source[self.position] == "/":
                self.next = Token("DIV", element)
                self.position += 1
            elif element == "*":
                self.next = Token("MULT", element)
                self.position += 1
            elif element == "+":
                self.next = Token("PLUS", element)
                self.position += 1
            elif element == "-":
                self.next = Token("MINUS", element)
                self.position += 1
            elif element == "(":
                self.next = Token("OPEN_Par", element)
                self.position += 1
            elif element == ")":
                self.next = Token("CLOSE_par", element)
                self.position += 1
            elif element == "=":
                if self.position + 1 < len(self.source) and self.source[self.position + 1] == "=":
                    self.next = Token("EQUAL_EQUAL", "==")
                    self.position += 2
                else:
                    self.next = Token("EQUAL", element)
                    self.position += 1
            elif element == "\n":
                self.next = Token("EOL", "\n")
                self.position += 1
            elif element.isalpha():
                while self.position < len(self.source):
                    n += element
                    if self.position + 1 < len(self.source) and self.source[self.position + 1].isalpha() or self.source[self.position + 1].isdigit() or self.source[self.position + 1] == "_":
                        self.position += 1
                        element = self.source[self.position]
                    else:
                        self.position += 1
                        break
                if n in Tokenizer.comands:
                    self.next = Token("COMAND", n)
                else:	
                    self.next = Token("ID", n)
            elif element == "_":
                while self.position < len(self.source):
                    n += element
                    if self.position + 1 < len(self.source) and self.source[self.position + 1].isalpha():
                        self.position += 1
                        element = self.source[self.position]
                    else:
                        self.position += 1
                        break
                self.next = Token("ID", n)
            elif element == "|" and self.position + 1 < len(self.source) and self.source[self.position + 1] == "|":
                self.next = Token("OR", "||")
                self.position += 2
            elif element == "&" and self.position + 1 < len(self.source) and self.source[self.position + 1] == "&":
                self.next = Token("AND", "&&")
                self.position += 2
            elif element == "!":
                self.next = Token("NOT", element)
                self.position += 1
            elif element == ">":
                self.next = Token("GREATER", element)
                self.position += 1
            elif element == "<":
                self.next = Token("LESS", element)
                self.position += 1
            elif element == "{":
                self.next = Token("OPEN_BRACE", element)
                self.position += 1
            elif element == "}":
                self.next = Token("CLOSE_BRACE", element)
                self.position += 1
            elif element == ";":
                self.next = Token("SEMICOLON", element)
                self.position += 1
            elif element == '"':
                string = ""
                self.position += 1
                while self.position < len(self.source) and self.source[self.position] != '"':
                    string += self.source[self.position]
                    self.position += 1
                self.next = Token("texto", string)
                self.position += 1
            elif element == ".":
                self.next = Token("CONCAT", element)
                self.position += 1
            else:
                raise ValueError("Erro")
        else:
            self.next = Token("EOF", "")

class Print(Node):
    def Evaluate(self, symbolTable):
        print(self.children[0].Evaluate(symbolTable))

class If(Node):
    def Evaluate(self, symbolTable):
        if self.children[0].Evaluate(symbolTable):
            self.children[1].Evaluate(symbolTable)
        elif len(self.children) == 3:
            self.children[2].Evaluate(symbolTable)

class For(Node):
    def Evaluate(self, symbolTable):
        self.children[0].Evaluate(symbolTable)
        while self.children[1].Evaluate(symbolTable) == ('int', 1):
            self.children[3].Evaluate(symbolTable)
            self.children[2].Evaluate(symbolTable)

class Scanln(Node):
    def Evaluate(self, symbolTable):
        return ('int', int(input()))

class SymbolTable:
    symbolTable = {}

    def set(self, name, value):
        if value[0] == self.symbolTable[name][0]:
            if name not in self.symbolTable:
                raise NameError(f"Erro")
            self.symbolTable[name] = value
        else:
            raise TypeError(f"Erro")

    def get(self, name):
        if name not in self.symbolTable:
            raise NameError(f"Erro")
        return self.symbolTable[name]
    
    def create(self, name, type):
        if name in self.symbolTable:
            raise NameError(f"Erro")
        self.symbolTable[name] = (type, None)

class Assigment(Node):
    def Evaluate(self, symbolTable):
        return symbolTable.set(self.children[0].value, self.children[1].Evaluate(symbolTable))

class block(Node):
    def Evaluate(self, symbolTable):
        for i in self.children:
            i.Evaluate(symbolTable)

class identifier(Node):
    def Evaluate(self, symbolTable):
        return symbolTable.get(self.value)
    
class VarDec(Node):
    def Evaluate(self, symbolTable):
        if len(self.children) == 2:
            symbolTable.create(self.children[0].value, self.value)
            symbolTable.set(self.children[0].value, self.children[1].Evaluate(symbolTable))
        else:
            symbolTable.create(self.children[0].value, self.value)

class StringVal(Node):
    def Evaluate(self, symbolTable):
        return ('string', self.value)
    
class program(Node):
    def Evaluate(self, symbolTable):
        for i in self.children:
            i.Evaluate(symbolTable)

class Parser:
    tokenizer = None

    def parse_program():
        r = program("", [])
        while Parser.tokenizer.next.type != "EOF":
            r.children.append(Parser.parse_statement())
        return r

    def parse_expression():
        r = Parser.parse_term()
        while Parser.tokenizer.next.type == "PLUS" or Parser.tokenizer.next.type == "MINUS" or Parser.tokenizer.next.type == "CONCAT":
            if Parser.tokenizer.next.type == "PLUS":
                Parser.tokenizer.selectNext()
                r = BinOp("+", [r, Parser.parse_term()])
            elif Parser.tokenizer.next.type == "MINUS":
                Parser.tokenizer.selectNext()
                r = BinOp("-", [r, Parser.parse_term()])
            elif Parser.tokenizer.next.type == "CONCAT":
                Parser.tokenizer.selectNext()
                r = BinOp(".", [r, Parser.parse_term()])
            else:
                raise Exception("Invalid syntax")
        return r

    def parse_term():
        r = Parser.parse_factor()
        while Parser.tokenizer.next.type == "DIV" or Parser.tokenizer.next.type == "MULT":
            if Parser.tokenizer.next.type == "DIV":
                Parser.tokenizer.selectNext()
                r = BinOp("/", [r, Parser.parse_factor()])
            elif Parser.tokenizer.next.type == "MULT":
                Parser.tokenizer.selectNext()
                r = BinOp("*", [r, Parser.parse_factor()])
            else:
                raise Exception("Invalid syntax")
        return r

    def parse_factor():
        resp = None
        if Parser.tokenizer.next.type == "inteiro":
            resp = IntVal(Parser.tokenizer.next.value, [])
            Parser.tokenizer.selectNext()
            return resp
        
        elif Parser.tokenizer.next.type == "PLUS":
            Parser.tokenizer.selectNext()
            resp = UnOp("+", [Parser.parse_factor()])
            return resp
        
        elif Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.selectNext()
            resp = UnOp("-", [Parser.parse_factor()])
            return resp
        
        elif Parser.tokenizer.next.type == "OPEN_Par":
            Parser.tokenizer.selectNext()
            resp = Parser.parse_bool_expression()
            if Parser.tokenizer.next.type == "CLOSE_par":
                Parser.tokenizer.selectNext()
                return resp
            else:
                raise Exception("Invalid syntax")
            
        elif Parser.tokenizer.next.value == "texto":
            r = StringVal(Parser.tokenizer.next.value, [])
            Parser.tokenizer.selectNext()
            return r
        
        elif Parser.tokenizer.next.type == "ID":
            resp = identifier(Parser.tokenizer.next.value, [])
            Parser.tokenizer.selectNext()
            return resp
        
        elif Parser.tokenizer.next.type == "NOT":
            Parser.tokenizer.selectNext()
            resp = UnOp("!", [Parser.parse_factor()])
            return resp
        
        elif Parser.tokenizer.next.value == "entrada":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OPEN_Par":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "CLOSE_par":
                    Parser.tokenizer.selectNext()
                    resp = Scanln("entrada", [])
                    return resp
                else:
                    raise Exception("Invalid syntax")
            else:
                raise Exception("Invalid syntax")
        else:
            raise Exception("Invalid syntax")
        
    def parse_statement():
        r = None
        if Parser.tokenizer.next.type == "COMAND":
            if Parser.tokenizer.next.value == "imprimir":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "OPEN_Par":
                    Parser.tokenizer.selectNext()
                    r = Print("", [Parser.parse_bool_expression()])
                    if Parser.tokenizer.next.type == "CLOSE_par":
                        Parser.tokenizer.selectNext()
                        return r
                    else:
                        raise Exception("Invalid syntax")
                else:
                    raise Exception("Invalid syntax")
            elif Parser.tokenizer.next.value == "se":
                Parser.tokenizer.selectNext()
                r = If("se", [Parser.parse_bool_expression()])
                r.children.append(Parser.parse_block())
                if Parser.tokenizer.next.value == "senao":
                    Parser.tokenizer.selectNext()
                    r.children.append(Parser.parse_block())
                if Parser.tokenizer.next.type == "EOL":
                    Parser.tokenizer.selectNext()
                    return r
                else:
                    raise Exception("Invalid syntax")
                
            elif Parser.tokenizer.next.value == "para":
                Parser.tokenizer.selectNext()
                r = For("para", [Parser.parse_assignment()])
                if Parser.tokenizer.next.type == "SEMICOLON":
                    Parser.tokenizer.selectNext()
                    r.children.append(Parser.parse_bool_expression())
                    if Parser.tokenizer.next.type == "SEMICOLON":
                        Parser.tokenizer.selectNext()
                        r.children.append(Parser.parse_assignment())
                        r.children.append(Parser.parse_block())
                        if Parser.tokenizer.next.type == "EOL":
                            Parser.tokenizer.selectNext()
                            return r
                        else:
                            raise Exception("Invalid syntax")
                    else:
                        raise Exception("Invalid syntax")
                else:
                    raise Exception("Invalid syntax")
                

            elif Parser.tokenizer.next.value == "var":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "ID":
                    var = identifier(Parser.tokenizer.next.value, [])
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.value == "texto" or Parser.tokenizer.next.value == "inteiro":
                        r = VarDec(Parser.tokenizer.next.value, [var])
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "EOL":
                            Parser.tokenizer.selectNext()
                            return r
                        elif Parser.tokenizer.next.type == "EQUAL":
                            Parser.tokenizer.selectNext()
                            r.children.append(Parser.parse_bool_expression())
                        else:
                            raise Exception("Invalid syntax")
                    else:
                        raise Exception("Invalid syntax")
            else:
                raise Exception("Invalid syntax")
        elif Parser.tokenizer.next.type == "ID":
            var = identifier(Parser.tokenizer.next.value, [])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "EQUAL":
                Parser.tokenizer.selectNext()
                r = Assigment("", [var, Parser.parse_bool_expression()])
                if Parser.tokenizer.next.type == "EOL":
                    Parser.tokenizer.selectNext()
                    return r
                else:
                    raise Exception("Invalid syntax")
            else:
                raise Exception("Invalid syntax")
        elif Parser.tokenizer.next.type == "EOL":
            Parser.tokenizer.selectNext()
            return NoOp("", [])
        else:
            raise Exception("Invalid syntax")
        
        
    def parse_block():
        if Parser.tokenizer.next.type == "OPEN_BRACE":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "EOL":
                Parser.tokenizer.selectNext()
                r = block("", [])
                while Parser.tokenizer.next.type != "CLOSE_BRACE":
                    r.children.append(Parser.parse_statement())
                if Parser.tokenizer.next.type == "CLOSE_BRACE":
                    Parser.tokenizer.selectNext()
                    return r
                else:
                    raise Exception("Invalid syntax")
    
    def parse_bool_expression():
        r = Parser.parse_bool_term()
        while Parser.tokenizer.next.type == "OR":
            Parser.tokenizer.selectNext()
            r = BinOp("||", [r, Parser.parse_bool_term()])
        return r
    
    def parse_bool_term():
        r = Parser.parse_rel_expression()
        while Parser.tokenizer.next.type == "AND":
            Parser.tokenizer.selectNext()
            r = BinOp("&&", [r, Parser.parse_rel_expression()])
        return r
    
    def parse_rel_expression():
        r = Parser.parse_expression()
        while Parser.tokenizer.next.type == "EQUAL_EQUAL" or Parser.tokenizer.next.type == "GREATER" or Parser.tokenizer.next.type == "LESS":
            if Parser.tokenizer.next.type == "EQUAL_EQUAL":
                Parser.tokenizer.selectNext()
                r = BinOp("==", [r, Parser.parse_expression()])
            elif Parser.tokenizer.next.type == "GREATER":
                Parser.tokenizer.selectNext()
                r = BinOp(">", [r, Parser.parse_expression()])
            elif Parser.tokenizer.next.type == "LESS":
                Parser.tokenizer.selectNext()
                r = BinOp("<", [r, Parser.parse_expression()])
        return r
    
    def parse_assignment():
        if Parser.tokenizer.next.type == "ID":
            id = Parser.tokenizer.next.value
            id_ok = identifier(id, [])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "EQUAL":
                Parser.tokenizer.selectNext()
                bool_expression = Parser.parse_bool_expression()
                return Assigment("=", [id_ok, bool_expression])
            else:
                raise Exception("Invalid syntax")
        else:
            raise Exception("Invalid syntax")



        
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()
        result = Parser.parse_program()
        if Parser.tokenizer.next.type == "EOF":
            return result
            
        else:
            raise TypeError(f"Erro")

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as arquivo:
        cont = arquivo.read()
        cont = PrePro.filter(cont)
    root = Parser.run(cont)
    symbolTable = SymbolTable()
    root.Evaluate(symbolTable)