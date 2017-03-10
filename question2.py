def convert(var):
    try:
        return int(var)
    except ValueError:
        pass
    try:
        return float(var)
    except ValueError:
        pass
    return var

if __name__ == "__main__":
    print type(convert('1'))
    print type(convert('1.0'))
    print type(convert('asd'))