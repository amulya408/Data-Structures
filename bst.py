class node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
class BT:
    def __init__(self):
        self.root=None
    def create(self,data):
        self.n=node(data)
        if(self.root==None):
            self.root=self.n
        else:
            self.temp=self.root
            while(self.temp!=None):
                ch=int(input("Enter 1 for left & 2 for right: "))
                if ch==1:
                    if(self.temp.left==None):
                        self.temp.left=self.n
                        return self.root
                    else:
                        self.temp=self.temp.left
                elif ch==2:
                    if(self.temp.right==None):
                        self.temp.right=self.n
                        return self.root
                    else:
                        self.temp=self.temp.right
def inorder(root):
    temp=root
    if(temp!=None):
        inorder(temp.left)
        print(temp.data,end=" ")
        inorder(temp.right)
def preorder(root):
    temp=root
    if(temp!=None):
        print(temp.data,end=" ")
        preorder(temp.left)
        preorder(temp.right)
def postorder(root):
    temp=root
    if(temp!=None):
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data,end=" ")
b=BT()
print("1.Create\n2.Inorder\n3.Preorder\n4.Postorder")
c=0
while(c<=4):
    c=int(input("Enter choice: "))
    if(c==1):
        x=int(input("Enter element: "))
        root=b.create(x)
    elif(c==2):
        inorder(root)
    elif(c==3):
        preorder(root)
    elif(c==4):
        postorder(root)
    else:
        break

