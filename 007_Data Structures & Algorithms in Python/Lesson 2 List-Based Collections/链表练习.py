class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linklist:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        curNode = self.head
        if self.head:
            while curNode.next:
                curNode = curNode.next
            curNode.next = Element(value)
        else:
            self.head = Element(value)

    def printValue(self):
        if self.head:
            curNode = self.head
            while curNode:
                print(curNode.value)
                curNode = curNode.next


if __name__ == "__main__":
    linkList = Linklist(Element(32))
    linkList.append(32)
    [linkList.append(i) for i in range(5)]
    linkList.printValue()
