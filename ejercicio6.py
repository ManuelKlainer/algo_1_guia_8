from queue import LifoQueue as Pila
def split(s: str, c: str) -> list[str]:
    res:list[str] = []
    acum:str = ""
    for ch in s:
        if ch == c:
            res.append(acum)
            acum = ""
        else:
            acum = acum + ch
    if not acum == "":
        res.append(acum)
    return res
                        

def evaluar_expresion(s: str) -> float:
    
    tokens: list[str] = s.split(" ")
    operandos : Pila[float] = Pila()
    
    for token in tokens:
        if not (token in ['+','-','*','/']):
            operandos.put(float(token))
        else:
            n2 = operandos.get()
            n1 = operandos.get()
            if token == '+':
                operandos.put(n1 + n2)
            if token == '-':
                operandos.put(n1 - n2)
            if token == '*':
                operandos.put(n1 * n2)
            if token == '/':
                operandos.put(n1 / n2)
    return operandos.get()



expresion: str = "3 4 + 5 * 2 -"
resultado: float = evaluar_expresion(expresion)
print(resultado)