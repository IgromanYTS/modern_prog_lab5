class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_words(word_list):
    if len(word_list) == 0:
        return

    
    def is_odd_length(word):
        return len(word) % 2 != 0

    
    head = Node(None)  
    current = head
    for word in word_list:
        if is_odd_length(word):
            word_trimmed = word[1:-1] + ","
            current.next = Node(word_trimmed)
            current.next.prev = current
            current = current.next

    
    current = head.next  
    while current is not None:
        print(current.data)
        current = current.next

words = ["apple", "banana", "orange"]
print_words(words)
