# Módulo para determinar la cantidad exacta a pedir según los requerimientos
def determinar_pedido(stock_actual, stock_minimo):
    # Lógica solicitada:
    # 1. Si stock actual < Stock minimo: Cantidad = Stock minimo - Stock actual.
    # 2. Si stock Actual >= Stock minimo: Cantidad = 0.
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Crear la matriz
matriz_inventario = []

# Ingreso de datos para 5 artículos
print("--- INGRESO DE DATOS DEL INVENTARIO ---")
for i in range(5):
    print(f"\nIngrese los datos del artículo {i + 1}:")
    codigo = input("Código del artículo: ")
    nombre = input("Nombre: ")
    stock_actual = int(input("Stock Actual: "))
    stock_minimo = int(input("Stock Mínimo Requerido: "))
    
    # Se agrega a la matriz siguiendo la estructura solicitada
    matriz_inventario.append([codigo, nombre, stock_actual, stock_minimo])

# Salida: Imprimir informe formateado
print("\n--- LISTA DE PEDIDOS A REALIZAR ---")

for articulo in matriz_inventario:
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    
    # Se utiliza la función requerida determinar_pedido
    cantidad = determinar_pedido(stock_actual, stock_minimo)
    
    # Salida formateada solicitada: "Artículo[Nombre]"
    print(f"Artículo[{nombre}] | Cantidad a solicitar: {cantidad}")
