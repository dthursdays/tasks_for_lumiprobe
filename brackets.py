def main(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            if stack.pop() != '(':
                return False

    if stack:
        return False
    return True


if __name__ == '__main__':
    print(main(input()))
