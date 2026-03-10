import textwrap

def wrap(string, max_width):
    w=textwrap.fill(string,max_width)
    return w

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)