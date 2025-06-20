class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    def reverse(self): # реверс
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def insertion_sort(self): #метод вставки
        sorted_head = None
        curr = self.head

        while curr:
            next_node = curr.next
            if not sorted_head or curr.value < sorted_head.value:
                curr.next = sorted_head
                sorted_head = curr
            else:
                search = sorted_head
                while search.next and search.next.value < curr.value:
                    search = search.next
                curr.next = search.next
                search.next = curr
            curr = next_node

        self.head = sorted_head

    @staticmethod
    def merge_sorted(list1, list2): # об'єднання
        dummy = Node(0)
        tail = dummy
        a, b = list1.head, list2.head

        while a and b:
            if a.value < b.value:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a or b

        merged_list = SinglyLinkedList()
        merged_list.head = dummy.next
        return merged_list

lst = SinglyLinkedList()
for v in [7, 3, 5, 2, 9]:
    lst.append(v)

print("Оригінальний список:", lst.to_list())

lst.reverse()
print("Після реверсу:", lst.to_list())

lst.insertion_sort()
print("Після сортування:", lst.to_list())

lst1 = SinglyLinkedList()
lst2 = SinglyLinkedList()
for v in [1, 4, 6]:
    lst1.append(v)
for v in [2, 3, 5]:
    lst2.append(v)

merged = SinglyLinkedList.merge_sorted(lst1, lst2)
print("Об'єднаний відсортований список:", merged.to_list())