from queue import Queue as Cola
from copiar_cola import copiar_cola

def intercalar(c1: Cola, c2: Cola) -> Cola:
	res: Cola = Cola()
	while (not (c1.empty())):
		res.put(c1.get())
		res.put(c2.get())
	return res
