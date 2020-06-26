def max_of_three(a: int, b: int, c: int) -> int:
    if (a == b) and a != c and a > c:
        return a
    elif (a == c) and a != b and a > b:
        return a
    elif a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


if __name__ == '__main__':
    res = max_of_three(a=3, b=2, c=2)
    print(res)
