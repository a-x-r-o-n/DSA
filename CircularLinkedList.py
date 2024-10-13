class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularlylinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        temp = self.head
        while True:
            print(temp.data,end=' > ')
            temp = temp.next
            if temp.data == 'H':
                print('(H)')
                break
    def insertAtBeginning(self,e):
        temp = self.head
        newnode = Node(e)
        if self.head.next is None:
            newnode.next = self.head
            temp.next = newnode
        else:            
            newnode.next = temp.next
            temp.next = newnode 
    def insertAtEnd(self,e):
        temp = self.head
        newnode = Node(e)        
        if temp.next is None:
            newnode.next = temp
            temp.next = newnode
        else:
            while temp.next.data != 'H':
                temp = temp.next
            newnode.next = temp.next
            temp.next = newnode
    def insertAtMiddle(self,e,i):
        temp = self.head
        while temp.next.data != 'H':
            newnode = Node(e)
            if temp.data == i:
                newnode.next = temp.next
                temp.next = newnode
            temp = temp.next
    def deleteNode(self,e):
        temp =self.head
        while temp.next.next.data != 'H':
            '''if temp.next.data == 'H':
                temp.next = self.head'''
            if temp.next.data == e:
                temp.next = temp.next.next
                break
            temp = temp.next
            if temp.next.next.data == 'H' and temp.next.data == e:
                temp.next = temp.next.next
    def deleteList(self):
        self.head.next = self.head
    def countDuplicates(self):
        count = 0
        isvisited = []
        temp = self.head
        while temp.next.data != 'H':
            u = temp.next
            while u.next.data != 'H':

                if temp.data == u.data:
                    count += 1
                    isvisited.append(temp.data)
                u = u.next
                if u.next.data == 'H' and temp.data == u.data:
                    count += 1
            temp = temp.next
        return count
    def deleteDuplicates(self):
        temp = self.head
        while temp.next.data != 'H':
            u = temp.next
            while u.next.data != 'H':

                if temp.data == u.data:
                    self.deleteNode(u.data)
                u = u.next
                if u.next.data == 'H' and temp.data == u.data:
                    self.deleteNode(u.data)
            temp = temp.next
    def sortList(self):
        temp = self.head
        while temp.next.data != 'H':
            u = temp.next
            if temp.data == 'H':
                pass
            else:
                while u.data != 'H':
                    if temp.data > u.data:
                        t = temp.data
                        temp.data = u.data
                        u.data = t
                    u = u.next
            temp = temp.next
    def reverseList(self):
        l = self.head
        lst = []
        rev = CircularlylinkedList()
        rev.head = Node('H')
        while True:
            lst.append(l.data)
            l = l.next
            if l.data == 'H':
                lst.remove('H')
                lst = lst[::-1]
                break
        for i in range(len(lst)):
            rev.insertAtEnd(lst[i])
        self.head = rev.head
def main():
    cll = CircularlylinkedList()
    cll.head = Node('H')
    cll.insertAtBeginning(2)
    cll.insertAtEnd(3)
    cll.insertAtEnd(7)
    cll.insertAtEnd(5)
    cll.insertAtEnd(3)
    cll.insertAtMiddle(7,'H')
    #cll.print_list()
    #print(cll.countDuplicates())
    cll.deleteDuplicates()
    #cll.print_list()
    cll.sortList()
    cll.print_list()
    cll.reverseList()
    cll.print_list()
if __name__ == '__main__':
    main()