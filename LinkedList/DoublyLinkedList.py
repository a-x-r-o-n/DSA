class DNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end=' <-> ')
            temp = temp.next
        print(None)
    def insertAtBeginning(self,e):
        newnode = DNode(e)
        if self.head.next is None:
            newnode.prev = self.head
            self.head.next = newnode
        else:
            newnode.next = self.head.next
            newnode.prev = self.head
            self.head.next = newnode
            newnode.next.prev = newnode
    
    def insertAtEnd(self,e):

        newnode = DNode(e)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp

    def insertAtMiddle(self,e,d):

        newnode = DNode(e)

        temp = self.head

        while temp:
            if temp.data == d:
                newnode.next = temp.next
                newnode.prev = temp
                temp.next = newnode
                newnode.next.prev = newnode
            
            temp = temp.next

    def swap(self,a,b):
        node = DNode(None)
        isAFound = False
        isBFound = False
        temp = self.head
        while temp != None:
            if temp.data == a:
                print("a found")
                apoint = temp
                isAFound = True
            elif temp.data == b:
                bpoint = temp
                print(f"b found: {bpoint.data}")
                isBFound = True
            elif isBFound and isAFound:
                
                node.next = bpoint.next
                bpoint.next = apoint.next
                apoint.next = node.next
                node.prev = bpoint.prev
                bpoint.prev = apoint.prev
                apoint.prev = node.prev

                if apoint.prev != None:
                    apoint.prev.next = apoint
                if bpoint.prev != None:
                    bpoint.prev.next = bpoint
                if bpoint.next != None:
                    bpoint.next.prev = bpoint
                if apoint.next != None:
                    apoint.next.prev = apoint
                
                print("checked")
                isAFound = False
                isBFound = False
            temp = temp.next
            


def main():

    dll = DoublyLinkedList()
    dll.head = DNode(5)
    #dll.print_list()
    dll.insertAtBeginning(7)
    dll.insertAtBeginning(3)
    dll.insertAtBeginning(2)
    dll.insertAtEnd(1)
    dll.insertAtEnd(4)
    dll.insertAtMiddle(6,2)
    dll.print_list()
    dll.swap(6,3)
    dll.print_list()

if __name__ == '__main__':
    main()