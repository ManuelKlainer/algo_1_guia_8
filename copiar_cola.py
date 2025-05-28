from queue import Queue as Cola
def copiar_cola(cola: Cola) -> Cola:
	res: Cola = Cola()
	lista_aux: list = []
	while (not (cola.empty())):
		lista_aux.append(cola.get())
	for el in lista_aux:
		res.put(el)
		cola.put(el)
	return res
	