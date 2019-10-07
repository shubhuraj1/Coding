class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def __len__(self):
        return len(self.items)

st=Stack()

def digitsinstack(num):
    while(num!=0):
        st.push(num%10)
        num=int(num/10)

def reversenumbr(num):
    digitsinstack(num)

    reverse=0
    i=1

    while(len(st)!=0):        
        reverse=reverse+(st.peek()*i)
        i=i*10
        st.pop()

    return reverse
num=int(input())
print(reversenumbr(num))            




