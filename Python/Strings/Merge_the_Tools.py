def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s=string[i:i+k]
        us=dict.fromkeys(s)
        print("".join(us))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)