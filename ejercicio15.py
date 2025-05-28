from queue import Queue as Cola
from copiar_cola import copiar_cola

def es_prioritario(cliente: tuple[str,int,bool,bool]) -> bool:
	_, _, _, prioritario = cliente
	return prioritario

def es_preferencial(cliente: tuple[str,int,bool,bool]) -> bool:
	_, _, preferencial, _ = cliente
	return preferencial


def atencion_a_clientes(c: Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
	c2: Cola[tuple[str,int,bool,bool]] = copiar_cola(c)
	prioritarios: Cola[tuple[str,int,bool,bool]]=Cola()
	preferenciales: Cola[tuple[str,int,bool,bool]]=Cola()
	clientes: Cola[tuple[str,int,bool,bool]]=Cola()
	res: Cola[tuple[str,int,bool,bool]]=Cola()

	while not c.empty():
		cliente:tuple[str,int,bool,bool] = c2.get()
		if es_prioritario(cliente):
			prioritarios.put(cliente)
		elif es_preferencial(cliente):
			preferenciales.put(cliente)
		else:
			clientes.put(cliente)
		
	while not prioritarios.empty():
		res.put(prioritarios.get())
	while not preferenciales.empty():
		res.put(preferenciales.get())
	while not clientes.empty():
		res.put(clientes.get())
	return res