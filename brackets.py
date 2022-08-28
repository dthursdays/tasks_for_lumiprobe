def main(string):
    stack = []
    for symbol in string:
        if symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            if not stack or stack.pop() != '(':
                return False

    if stack:
        return False
    return True


if __name__ == '__main__':
    print(main(input()))
