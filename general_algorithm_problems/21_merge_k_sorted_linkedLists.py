class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += (' '+ str(c.val)) if c.val else "none"
            c = c.next
        return answer

def merge(lists):
    # Fill this in.
    result = None
    head = None
    while(len(lists)):
        i = 0
        while(i < len(lists)):
            if(not lists[i]):
                lists.pop(i)
            else:
                i += 1
        
        if(len(lists) == 0):
            break

        minNode = lists[0]
        minIndex = 0
        for i in range(0,len(lists)):
            currentNode = lists[i]
            if(currentNode.val < minNode.val):
                minNode = currentNode
                minIndex = i

        if(result):
            result.next = minNode 
            result = result.next
        else:
            result = minNode
            head = result

        lists[minIndex] = lists[minIndex].next

    return head

a = Node(1, Node(4, Node(5)))
b = Node(1, Node(3, Node(4)))
c = Node(2, Node(6))
print merge([a, b, c])
# 123456