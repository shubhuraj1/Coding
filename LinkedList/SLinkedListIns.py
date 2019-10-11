class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end="-")
            curr_node = curr_node.next
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insertafternode(self, prev_node, data):

        if not prev_node:
            print("Prev node is empty")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        while(cur_node is not None):
            if cur_node.data == key:
                break
            prev = cur_node
            cur_node = cur_node.next

        if(cur_node==None):
            return

        prev.next = cur_node.next
        cur_node=None
    def delete_list(self):
        curr = self.head
        while curr:
            prev=curr.next
            del curr.data
            curr = prev
        print("Linked List Deleted.")
    def getcount(self):
        return self.getcountrec(self.head)
    def getcountrec(self, curr):
        if not curr:
            return 0
        else:
            return 1 + self.getcountrec(curr.next)
    def size(self):
        count=0
        curr=self.head
        while curr:
            curr=curr.next
            count+=1
        return count
    def searchelement(self, key):
        curr=self.head
        while curr:
            if curr.data == key:
                return True
            curr=curr.next
        return False
    def getNthNode(self, index):
        curr=self.head
        count = 0
        while curr:
            if count == index:
                return curr.data
            count+=1
            curr=curr.next

        assert(False)
        return 0
    def removeDups(self):
        curr = curr2 = self.head
        while curr is not None:
            while curr2.next is not None:
                if curr2.next.data == curr.data:
                    curr2.next = curr2.next.next
                else:
                    curr2 = curr2.next
            curr = curr2 = curr.next
    def detectloop(self):
        curr=self.head
        temp=""
        while curr:
            if curr.next==None:
                return False
            if  curr.next==temp:
                return True
            nex=curr.next
            curr.next=temp
            curr=nex
        return False


llist = LinkedList()
llist.append(3)
llist.append(4)
llist.append(7)
llist.append(5)
llist.append(3)
llist.append(5)
llist.append(9)
llist.append(9)
llist.print_list()
llist.removeDups()
llist.print_list()
