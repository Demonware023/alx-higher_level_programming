#!/usr/bin/python3

if __name__ == "__main__":
    """\n"""

    from sys import argv

    def add(args):
        result = 0
        for i in range(len(args)):
            result += int(args[i])
        return (result)

    if (len(argv) == 1):
        print("0")
    elif (len(argv) >= 2):
        numbers = [int(arg) for arg in argv[1:]]
        result = add(numbers)
        print(result)
