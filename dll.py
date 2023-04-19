class node:
    def __init__(self,d):
        self.data=d
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def create(self,val):
        self.n=node(val)
        if(self.head==None):
            self.head=self.n
            self.last=self.n
        else:
            self.last.next=self.n
            self.n.prev=self.last
            self.last=self.n
    def add(self,val):
        self.n=node(val)
        self.n.next=self.head
        self.head.prev=self.n
        self.head=self.n
    def display_Forward(self):
        self.temp=self.head
        while(self.temp!=None):
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
            print()
    def delete(self):
        self.temp=self.head
        self.head=self.head.next
        self.head.prev=None
        del self.temp
    def add_end(self,val):
        self.n=node(val)
        self.last.next=self.n
        self.n.prev=self.last
        self.last=self.n
    def dele_end(self):
        self.temp=self.head
        while(self.temp!=self.last):
            self.prev=self.temp
            self.temp=self.temp.next
        self.last=self.last.prev
        self.last.next=None
        del self.temp
dll=DLL()
print("1. create 2.display 3.delete 4.add 5.add element at the end 6.delete element at the end")
ch=0
while(ch<=6):
    ch=int(input("Enter your choice: "))
    if (ch==1):
        n=int(input("Enter value: "))
        dll.create(n)
    elif(ch==2):
        dll.display_Forward()
    elif(ch==3):
        dll.delete()
    elif(ch==4):
        x=int(input("Enter an element to add: "))
        dll.add(x)
    elif(ch==5):
        x=int(input("Enter an element to add at the end: "))
        dll.add_end(x)
    elif(ch==6):
        dll.dele_end()
    else:
        break
