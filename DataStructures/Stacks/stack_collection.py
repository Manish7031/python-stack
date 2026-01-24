## stack implemnt using collection module deque

from collections import deque
stack  = deque()
stack_size = 10
def push():
    if len(stack) >= stack_size:
        print("\n ***** Stack overflow ***** ")
        return stack
    else:
        element = input("Enter element to push into stack: ")
        stack.append(element)
        print(f"Pushed {element} into stack.")
        print(stack)
def pop():
    if not stack:
        print("Stack is empty.")
    else:
        element = stack.pop()
        print(f"Popped {element} from stack.")
        print(stack)