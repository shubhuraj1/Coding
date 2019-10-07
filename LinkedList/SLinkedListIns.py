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

llist = LinkedList()
llist.append(2)
llist.append(3)
llist.append(5)
llist.append(7)
llist.append(9)
llist.append(6)
llist.print_list()
#llist.delete_node(7)
#llist.print_list()
#llist.delete_list()
#llist.print_
