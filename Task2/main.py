from Task1.main import Stack


def check_balance(hook_list: str) -> str:

    hl = Stack()

    for elem in hook_list:
        if elem in '({[':
            hl.push(elem)
            continue
        if elem == ')' and hl.peek() == '(' or elem == ']' and hl.peek() == '[' or elem == '}' and hl.peek() == '{':
            hl.pop()
        else:
            return 'Не сбалансировано'

    if hl.isEmpty():
        return 'Сбалансированно'
    else:
        return "Не сбалансированно"


if __name__ == '__main__':
    print(check_balance('(((([{}]))))'))
    print(check_balance('[([])((([[[]]])))]{()}'))
    print(check_balance('{{[()]}}'))
    print(check_balance('}{}'))
    print(check_balance('{{[(])]}}'))
    print(check_balance('[[{())}]'))
