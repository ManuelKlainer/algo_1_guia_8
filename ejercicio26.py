def es_egible(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9') or c == ' ' or c == '_'

def listar_textos_de_archivos(nombre_archivo:str) -> list[str]:
    res: list[str] = []
    archivo = open(nombre_archivo, 'rb')
    contenido: bytes = archivo.read()
    archivo.close()
    actual: str = ""
    
    for byte in contenido:
        c: str = chr(byte)
        if es_egible(c):
            actual += c
        else:
            if len(actual) >= 5:
                res.append(actual)
            actual = ""
    if len(actual) >= 5:
        res.append(actual)
    return res
