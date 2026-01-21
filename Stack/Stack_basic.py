# Basic Stack

size = int(input("Enter the size of the Stack: "))
stack = []
top = -1


def isFull():
    return top == size - 1


def isEmpty():
    return top == -1


def push(val):
    global top
    if isFull():
        print("Stack Overflow!")
    else:
        stack.append(val)
        top += 1
        print(val, "pushed into stack")


def pop():
    global top
    if isEmpty():
        print("Stack Underflow!")
        return None
    else:
        val = stack.pop()
        top -= 1
        return val


def peek():
    if isEmpty():
        print("Stack is Empty!")
        return None
    else:
        return stack[top]


while True:
    opt = input("""
Enter Operation:
1. Push
2. Pop
3. Peek
4. Exit
Choice: """)

    if opt == "1":
        val = int(input("Enter the value: "))
        push(val)

    elif opt == "2":
        val = pop()
        if val is not None:
            print("Popped:", val)

    elif opt == "3":
        val = peek()
        if val is not None:
            print("Top element:", val)

    elif opt == "4":
        print("Bye!")
        break

    else:
        print("Invalid choice")
