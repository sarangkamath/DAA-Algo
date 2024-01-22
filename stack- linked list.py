class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    stack = Stack()

    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the value to push: ")
            stack.push(data)
            print(f"{data} pushed onto the stack.")
        elif choice == '2':
            try:
                popped_data = stack.pop()
                print(f"Popped value: {popped_data}")
            except IndexError as e:
                print(f"Error: {e}")
        elif choice == '3':
            try:
                peeked_data = stack.peek()
                print(f"Peeked value: {peeked_data}")
            except IndexError as e:
                print(f"Error: {e}")
        elif choice == '4':
            print("Stack:")
            stack.display()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
