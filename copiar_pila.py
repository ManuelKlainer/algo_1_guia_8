from queue import LifoQueue as Pila
def copiar_pila(p: Pila):
    p_aux: Pila = Pila()
    p_copia: Pila = Pila()
    while (not p.empty()):
        el = p.get()
        p_aux.put(el)
    while (not p_aux.empty()):
        el = p_aux.get()
        p.put(el)
        p_copia.put(el)
    return p_copia