from linkedList import LinkedList
from combinar import combinar
def test_insert():
    objLinkedlist = LinkedList()
    objLinkedlist.insert(5)
    assert objLinkedlist.head.value == 5
    assert objLinkedlist.head.next is None

    objLinkedlist.insert(10)
    objLinkedlist.insert(20)
    assert objLinkedlist.head.next.value == 10
    assert objLinkedlist.head.next.next is not None

    assert objLinkedlist.head.next.next.value == 20
    assert objLinkedlist.head.next.next.next is None


def test_getIndex():
    objLinkedlist = LinkedList()
    objLinkedlist.insert(5)
    objLinkedlist.insert(10)
    objLinkedlist.insert(20)
    objLinkedlist.insert(30)

    assert objLinkedlist.getIndex(0) == 5
    assert objLinkedlist.getIndex(1) == 10
    assert objLinkedlist.getIndex(2) == 20
    assert objLinkedlist.getIndex(3) == 30

    try:
        objLinkedlist.getIndex(4)
    except IndexError:
        assert True
    except Exception:
        assert False


def test_delete():
    objLinkedlist = LinkedList()
    objLinkedlist.insert(5)
    objLinkedlist.insert(10)
    objLinkedlist.insert(20)
    objLinkedlist.insert(30)

    objLinkedlist.delete(5)
    assert objLinkedlist.getIndex(0) == 10

    objLinkedlist.delete(20)
    assert objLinkedlist.getIndex(0) == 10
    assert objLinkedlist.getIndex(1) == 30

    try:
        objLinkedlist.delete(40)
    except ValueError:
        assert True
    except Exception:
        assert False


def test_combinar():
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
    assert lista_combinada.getIndex(0) == 1
    assert lista_combinada.getIndex(1) == 2
    assert lista_combinada.getIndex(2) == 3
    assert lista_combinada.getIndex(3) == 4
    assert lista_combinada.getIndex(4) == 5
    assert lista_combinada.getIndex(5) == 6

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
    assert lista_combinada.getIndex(0) == 1
    assert lista_combinada.getIndex(1) == 2
    assert lista_combinada.getIndex(2) == 2
    assert lista_combinada.getIndex(3) == 2
    assert lista_combinada.getIndex(4) == 3
    assert lista_combinada.getIndex(5) == 4

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
    assert lista_combinada.getIndex(0) == 1
    assert lista_combinada.getIndex(1) == 3
    assert lista_combinada.getIndex(2) == 5
    assert lista_combinada.getIndex(3) == 5
    assert lista_combinada.getIndex(4) == 7
    assert lista_combinada.getIndex(5) == 9
