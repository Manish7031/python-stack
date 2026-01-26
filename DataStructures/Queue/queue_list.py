# queue implemt using list
queue = []

def enqueue(element):
    queue.append(element)
    print(f"Enqueued: {element}")
    print(f"current Queue: {queue}")

def dequeue():
    if not queue:
        print("Queue is empty..")
    else:
        el = queue.pop(0)
        print(f"Dequeued: {el}")
        print(f"current Queue: {queue}")


def isFull():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print(f"current Queue: {queue}")


if __name__ == "__main__":
    while True:
        print("\nQueue Operations Menu: 1. Add item 2. remove item 3. Display Queue 4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            enqueue(input("Enter element to add to queue: "))
        elif choice == '2':
            dequeue()
        elif choice == '3':
            isFull()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        

        

# queue.insert(0, 4)
# queue.insert(0, 5)
# print("Initial queue:", queue)

# # Dequeue elements
# dequeued_element = queue.pop(0)
# print("Dequeued element:", dequeued_element)
# dequeued_element = queue.pop(1)
# print("Dequeued element:", dequeued_element)
# dequeued_element = queue.pop(2)
# print("Dequeued element:", dequeued_element)