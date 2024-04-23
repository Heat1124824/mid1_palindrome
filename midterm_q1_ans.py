#Reference: LeetCode 234 Palindrome Linked List
class Node: 
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, x):
        self.head = Node(x)

    def append(self, x):
        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = Node(x)

    def printLinkedList(self):
        tmp = self.head
        print("[", end="")
        while tmp != None:
            print(tmp.data, end="")
            tmp = tmp.next
            if tmp != None:
                print(", ", end="")
        print("]")

    # 鏈結串列轉普通串列方法
    def isPalindrome(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next

        left = 0
        right = len(nodes) - 1
        while left < right:
            if nodes[left] != nodes[right]:
                return False
            left += 1
            right -= 1

        return True

    #堆疊法
    def isPalindrome2(self):
        if not self.head:
            return True

        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        stack = []
        current = self.head
        for _ in range(length // 2):
            stack.append(current.data)
            current = current.next

        while current:
            if stack.pop() != current.data:
                return False
            current = current.next

        return True

def main():
    lst = LinkedList()
    lst.insertHead(1)
    lst.append(2)
    lst.append(3)
    lst.append(3)
    lst.append(2)
    lst.append(1)
    print("lst : ", end="")
    lst.printLinkedList()
    print(lst.isPalindrome())
    print(lst.isPalindrome2())

if __name__ == "__main__":
    main()