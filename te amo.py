# te_amo.py

mensaje = "Te amo " + ("mucho " * 5000)

nombre_archivo = "te_amo.txt"

with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write(mensaje)

print("Archivo creado:", nombre_archivo)

# Intentar abrir automáticamente (funciona en algunos dispositivos)
try:
    import os
    os.system(f'xdg-open "{nombre_archivo}"')
except:
    pass