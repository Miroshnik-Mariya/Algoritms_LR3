print("Лабораторная работа №3\nВариант 1\nВыполнила Мирошник Мария 6201-020302D\n") 
print("1. Дан однонаправленный список с петлёй. Его «последний» элемент содержит указатель на один из элементов этого же списка, причём не обязательно на первый. Найдите начальный узел петли. Элементы списка менять нельзя, память должна быть константна;")
print("\n2. Дан список с двумя указателями у каждого элемента. Зацикленность списка не допускается. Скопируйте данный список за время О(n) без использования дополнительной памяти. Выделение памяти под все данные одним блоком (как под массив) не допускается, список должен быть разбросанным по частям;")
print("\n3. Удалите дубликаты из несортированного связного списка. Память должна быть константна.")

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
 

class TwoNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


'''
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:  
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return self  

    def __str__(self):  
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes)
    '''


def exersice1(head):
    turtle = head
    hare = head

    while hare is not None and hare.next is not None:
        turtle = turtle.next
        hare = hare.next.next
        if turtle == hare:
            break  # Петля обнаружена

    
    if hare is None or hare.next is None:
        return None

    turtle = head
    while turtle != hare:
        turtle = turtle.next
        hare = hare.next
        
    return turtle  # turtle и hare теперь указывают на начало петли


def exersice2(head):
    if not head:
        return None

    new_head = TwoNode(head.data)
    new_current = new_head  # Текущий узел в новом списке
    original_current = head.next  # Начинаем со второго узла оригинала

    # Копируем остальные узлы
    while original_current:
        new_node = TwoNode(original_current.data)
        new_node.prev = new_current
        new_current.next = new_node
        new_current = new_node
        original_current = original_current.next
    return new_head


def print_doubly_linked_list(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
  

def exercise3(head):
    if not head:
        return None

    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next  # Пропускаем дубликат
            else:
                runner = runner.next  # Переход к следующему элементу
        current = current.next  # Переход к следующему уникальному элементу

    return head  

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  

loop_start = exersice1(head)
if loop_start != None:
    print(f"\n\n№1\nНачало петли: {loop_start.data}") 
else:
    print("Петля не найдена")


node6 = Node(6)
node5.next = node6  
loop_start = exersice1(head)
print(" ")
print_doubly_linked_list(head) 
if loop_start != None:
    print(f"\n\n№1\nНачало петли: {loop_start.data}") 
else:
    print("Петля не найдена")
    

head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.next = node3
node2.prev = head
node3.prev = node2


print("\n\n\n№2\Оригинальный список:")
print_doubly_linked_list(head) 

new_head = exersice2(head)

print("\n\nСкопированный список:")
print_doubly_linked_list(new_head) 



head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(3)
node5 = Node(1)
node6 = Node(6)
node7 = Node(6)
node8 = Node(6)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6 
node6.next = node7 
node7.next = node8 

print("\n\n\n№3\nИсходный список:")
print_doubly_linked_list(head) 
head = exercise3(head)
print("\n\nСписок без дупликатов:")
print_doubly_linked_list(head) 
print("\n\n\n")