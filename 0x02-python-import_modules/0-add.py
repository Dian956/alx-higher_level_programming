#!/usr/bin/python3
from add_0 import add


def main():
    """Print the sum of 1 and 2."""
    a, b = 1, 2
    print(f"{a} + {b} = {add(a, b)}")


if __name__ == "__main__":
    main()
