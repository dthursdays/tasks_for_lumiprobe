def main(string):
    stack = []
    for symbol in string:
        if symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            if not stack or stack.pop() != '(':
                return False
        else:
            return 'В вводе допустимы лишь символы "(" и ")"'

    if stack:
        return False
    return True


if __name__ == '__main__':
    print(main(input("Введите скобочную последовательность:\n")))
