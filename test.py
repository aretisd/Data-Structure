import string
import random

class Node:
    def __init__(self, name, num):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None
        self.num = num

class Tree:
    def __init__(self):
        self.root = None

    def length(self):
        return self.size

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print  str(node.name) + ' ' + str(node.num) 
            self.inorder(node.right)
            
    def search(self, name):
        node = self.root
        while node != None:
            if node.name == name:
                return node.num
            if node.name > name:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, name, num):
        t = Node(name, num)
        parent = None
        node = self.root
        while node != None:
            parent = node
            if node.name > t.name:
                node = node.left
            else:
                node = node.right
        t.parent = parent
        if parent == None:
            self.root = t
        elif t.name < parent.name:
            parent.left = t
        else:
            parent.right = t
        return t      

    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.parent != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.parent = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.parent = succ

    def transplant(self, node, newnode):
        if node.parent == None:
            self.root = newnode
        elif node == node.parent.left:
            node.parent.left = newnode
        else:
            node.parent.right = newnode
        if newnode != None:
            newnode.parent = node.parent
            
def randomName(size = 3, chars = string.ascii_lowercase):
    return "".join(random.choice(chars) for _ in range(size))
def randomNum(size = 10, chars = string.digits):
    return "".join(random.choice(chars) for _ in range(size))

contactList = Tree()

def generateList(n):
        
    for i in range (n):
        contactList.insert(randomName(),randomNum())

while True:
    print "---------- WELCOME TO CONTACT LISTS-----------"
    print "1. Add a new contact."
    print "2. Remove a contact."
    print "3. Random a list."
    print "4. Show list."
    print "5. Search for contact."
    print "6. Exit."
    print "----------------------------------------------"


    i = input("Choose your choices: ")
    if i == 1:
        name = raw_input("Insert a name: ")
        num = raw_input("Insert a Tel.: ")
        contactList.insert(name, num)

    elif i == 2:
        name = raw_input("Insert a name: ")
        contactList.delete(name)
    elif i == 3:
        n = input("Enter number of list: ")
        generateList(n)  
    elif i == 4:
        contactList.inorder(contactList.root)
    elif i == 5:
        name = raw_input("Insert a name: ")
        print "Tel.:" + (contactList.search(name))
    elif i == 6:
        break
