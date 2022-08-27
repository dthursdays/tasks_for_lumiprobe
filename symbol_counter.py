def main(string):
    counts = {element: string.count(element) for element in set(string)}
    for key, value in counts.items():
        if (value == max(counts.values())):
            return (key, value)
    return 'На вход дана пустая строка'


if __name__ == '__main__':
    print(main(input().lower()))
