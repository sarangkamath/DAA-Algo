class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data

    def front_value(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the value to enqueue: ")
            queue.enqueue(data)
            print(f"{data} enqueued into the queue.")
        elif choice == '2':
            try:
                dequeued_data = queue.dequeue()
                print(f"Dequeued value: {dequeued_data}")
            except IndexError as e:
                print(f"Error: {e}")
        elif choice == '3':
            try:
                front_value = queue.front_value()
                print(f"Front value: {front_value}")
            except IndexError as e:
                print(f"Error: {e}")
        elif choice == '4':
            print("Queue:")
            queue.display()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
