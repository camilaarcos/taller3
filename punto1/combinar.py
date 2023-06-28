from linkedList import LinkedList

def combinar(lista1, lista2):
    lista_combinada = LinkedList()

    # Punteros para recorrer las listas
    p1 = lista1.head
    p2 = lista2.head

    while p1 is not None and p2 is not None:
        if p1.value <= p2.value:
            lista_combinada.insert(p1.value)
            p1 = p1.next
        else:
            lista_combinada.insert(p2.value)
            p2 = p2.next

    # Agregar los elementos restantes de la lista1
    while p1 is not None:
        lista_combinada.insert(p1.value)
        p1 = p1.next

    # Agregar los elementos restantes de la lista2
    while p2 is not None:
        lista_combinada.insert(p2.value)
        p2 = p2.next

    return lista_combinada



