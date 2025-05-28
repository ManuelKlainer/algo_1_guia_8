from queue import LifoQueue as Pila

def invertir_str(s: str):
    res:str = ""
    for i in range(len(s)-1,-1,-1):
        res = res + s[i]
    return res

def esta_bien_balanceada(s: str) -> bool:
    resultado:bool=True
    caracteres: Pila[str]=Pila()
    sInv: str = invertir_str(s)
    parentesisAunAbiertos: int = 0
    for c in sInv:
        caracteres.put(c)
    while not caracteres.empty():
        caracter: str = caracteres.get()
        if caracter == "(":
            parentesisAunAbiertos = parentesisAunAbiertos + 1
        if caracter == ")":
            parentesisAunAbiertos = parentesisAunAbiertos - 1
		# Si en algún momento tengo más paréntesis cerrando que abriendo, devuelvo false
        if parentesisAunAbiertos < 0:
            resultado = False
    if parentesisAunAbiertos > 0:
        resultado = False
    return resultado


    