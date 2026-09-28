def calcular_descuento(tipo_cliente, monto):
    if tipo_cliente == "vip":
        if monto > 100000:
            descuento = 0.20
        elif monto > 50000:
            descuento = 0.15
        elif monto > 20000:
            descuento = 0.10
        else:
            descuento = 0.05
    elif tipo_cliente == "frecuente":
        if monto > 100000:
            descuento = 0.15
        elif monto > 50000:
            descuento = 0.10
        elif monto > 20000:
            descuento = 0.05
        else:
            descuento = 0
    elif tipo_cliente == "nuevo":
        if monto > 100000:
            descuento = 0.10
        elif monto > 50000:
            descuento = 0.05
        else:
            descuento = 0
    else:
        descuento = 0

    return monto * descuento


def procesar_venta(cliente, productos):
    total = 0

    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]

        subtotal = precio * cantidad
        total += subtotal

        print("Producto:", nombre)
        print("Precio:", precio)
        print("Cantidad:", cantidad)
        print("Subtotal:", subtotal)

    if cliente["tipo"] == "vip":
        if total > 100000:
            descuento = total * 0.20
        elif total > 50000:
            descuento = total * 0.15
        elif total > 20000:
            descuento = total * 0.10
        else:
            descuento = total * 0.05
    elif cliente["tipo"] == "frecuente":
        if total > 100000:
            descuento = total * 0.15
        elif total > 50000:
            descuento = total * 0.10
        elif total > 20000:
            descuento = total * 0.05
        else:
            descuento = 0
    else:
        descuento = 0

    total_final = total - descuento

    print("Cliente:", cliente["nombre"])
    print("Total:", total)
    print("Descuento:", descuento)
    print("Total final:", total_final)

    return total_final


def validar_producto(producto):
    if producto["precio"] < 0:
        return False

    if producto["cantidad"] < 0:
        return False

    if producto["nombre"] == "":
        return False

    if producto["precio"] == 0:
        return False

    return producto["cantidad"] != 0


def calcular_total_productos(productos):
    total = 0

    for producto in productos:
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        subtotal = precio * cantidad
        total += subtotal

    return total


def calcular_subtotal_productos(productos):
    total = 0

    for producto in productos:
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        subtotal = precio * cantidad
        total += subtotal

    return total
