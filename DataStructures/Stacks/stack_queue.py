## stack implemnt using queue module LifoQueue

import queue
stack_size = 10
stack = queue.LifoQueue(stack_size)

def push_item():  ## put
    if stack.qsize() >= stack_size:
        print("\n ***** Stack overflow ***** ")
        return stack
    else:
        element = input("Enter element to push into stack: ")
        stack.put(element)
        print(f"Pushed {element} into stack.")
        print(list(stack.queue))

def pop_item(): ## get
    if stack.empty():
        print("Stack is empty.")
    else:
        element = stack.get(timeout=1)
        print(f"Popped {element} from stack.")
        print(list(stack.queue))

if __name__=="__main__":
    push_item()