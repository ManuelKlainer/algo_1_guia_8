from queue import LifoQueue as Pila
from copiar_pila import copiar_pila

def invertir_pila(p: Pila[int]) -> Pila[int]:
    lista : list[int] = []
    elem: int
    while not p.empty():
        elem = p.get()
        lista.append(elem)
    for el in lista:
        p.put(el)  # reponer en la original
    res: Pila[int] = Pila()
    for i in range(len(lista)-1, -1, -1):
        res.put(lista[i])
    return res

def intercalar(p1: Pila[int], p2: Pila[int]) -> Pila[int]:
    p1_copia: Pila[int] = copiar_pila(p1)
    p2_copia: Pila[int] = copiar_pila(p2)

    p1_inv: Pila[int] = invertir_pila(p1_copia)
    p2_inv: Pila[int] = invertir_pila(p2_copia)

    res: Pila[int] = Pila()
    e1: int
    e2: int
    while not p1_inv.empty() and not p2_inv.empty():
        e1 = p1_inv.get()
        res.put(e1)
        e2 = p2_inv.get()
        res.put(e2)
    return res

# Prueba
p1: Pila[int] = Pila()
p2: Pila[int] = Pila()
for x in [9, 7, 5, 3, 1]:
    p1.put(x)
for x in [10, 8, 6, 4, 2]:
    p2.put(x)

res: Pila[int] = intercalar(p1, p2)

while not res.empty():
    print(res.get())
