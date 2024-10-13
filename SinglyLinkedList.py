class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    
class SinglyLinkedlist:
    def __init__(self):
        self.head = None
    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data} >",end=' ')
            temp = temp.next
        print('None')
    def traverse(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    def findinList(self,d):
        temp = self.head
        displaystring = ""
        self.print_list()
        while temp:
            if temp.data == d:
                print(f"{displaystring}^",end='')
            displaystring = displaystring + "    "
            temp = temp.next
    def insertBegin(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def insertMiddle(self,d,ind):
        newnode = Node(d)
        node = self.head
        while node.next:
            if node.data == ind:
                temp = node.next
                node.next = newnode
                node.next.next = temp
            node = node.next
    def insertEnd(self,data):
        temp = self.head
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        while temp.next:
            temp = temp.next
        temp.next = newnode
    def swap(self,ind1,ind2):
        node = self.head
        while node.next:
            '''if node.data == ind1:
                node.data = ind2
            elif node.data == ind2:
                node.data = ind1'''
            
            if node.data == ind1:
                temp1 = node.next
                self.deleteNode()
            elif node.data == ind2:
                temp2 = node.next
            node = node.next
        pass
    def sortList(self,rev=False):
        t = self.head
        while t:
            u = t.next
            while u:
                if not rev:
                    if t.data > u.data:
                        temp = t.data
                        t.data = u.data
                        u.data = temp
                elif rev:
                    if t.data < u.data:
                        temp = t.data
                        t.data = u.data
                        u.data = temp
                u = u.next
            t = t.next
    def deleteNode(self,d='None',ind='None'):

        if d != 'None' and ind != 'None':
            print('Invalid command')
            return
        elif d != 'None':
            t = self.head
            while t.next.next:
                if t.next.data == d:
                    t.next = t.next.next
                    return
                t = t.next
        elif ind != 'None':
            t = self.head
            traverse = 0
            while t.next:
                if traverse+1 == ind:
                    t.next = t.next.next
                    return
                traverse += 1
                t = t.next
    def countduplicates(self,e):
        count = -1
        temp = self.head
        while temp:
            if temp.data == e:
                count += 1
            temp = temp.next
        if count == -1:
            return f"{e} not found on the LinkeList"
        else:
            return count     
    def deleteDuplecates(self):
        temp = self.head
        while temp.next:
            traverse = temp.next
            while traverse:
                if temp.data == traverse.data:
                    self.deleteNode(temp.data)
                traverse = traverse.next
            temp = temp.next
    def reverseList(self):
        l = []
        node = self.head
        while node:
            l.append(node.data)
            node = node.next
        rev = l[::-1]
        node = self.head
        index = 0
        while node:
            node.data = rev[index]
            index += 1
            node = node.next
    def removeFriends(self):
        temp = self.head
        nlist = SinglyLinkedlist()
        while temp:
            nlist.insertEnd(temp.data)
            temp = temp.next
        nlist.sortList()
        self.deleteNode(d=nlist.head.data)
        self.deleteNode(d=nlist.head.next.data)
        temp = None


def SLL():    
    SLList = SinglyLinkedlist()

    '''llist = SinglyLinkedlist()
    llist.head = Node(30)
    llist.head.next = Node(4)
    llist.insertEnd(20)
    llist.insertMiddle(6,30)
    llist.insertBegin(12)
    #llist.sortList()
    llist.deleteNode()
    llist.print_list()'''

    SLList.insertEnd(11)
    SLList.insertEnd(16)
    SLList.insertEnd(2)
    SLList.insertEnd(4)
    SLList.insertEnd(15)
    SLList.insertEnd(18)
    SLList.insertEnd(2)
    SLList.insertBegin(15)
    SLList.insertEnd(18)
    SLList.insertEnd(17)
    SLList.insertEnd(14)
    SLList.insertEnd(2)
    SLList.insertMiddle(7,15)
    SLList.insertEnd(5)
    SLList.insertEnd(4)


    #createSLNode()
    #SLList.sortList()
    #print(SLList.countduplicates(100))
    #SLList.deleteDuplecates()
    #SLList.print_list()
    #SLList.reverseList()
    #SLList.sortList()
    SLList.print_list()
    SLList.removeFriends()
    SLList.print_list()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    return False
if __name__ == '__main__':
    main()