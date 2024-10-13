# DSA Learning Process

Welcome to my GitHub repository documenting my journey of learning Data Structures and Algorithms (DSA). This repository contains Python implementations of various data structures, including linked lists, stacks, and queues.

## Table of Contents
- [Circular Linked List](#circular-linked-list)
- [Doubly Linked List](#doubly-linked-list)
- [Singly Linked List](#singly-linked-list)
- [Stacks](#stacks)
- [Queues](#queues)

---

### Circular Linked List
- **File:** [CircularLinkedList.py](CircularLinkedList.py)
- **Description:** Implementation of a circular linked list that supports operations such as insertion at the beginning, middle, and end, deletion of nodes, counting duplicates, sorting, and reversing the list.
- **Key Features:**
  - `insertAtBeginning(e)`
  - `insertAtEnd(e)`
  - `insertAtMiddle(e, i)`
  - `deleteNode(e)`
  - `reverseList()`

### Doubly Linked List
- **File:** [DoublyLinkedList.py](DoublyLinkedList.py)
- **Description:** Implementation of a doubly linked list where each node contains links to both the next and previous nodes. The list supports insertion at various points, swapping nodes, and printing the list.
- **Key Features:**
  - `insertAtBeginning(e)`
  - `insertAtEnd(e)`
  - `insertAtMiddle(e, d)`
  - `swap(a, b)`

### Singly Linked List
- **File:** [SinglyLinkedList.py](SinglyLinkedList.py)
- **Description:** Implementation of a singly linked list that supports common operations such as insertion, deletion, finding elements, and sorting the list. Also includes a function to remove duplicates and reverse the list.
- **Key Features:**
  - `insertBegin(data)`
  - `insertMiddle(d, ind)`
  - `insertEnd(data)`
  - `deleteNode(d)`
  - `reverseList()`

### Stacks
- **File:** [stacks.py](stacks.py)
- **Description:** A basic stack implementation supporting push, pop, and peek operations. The stack is visualized with a custom print function.
- **Key Features:**
  - `push(data)`
  - `pop()`
  - `peek()`
  - `print_stack()`

### Queues
- **File:** [Queue.py](Queue.py)
- **Description:** A queue implementation supporting enqueue, dequeue, and peek operations. Includes a function to print the current state of the queue.
- **Key Features:**
  - `enqueue(data)`
  - `dequeue()`
  - `peek()`
  - `print_queue()`

---

## How to Run
To run any of the Python files, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DSA-learning-process.git
   ```
2. Navigate to the directory and execute the desired file:
   ```bash
   python filename.py
   ```
   Replace `filename.py` with the name of the file you want to run, e.g., `CircularLinkedList.py`.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

