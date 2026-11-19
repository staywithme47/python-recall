class Stack:
    def __init__(self):
        self._items = []


    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            return None
        else:
            return self._items.pop()

    def peek(self):
        if not self._items:
            return None
        else:
            return self._items[-1]

    def is_empty(self):
        return not self._items

    def size(self):
        return len(self._items)


class Queue:
    def __init__(self):
        self._items = []


    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            return None
        else:
            return self._items.pop(0)

    def peek(self):
        if not self._items:
            return None
        else:
            return self._items[0]

    def is_empty(self):
        return not self._items

    def size(self):
        return len(self._items)



def is_valid_brackets(s:str) -> bool:
    stack = Stack()
    pairs = {")" : "(", "]" : "[", "}" : "{" }
    top = None
    for sym in s:
        if sym in "([{":
            stack.push(sym)

        elif sym in ")]}":
            top = stack.pop()

            if top is None or top != pairs[sym]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    print("--- ТЕСТ СТЕКА ---")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("Размер:", s.size())
    print("Верхний:", s.peek())
    print("Извлекли:", s.pop())
    print("Размер:", s.size())

    print("\n--- ТЕСТ ОЧЕРЕДИ ---")
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print("Размер:", q.size())
    print("Первый:", q.peek())
    print("Извлекли:", q.dequeue())
    print("Извлекли:", q.dequeue())
    print("Размер:", q.size())

    print("\n--- ТЕСТ СКОБОК ---")
    print(is_valid_brackets("()[]{}"))
    print(is_valid_brackets("(]"))
    print(is_valid_brackets("([)]"))
    print(is_valid_brackets("{[]}"))