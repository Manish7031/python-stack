## priority queue using tuple implementation

q = []

def enqueue(el, priority):
    q.append((priority, el))
    print(f"Enqueued: {el} with priority {priority}")
    print(f"Current Queue: {q}")
    q.sort(reverse=True)  # Higher priority elements first

def dequeue(priority):
    if not q:
        print("Queue is empty.")
    else:
        el = q.pop(priority)
        print(f"Dequeued: {el} with priority {priority}")
        print(f"Current Queue: {q}")

def isFull():
    if not q:
        print("Queue is empty.")
    else:
        print(f"Current Queue: {q}")

if __name__ == "__main__":
    while True:
        print("\nQueue Operations Menu: 1. Add item 2. remove item 3. Display Queue 4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            element = input("Enter element to add to queue: ")
            priority = int(input("Enter priority (higher number means higher priority): "))
            enqueue(element, priority)
        elif choice == '2':
            priority = int(input("Enter priority to remove item : "))
            dequeue(priority)
        elif choice == '3':
            isFull()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
           