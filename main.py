# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from test_linkedList import test_insert
from test_linkedList import test_delete
from test_linkedList import test_getIndex
from linkedList import LinkedList
from combinar import combinar

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
if __name__ == '__main__':
    print_hi('PyCharm')
    test_insert()
    test_getIndex()
    test_delete()

    # Ejemplo 1
    lista1 = LinkedList()
    lista1.insert(1)
    lista1.insert(3)
    lista1.insert(5)

    lista2 = LinkedList()
    lista2.insert(2)
    lista2.insert(4)
    lista2.insert(6)

    lista_combinada = combinar(lista1, lista2)
    print("Ejemplo 1:")
    print("Lista 1:")
    current = lista1.head
    while current is not None:
        print(current.value)
        current = current.next

    print("Lista 2:")
    current = lista2.head
    while current is not None:
        print(current.value)
        current = current.next

    print("Lista combinada:")
    current = lista_combinada.head
    while current is not None:
        print(current.value)
        current = current.next

    # Ejemplo 2
    lista1 = LinkedList()
    lista1.insert(1)
    lista1.insert(2)
    lista1.insert(2)

    lista2 = LinkedList()
    lista2.insert(2)
    lista2.insert(3)
    lista2.insert(4)

    lista_combinada = combinar(lista1, lista2)
    print("Ejemplo 2:")
    print("Lista 1:")
    current = lista1.head
    while current is not None:
        print(current.value)
        current = current.next

    print("Lista 2:")
    current = lista2.head
    while current is not None:
        print(current.value)
        current = current.next

    print("Lista combinada:")
    current = lista_combinada.head
    while current is not None:
        print(current.value)
        current = current.next

    # Ejemplo 3
    lista1 = LinkedList()
    lista1.insert(5)
    lista1.insert(7)
    lista1.insert(9)

    lista2 = LinkedList()
    lista2.insert(1)
    lista2.insert(3)
    lista2.insert(5)

    lista_combinada = combinar(lista1, lista2)
    print("Ejemplo 3:")
    print("Lista 1:")
    current = lista1.head
    while current is not None:
        print(current.value)
        current = current.next

    print("Lista 2:")
    current = lista2.head
    while current is not None:
        print(current.value)
        current = current.next

    print("Lista combinada:")
    current = lista_combinada.head
    while current is not None:
        print(current.value)
        current = current.next
