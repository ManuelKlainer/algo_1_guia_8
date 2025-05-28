from queue import LifoQueue as Pila
historiales:dict[str,Pila[str]] = {}

def visitar_sitio(historiales:dict[str,Pila[str]], usuario: str, sitio:str):
	if usuario in historiales:
		historial: Pila[str] = historiales[usuario]
		historial.put(sitio)
		historiales[usuario] = historial
	else:
		historial: Pila[str] = Pila()
		historial.put(sitio)
		historiales[usuario] = historial

def navegar_atras(historiales:dict[str,Pila[str]], usuario: str) -> str:
	historial: Pila[str] = historiales[usuario]
	ultimo_sitio: str = historial.get()
	historiales[usuario] = historial
	return ultimo_sitio

