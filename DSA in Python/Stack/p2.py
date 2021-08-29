stack = []

def push():
    if len(stack)==n:
        print("list is full")
    else:
      element = input("Enter the element:")
      stack.append(element)
      print(stack)

def show():
    print("elements in the stack:")
    print(stack)

def popElement():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("removed element:",e)
        print(stack)

n = int(input("Enter the limit of the stack:"))

while True:
    print("select the operation 1.push 2.pop 3.Elements 4.quit")
    choice = int(input("Enter the choice:"))
    if choice==1:
        push()
    elif choice==2:
        popElement()
    elif choice==3:
        show()
    elif choice==4:
        break
    else:
        print("Enter the correct operation")