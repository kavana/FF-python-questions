def min(first, second, third):
    min = first
    if(min > second):
        min = second
    if(third < min):
        min = third
    return min


if __name__ == "__main__":
    print min(2,3,4)