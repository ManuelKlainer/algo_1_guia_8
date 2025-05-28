# dict[str,dict[str, float|int]]

def agregar_producto(inventario: dict[str,dict[str, int | float]], nombre: str, precio: float, cantidad: int):
	valor: dict[str, int | float] = {}
	valor["precio"] = precio
	valor["cantidad"] = cantidad
	inventario[nombre] = valor

def actualizar_stock(inventario: dict[str,dict[str, int | float]], nombre: str, cantidad: int):
	inventario[nombre]["cantidad"] = cantidad


def actualizar_precio(inventario: dict[str,dict[str, int | float]], nombre: str, precio: float):
	inventario[nombre]["precio"] = precio


def calcular_valor_inventario(inventario: dict[str,dict[str, int | float]]) -> float:
	res: float = 0
	for nombre in inventario:
		valor: dict[str, int | float] = inventario[nombre]
		res = res + valor["precio"]*valor["cantidad"]
	return res

inventario: dict[str,dict[str, int | float]] = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total: float = calcular_valor_inventario(inventario)
print(valor_total)