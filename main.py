class Stack:
    def __init__(self):
        self.data = list()

    def is_empty(self):
        return False if self.data else True
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        self.data.pop()

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return 'Пустой стэк'
        
    def size(self):
        return len(self.data)
    
    
def sequnce_check(stack, string):
    brackets = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for i in string:
        if i in '{([':
            stack.push(i)
        elif i in '})]':
            if stack.peek() == brackets[i]:
                stack.pop()
            else:
                return 'Строка не сбалансирована'
            
    return 'Строка сбалансирована'

def main():
    stack = Stack()
    string = input('Введите строку со скобками для проверки на сбалансированность: ')

    print(sequnce_check(stack, string))

if __name__ == '__main__':
    main()