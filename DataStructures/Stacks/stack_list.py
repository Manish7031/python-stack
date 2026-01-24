stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# if not stack:
#     print("Stack is empty")
# else:
#     print("Stack is not empty")
N = 10
count = 20
def push():
    if len(stack) >= N:
        print("\n ***** Stack overflow ***** ")
        print(f"here is stack : {stack}")
    else:
        element = input("Enter element to push into stack: ")
        stack.append(element)
        print(f"Pushed {element} into stack.")
        print(stack)

def pop():
    if not stack:
        print("Stack is empty. Cannot pop.")
    else:
        element = stack.pop()
        print(f"Popped {element} from stack.")
        print(stack)

def peek():
    if not stack:
        print("Stack is empty.")
    else:
        element = stack[-1]
        print(f"Top element is: {element}")

if __name__=="__main__":
    while count>0:
        print("\nStack Operations Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            push()
        elif choice == '2':
            pop()
        elif choice == '3':
            peek()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        count -= 1
