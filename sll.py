class node:
    def __init__ (self,d):
        self.data=d
        self.next=None
class LinkedList:
    def __init__ (self):
        self.head=None
    def create(self,val):
        self.n=node(val)
        if(self.head==None):
            self.head=self.n
            self.last=self.n
        else:
            self.last.next=self.n
            self.last=self.n
    def display(self):
        self.temp=self.head
        while(self.temp!=None):
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
        print()
    def dele_beg(self):
        self.temp=self.head
        self.head=self.head.next
        del self.temp
    def add_beg(self,val):
        self.n=node(val)
        self.n.next=self.head
        self.head=self.n
    def dele_end(self):
        self.temp=self.head
        while(self.temp!=self.last):
            self.prev=self.temp
            self.temp=self.temp.next
        self.last=self.prev
        self.last.next=None
        del self.temp
    def add_end(self,val):
        self.n=node(val)
        self.last.next=self.n
        self.last=self.n
Ll=LinkedList()
print("1 create")
print("2 display")
print("3 delete beginning")
print("4 add beginning")
print("5 delete element at the end")
print("6 add element at the end")
ch=0
while(ch<=6):
    ch=int(input("Enter your choice: "))
    if (ch==1):
        n=int(input("Enter value: "))
        Ll.create(n)
    elif(ch==2):
        Ll.display()
    elif(ch==3):
        Ll.dele_beg()
    elif(ch==4):
        x=int(input("Enter an element to add: "))
        Ll.add_beg(x)
    elif(ch==5):
        Ll.dele_end()
    elif(ch==6):
        x=int(input("Enter an element to add at the end: "))
        Ll.add_end(x)
    else:
        break
