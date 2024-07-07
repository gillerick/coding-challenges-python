### Problems

1. [Time Delta](https://www.hackerrank.com/challenges/python-time-delta) [Medium]
2. [Word Order](https://www.hackerrank.com/challenges/word-order) [Medium]
3. [Runner Up Score](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list) [Easy]
4. [Words Score](https://www.hackerrank.com/challenges/words-score) [Medium]
5. [Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles) [Easy]
6. [Mini Max Sum](https://www.hackerrank.com/challenges/mini-max-sum) [Easy]
7. [Time Conversion](https://www.hackerrank.com/challenges/time-conversion) [Easy]
8. [Fraudulent Activity Notifications](https://www.hackerrank.com/challenges/fraudulent-activity-notifications) [Medium]
9. [Text Wrap](https://www.hackerrank.com/challenges/text-wrap) [Easy]
10. [Merge the Tools](https://www.hackerrank.com/challenges/merge-the-tools) [Medium]
11. [Capitalize](https://www.hackerrank.com/challenges/capitalize) [Easy]
12. [Minimum Bribes](https://www.hackerrank.com/challenges/new-year-chaos) [Medium]
13. [Minimum Swaps 2](https://www.hackerrank.com/challenges/minimum-swaps-2) [Medium]
14. [Compare the Triplets](https://www.hackerrank.com/challenges/compare-the-triplets/) [Easy]
15. [An Interesting Game](https://www.hackerrank.com/challenges/an-interesting-game-1) [Medium]
16. [Two Sub-arrays](https://www.hackerrank.com/challenges/two-subarrays/) [Expert]
17. [Sherlock and Anagrams](https://www.hackerrank.com/challenges/sherlock-and-anagrams) [Medium]
18. [Hackerland Radio Transmitters](https://www.hackerrank.com/challenges/hackerland-radio-transmitters) [Medium]
19. [Minimum Loss](https://www.hackerrank.com/challenges/minimum-loss/) [Medium]
20. [Missing Numbers](https://www.hackerrank.com/challenges/missing-numbers) [Easy]
21. [Pairs](https://www.hackerrank.com/challenges/pairs/) [Medium]
22. [Sherlock and Arrays](https://www.hackerrank.com/challenges/sherlock-and-array) [Easy]
23. [Maximum Sub-array Sum](https://www.hackerrank.com/challenges/maximum-subarray-sum) [Hard]
24. [Compress the String](https://www.hackerrank.com/challenges/compress-the-string/) [Medium]
25. [Playing with Numbers](https://www.hackerrank.com/challenges/playing-with-numbers) [Hard]
26. [Index of first occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) [Medium]
27. [Move Zeros](https://leetcode.com/problems/move-zeroes/) [Easy]

#### DSA Designs

#### 1. Array-Based Stack Implementation (Data Structures & Algorithms in Python, page 234)

- The implementations for _top_, _is_empty_, and _len_ use constant time in the worst case. The O(1) time for push and
  pop are **amortized** bounds a typical call to either of these methods uses constant time, but there is occasionally
  an O(n)-time worst case, where n is the current number of elements in the stack, when an operation causes the list to
  resize its internal array.

#### 2. Reversing Data Using a Stack (Data Structures & Algorithms in Python, page 235)

- One technical detail worth noting is that we intentionally strip trailing newlines from lines as they are read, and
  then re-insert newlines after each line when writing the resulting file. The reason for doing this is to handle a
  special case in which the original file does not have a trailing newline for the final line.
- If we exactly echoed the lines read from the file in reverse order, then the original last line would be followed
  (without newline) by the original second-to-last line. In our implementation, we ensure that there will be a
  separating newline in the result.

#### 3. Array-Based Queue Implementation (Data Structures & Algorithms in Python, page 241 - 246)

| Operation    | Running Time |
|--------------|:------------:
| Q.enqueue(e) |    O(1)*     |
| Q.dequeue()  |    O(1)*     |
| Q.first()    |     O(1)     |     
| Q.is_empty() |     O(1)     |
| len(Q)       |     O(1)     | 

*amortized

#### 4. Validating a Binary Sort Tree(BST)

- Even though there is no memory used the space complexity of this operation is O(d) where d is the depth of the tree
- The time complexity is O(n) where n is the number of nodes in the tree. This is because we are traversing through each
  of the tree's nodes
- For a valid BST, a node's value has to be greater than or equal to the minimum value and less than the maximum value.

  ```python
  if tree.data < minValue or tree.data >= maxValue:
    return False
  ```

#### 5. Linked Lists

- A linked list is a data structure that represents a sequence of **nodes**. In a _singly linked list_, each node points
  to the next node in the linked list. In a _doubly linked list_, each node points to both the next node and the
  previous node in the linked list.
- In a linked list, the least significant digit always comes first. So that 2 -> 4 -> 7 -> 1 represents the
  number `1742`

##### 5.1. Creating a linked list

```java
class Node {
  Node next = null;
  int data;

  public Node(int d) {
    data = d;
  }

  void appendToTail(int d) {
    Node end = new Node(d);
    Node n = this;
    while (n.next != null) {
      n = n.next;
    }
    n.next = end;
  }
}
```

##### 5.2. Deleting a node from a singly linked list

- Given a node n, we first find the previous node `prev` and set `prev.next` equal to `n.next`. If the list is doubly
  linked, we must also update `n.next` to set `n.next.prev` to `n.prev`.
- The important thing to remember is (1) To check for the null pointer and (2) To update the head or tail pointer as
  necessary
- If this is implemented in a language that requires the developer to do memory management, deallocating the removed
  node should be considered.

```java
Node deleteNode(Node head, int d) {

    Node n = head;

    if (n.data == d) {
      return head.next; /*moved head*/
    }

    while (n.next != null) {
      if (n.next.data == d) {
        n.next = n.next.next;
        return head; /*head did not change*/
      }
      n = n.next;
    }
    return head;
  }
```

#### 5. The Queue Data Structure

- A queue is a data structure in which all the additions are made at one end (head or front of queue) and all deletions
  are made at one end (rear or tail of the queue)
- It is a FIFO data structure

#### 5.1. Applications

- CPU scheduling
- Data is transferred asynchronously between two processes
- Graph traversal algorithms
- Transport and operations management
- File servers
- IO buffers
- Printer queues
- Phone calls to customer service hotlines
- Resource is shared among multiple consumers

#### 5.2. Operations

- **Enqueue** - to put an item into the queue
- **Dequeue** - to remove an item from the front of the queue
- Lists are not efficient for implementing queues. While **appends** and **pops** from the end of the list are fast, **inserts** or **pops** from the beginning of the list is slow because all the other elements have to be shifted by
  one.

![img.png](img.png)

##### 5.3. Priority Queue

#### 6. Linked Lists




