class SingleLinkedListNode:
    def __init__(self, value: 0, next: None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}"


class SingleLinkList:
    def __init__(self, head: None):
        self.head = head

    def __repr__(self) -> str:
        single_linked_list = []
        if self.head and self.head.next:
            single_linked_list.append(self.head.value)
            next = self.head.next
            while next:
                single_linked_list.append(next.value)
                next = next.next
            return f"{single_linked_list}"
        elif self.head:
            return f"{[self.value]}"
        else:
            return f"{single_linked_list}"

    def _get_length(self):
        return len(self.__repr__())

    def insert(self, value, index):
        new_node = SingleLinkedListNode(value, None)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            target = self.get(index)
            before_target = self.get(index-1)
            before_target.next = new_node
            new_node.next = target

    def delete(self, index: int):
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            target = self.get(index)
            after_target = target.next
            before_target = self.get(index-1)
            before_target.next = after_target

    def get(self, index: int) -> SingleLinkedListNode:
        if index < 0:
            raise IndexError
        if index == 0:
            return self.head
        else:
            node = self.head
            next = self.head.next
            count = 0
            while count < index:
                if next:
                    count += 1
                    node = next
                    next = node.next
            return node


def main(single_list_link):
    # get
    print(single_linked_list.get(0))
    print(single_linked_list.get(3))
    print(single_linked_list.get(9))
    # print(single_linked_list.get(10))
    # insert
    single_linked_list.insert(11, 9)
    print(single_linked_list)
    single_linked_list.insert(-1, 0)
    print(single_linked_list)
    single_linked_list.insert(3.5, 3)
    print(single_linked_list)
    # delete
    single_linked_list.delete(0)
    print(single_linked_list)
    single_linked_list.delete(5)
    print(single_linked_list)
    single_linked_list.delete(10)
    print(single_linked_list)

    # print


if __name__ == "__main__":
    tenth = SingleLinkedListNode(9, None)
    nineth = SingleLinkedListNode(8, tenth)
    eighth = SingleLinkedListNode(7, nineth)
    seventh = SingleLinkedListNode(6, eighth)
    sixth = SingleLinkedListNode(5, seventh)
    fifth = SingleLinkedListNode(4, sixth)
    forth = SingleLinkedListNode(3, fifth)
    third = SingleLinkedListNode(2, forth)
    second = SingleLinkedListNode(1, third)
    head = SingleLinkedListNode(0, second)
    single_linked_list = SingleLinkList(head)

    main(single_linked_list)
