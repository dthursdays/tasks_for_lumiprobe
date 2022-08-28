def main(string):
    amounts = {element: string.count(element) for element in set(string)}
    for key, value in amounts.items():
        if (value == max(amounts.values())):
            return (key, value)
    return 'На вход дана пустая строка'


if __name__ == '__main__':
    print(main(input('Введите строку:\n').lower()))
