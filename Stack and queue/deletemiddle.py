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

def deletemiddle(st,n,first):

    if (st.is_empty() or first==n):
        return

    x=st.peek()
    st.pop()
    deletemiddle(st,n,first+1)
    if(first!=int(n/2)):
        st.push(x)

st=Stack()
st.push(2)
st.push(7)
st.push(8)
st.push(9)
st.push(3)
st.push(4)
st.push(6)

deletemiddle(st,len(st),0)
print(st.get_stack())